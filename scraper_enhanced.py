# scraper_enhanced.py
# Updated version with Groq integration for AI analysis and summarization
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
import time
from groq import Groq, RateLimitError

# Configuration
URL = "https://oia.hanyang.ac.kr/notice"
KEYWORDS = ["internship", "인턴십", "채용", "취업", "모집"]
BASE_URL = "https://oia.hanyang.ac.kr"
USER_AGENT = "HanyangOIANoticeScraper/1.0 (+https://github.com/aideedamsyar/OIA-Agent)"
WEB_APP_DIR = "web"
DATA_DIR = os.path.join(WEB_APP_DIR, "src", "data")
OUTPUT_FILE_NAME = "notices.json"
GROQ_MODEL = "llama3-8b-8192"  # Fast and capable model from Groq
CJK_THRESHOLD = 0.6  # % of text that triggers non-Korean/English flag

# --- Groq API Client Initialization ---
groq_client = None
groq_api_key = os.environ.get("GROQ_API_KEY")
if groq_api_key:
    try:
        groq_client = Groq(api_key=groq_api_key)
        print("Groq client initialized.")
    except Exception as e:
        print(f"Error initializing Groq client: {e}")
else:
    print("Warning: GROQ_API_KEY environment variable not found. AI analysis will be skipped.")

# --- Helper Functions ---

def fetch_page(url):
    """Fetches HTML content from a given URL."""
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers, timeout=15)  # Increased timeout for detail pages
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def fetch_notices():
    """Fetches the notice page HTML from the main URL."""
    return fetch_page(URL)

def fetch_notice_detail(url):
    """Fetches and extracts the main text content from a notice detail page."""
    html_content = fetch_page(url)
    if not html_content:
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    # Try different selectors for main content areas
    content_selectors = ['#content', 'div.view_content', 'div.board-contents', '.content', 'article', 'main']
    content_area = None
    for selector in content_selectors:
        content_area = soup.select_one(selector)
        if content_area:
            break
    
    if not content_area:
        print(f"Warning: Could not find main content area for URL {url}")
        # Fallback: return all visible text
        return soup.get_text(separator=' ', strip=True)

    # Extract text from the content area
    text = content_area.get_text(separator=' ', strip=True)
    return text

def check_language(text):
    """
    Performs a basic language check based on character ranges.
    Returns True if likely Korean/English, False if predominantly CJK/Japanese.
    """
    if not text or len(text) == 0:
        return True  # Assume okay if no text
    
    text_len = len(text)
    cjk_count = 0
    
    # Unicode ranges for Chinese/Japanese characters
    for char in text:
        ord_char = ord(char)
        if (0x4E00 <= ord_char <= 0x9FFF or  # CJK main block
            0x3040 <= ord_char <= 0x309F or  # Hiragana
            0x30A0 <= ord_char <= 0x30FF):   # Katakana
            cjk_count += 1

    cjk_ratio = cjk_count / text_len
    # Return True if below threshold (likely Korean/English), False otherwise
    return cjk_ratio < CJK_THRESHOLD

def analyze_notice_content(client, text):
    """
    Uses Groq API to classify notice relevance and generate a summary.
    Returns (is_direct_opportunity: bool, summary: str | None)
    """
    if not client:
        print("Skipping AI analysis: Groq client not available.")
        return False, None
    
    if not text or len(text.strip()) < 50:  # Skip if text is too short
        print("Skipping AI analysis: Text content too short.")
        return False, None

    # Limit text length to avoid excessive token usage
    max_len = 8000
    truncated_text = text[:max_len] if len(text) > max_len else text

    prompt = f"""
Analyze the following text from a university notice board.
First, on a line by itself, write only 'Yes' if it describes a specific job or internship opportunity students can directly apply for, or write only 'No' if it's primarily an announcement for an information session, career fair, workshop, general advice, or other non-application event.
Second, on the next line, provide a concise one-sentence summary of the notice's main point, focusing on the opportunity if available.

Text:
{truncated_text}
"""
    try:
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant analyzing university notices. Follow the output format precisely: Line 1 is 'Yes' or 'No'. Line 2 is a one-sentence summary."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1,  # Lower temperature for more deterministic output
            max_tokens=100,   # Allow enough tokens for Yes/No + summary
        )
        
        response_content = completion.choices[0].message.content
        if not response_content:
            print("Warning: Empty response from Groq.")
            return False, None

        lines = response_content.strip().split('\n', 1)  # Split into max 2 parts

        # Classification
        classification_line = lines[0].strip().lower()
        is_direct_opportunity = classification_line == 'yes'

        # Summary
        summary = None
        if len(lines) > 1:
            summary = lines[1].strip()
            # Clean up potential artifacts if summary is very short or repetitive
            if len(summary) < 15 or summary.lower() in classification_line:
                summary = None

        return is_direct_opportunity, summary

    except RateLimitError:
        print("Warning: Groq rate limit hit. Skipping AI analysis for this notice.")
        return False, None
    except Exception as e:
        print(f"Error during Groq API call: {e}")
        return False, None

