# scraper.py
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Configuration
URL = "https://oia.hanyang.ac.kr/notice"
KEYWORDS = ["internship", "인턴십", "채용", "취업", "모집"]
OUTPUT_FILE = "notices.json"
BASE_URL = "https://oia.hanyang.ac.kr"
USER_AGENT = "HanyangOIANoticeScraper/1.0 (+https://github.com/your-repo)" # Be polite, identify your bot

def fetch_notices():
    """Fetches the notice page HTML."""
    headers = {"User-Agent": USER_AGENT}
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {URL}: {e}")
        return None

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

        if not title_cell or not time_cell:
            continue # Skip header or malformed rows

        link_tag = title_cell.find('a')
        if not link_tag:
            continue

        title = link_tag.get_text(strip=True)
        relative_link = link_tag.get('href') 
        absolute_link = BASE_URL + relative_link if relative_link else None
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
    """Saves the filtered notices to a JSON file."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, OUTPUT_FILE)
    
    output_data = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "notices": notices
    }
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        print(f"Successfully saved {len(notices)} filtered notices to {output_path}")
    except IOError as e:
        print(f"Error saving notices to {output_path}: {e}")


if __name__ == "__main__":
    print(f"Fetching notices from {URL}...")
    html = fetch_notices()
    if html:
        print("Parsing notices...")
        all_notices = parse_notices(html)
        print(f"Found {len(all_notices)} total notices on the first page.")
        
        print(f"Filtering notices with keywords: {KEYWORDS}...")
        filtered = filter_notices(all_notices)
        print(f"Found {len(filtered)} relevant notices.")
        
        print(f"Saving filtered notices to {OUTPUT_FILE}...")
        save_notices(filtered)
    else:
        print("Scraping failed.") 