def parse_notices(html_content):
    """Parses the HTML to extract notice details."""
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='list_wrap')
    if not table:
        print("Error: Could not find the notice table.")
        return []

    tbody = table.find('tbody')
    if not tbody:
        print("Error: Could not find the table body.")
        return []

    notices = []
    rows = tbody.find_all('tr')

    for row in rows:
        title_cell = row.find('td', class_='title')
        time_cell = row.find('td', class_='time')

        # Skip header rows or malformed rows
        if not title_cell or not time_cell or row.find('th'):
            continue

        link_tag = title_cell.find('a')
        if not link_tag:
            continue

        title = link_tag.get_text(strip=True)
        relative_link = link_tag.get('href')
        
        # Construct absolute link properly
        if relative_link and not relative_link.startswith('http'):
            absolute_link = BASE_URL + (relative_link if relative_link.startswith('/') else '/' + relative_link)
        elif relative_link:
            absolute_link = relative_link  # Already absolute
        else:
            absolute_link = None

        date_str = time_cell.get_text(strip=True)

        if title and absolute_link and date_str:
            notices.append({
                "title": title,
                "link": absolute_link,
                "date": date_str
            })

    return notices

def filter_notices(notices):
    """Filters notices based on keywords in the title."""
    filtered = []
    for notice in notices:
        title_lower = notice['title'].lower()
        if any(keyword.lower() in title_lower for keyword in KEYWORDS):
            filtered.append(notice)
    return filtered

def save_notices(notices):
    """Saves the enriched notices to a JSON file inside the web app's data directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_data_dir = os.path.join(script_dir, DATA_DIR)
    output_path = os.path.join(target_data_dir, OUTPUT_FILE_NAME)

    # Create the target directory if it doesn't exist
    os.makedirs(target_data_dir, exist_ok=True)

    output_data = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "notices": notices
    }

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        print(f"Successfully saved {len(notices)} processed notices to {output_path}")
    except IOError as e:
        print(f"Error saving notices to {output_path}: {e}")

# --- Main Execution Logic ---
if __name__ == "__main__":
    print(f"[{datetime.now()}] Starting scraper run...")
    print(f"Fetching main notice list from {URL}...")
    main_html = fetch_notices()

    if main_html:
        print("Parsing main notice list...")
        all_notices = parse_notices(main_html)
        print(f"Found {len(all_notices)} total notices on the first page.")

        print(f"Filtering notices with keywords: {KEYWORDS}...")
        filtered_initial = filter_notices(all_notices)
        print(f"Found {len(filtered_initial)} notices matching keywords.")

        enriched_notices = []
        print("Processing relevant notices (fetching details, language check, AI analysis)...")
        
        for i, notice in enumerate(filtered_initial):
            print(f"Processing notice {i+1}/{len(filtered_initial)}: {notice['title'][:50]}...")
            
            detail_text = fetch_notice_detail(notice['link'])
            
            # Initialize enrichment fields
            notice['passed_language_check'] = None
            notice['is_direct_opportunity'] = None
            notice['summary'] = None
            
            if detail_text:
                # 1. Language Check
                notice['passed_language_check'] = check_language(detail_text)
                print(f"  - Language check passed: {notice['passed_language_check']}")

                # 2. AI Analysis (if language check passed and client available)
                if notice['passed_language_check'] and groq_client:
                    is_opportunity, summary = analyze_notice_content(groq_client, detail_text)
                    notice['is_direct_opportunity'] = is_opportunity
                    notice['summary'] = summary
                    print(f"  - AI: Direct Opportunity={is_opportunity}, Summary='{summary}'")
                elif not notice['passed_language_check']:
                    print("  - AI: Skipped (Language Check Failed)")
                    notice['is_direct_opportunity'] = False  # Mark as not relevant if language failed
                else:  # Language passed, but no Groq client
                    print("  - AI: Skipped (Groq client not initialized)")
                    # Keep is_direct_opportunity as None - we don't know
            else:
                print("  - Warning: Failed to fetch detail text.")
                notice['passed_language_check'] = False  # Cannot check language
                notice['is_direct_opportunity'] = False  # Cannot analyze

            enriched_notices.append(notice)
            
            # Be polite - add a small delay between detail page fetches / AI calls
            time.sleep(1.5)

        print(f"Saving {len(enriched_notices)} processed notices to {os.path.join(DATA_DIR, OUTPUT_FILE_NAME)}...")
        save_notices(enriched_notices)
    else:
        print("Scraping failed: Could not fetch main notice page.")

    print(f"[{datetime.now()}] Scraper run finished.") 