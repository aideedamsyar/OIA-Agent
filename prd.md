✍️ Brand Copy & Typography System
For headers, sections, and general page text

🎯 Tone:
Professional, not corporate

Calm, confident, and focused

Uses short, declarative sentences

Avoids hype or fluff — just clarity and relevance

📢 Brand Slogan (Hero Section)
Opportune
Right place. Right time.
Discover curated job and internship opportunities from Korea's top universities — all in one place.

🗂 Section Headings + Microcopy
🔍 Latest Opportunities
Fresh listings updated daily from university job boards.
Browse internships, part-time roles, and full-time career notices — without checking every school manually.

🎓 Trusted Sources
Handpicked from top universities.
We monitor official career boards from institutions like SNU, POSTECH, Yonsei, and more.

🤖 Smart Filtering
Less noise, more signal.
AI-powered filters surface real job listings, not just information sessions or event flyers.

📌 Save What Matters
Stay organized with your personal watchlist (coming soon).
Bookmark posts and receive notifications when deadlines approach.

🧬 Footer Tagline
Built by students, for students.
Opportune is open-source and driven by a mission to make opportunity more accessible.

🧩 Page Structure — Bloomberg-Inspired Layout
Let's break it into clear visual sections. Think strong grid, subtle dividers, data-forward, and no visual fluff.

┌───────────────────────────────────────────────────────────────┐
│                      Sticky Top Header                        │
│   ┌──────────────┐    ┌─────────────┐   ┌───────────────┐     │
│   │   Opportune  │    │ Home        │   │ About         │     │
└───────────────────────────────────────────────────────────────┘

┌──────────────────────────── Hero Section ─────────────────────────────┐
│  [ LOGO ]               Opportune                                     │
│                     Right place. Right time.                         │
│  Discover curated job and internship opportunities...                │
└──────────────────────────────────────────────────────────────────────┘

╭────────── Grid Divider ──────────╮
│                                  │
│     LATEST OPPORTUNITIES         │   ← Heading
│     Fresh listings updated daily │   ← Subhead
│                                  │
╰──────────────────────────────────╯

[ NoticeCard ]   [ NoticeCard ]   [ NoticeCard ]
[ NoticeCard ]   [ NoticeCard ]   [ NoticeCard ]

╭────────── Grid Divider ──────────╮
│   🎓 TRUSTED SOURCES             │
│   Posts from verified university│
╰──────────────────────────────────╯

[ UniversityCard: SNU ]   [ POSTECH ]   [ Yonsei ]

╭────────── Grid Divider ──────────╮
│   🤖 SMART FILTERING              │
│   AI hides noise, highlights jobs│
╰──────────────────────────────────╯

[ Card with AI Summary + Score Bar ]

╭────────── Footer Divider ────────╮
│   Built by students, for students│
│   GitHub · Privacy · Terms       │
╰──────────────────────────────────╯

🧱 CSS & Tailwind Layout Hints
Page Shell

<div className="min-h-screen bg-background text-neutral-900 font-sans">
  <Header />
  <main className="max-w-7xl mx-auto px-6 py-12 space-y-16">
    <Hero />
    <Section title="Latest Opportunities" subtitle="Fresh listings updated daily from university job boards.">
      <NoticesGrid />
    </Section>
    <Section title="Trusted Sources" subtitle="Handpicked from Korea's top universities.">
      <UniversityCards />
    </Section>
    <Section title="Smart Filtering" subtitle="AI surfaces real jobs, not noise.">
      <AISummaryCards />
    </Section>
  </main>
  <Footer />
</div>

Dividers / Bloomberg Style Lines
<div className="border-t border-neutral-300 w-full my-8" />

Use these to segment each section — just like Bloomberg does on both light and dark mode. Combine with subtle uppercase text-xs tracking-wider for section headers.


Typography Details (Tailwind + IBM Plex)

<h1 className="text-4xl md:text-5xl font-bold tracking-tight">
  Opportune
</h1>

<p className="text-lg text-neutral-700 mt-2">
  Right place. Right time.
</p>

<h2 className="text-xl font-semibold tracking-wide uppercase text-neutral-800 border-b pb-2">
  Latest Opportunities
</h2>

<p className="text-sm text-neutral-600 mb-4">
  Curated notices, updated daily from real university sources.
</p>

🎯 Extra Touches to Match Bloomberg Feel
Sticky Header: Always in view with logo + quick nav

Monochrome icons or Lucide/Feather icons only

Minimal hover effects: hover:underline, hover:bg-neutral-100

No shadows unless very light (shadow-sm, not shadow-xl)

Wide grids: Bloomberg uses plenty of whitespace and breathing room

Responsive layout: Keep it clean on mobile — no cramming


# Product Requirements Document: Hanyang OIA Notice Scraper

# App Name: Opportune

## 1. Introduction & Goal

This project aims to build a web application that automatically fetches, filters, and displays relevant job and internship opportunities from the Hanyang University Office of International Affairs (OIA) notice board. The goal is to provide students with a centralized and easy-to-access view of career-related announcements, saving them the effort of manually checking the OIA website daily.

## 2. Requirements

### Functional Requirements

*   **F1: Daily Scraping:** The system must automatically scrape the first page of the Hanyang OIA notice board (`https://oia.hanyang.ac.kr/notice`) once per day.
*   **F2: Content Filtering:** The system must parse the scraped content and filter notices based on keywords indicating job or internship opportunities. The primary keywords are: `internship`, `인턴십`, `채용`, `취업`, `모집`. Only notices containing these keywords in their title on the *first page* should be considered relevant.
*   **F3: Data Storage:** Filtered notices (including title, link, date) must be stored persistently.
*   **F4: Web Interface:** A web interface must display the filtered notices in a clean, user-friendly manner.
*   **F5 (Optional): AI Relevance Analysis:** For each filtered notice, fetch the detailed content by following its link. Use an AI service (e.g., Groq's free tier) to analyze the content and determine its relevance more accurately (e.g., distinguishing actual job postings from general recruitment information sessions).
*   **F6 (Optional): Display AI Summary:** If F5 is implemented, display a brief summary or relevance score generated by the AI alongside the notice title.

### Non-Functional Requirements

*   **NF1: Free Hosting:** The entire application (backend scraping logic, data storage, frontend) must be hostable using free service tiers.
*   **NF2: Performance:** The web interface should load quickly. Scraping should be efficient and avoid overloading the source website.
*   **NF3: Reliability:** The scraping process should be robust against minor HTML structure changes if possible, though significant changes might require manual updates.
*   **NF4: UI/UX:** The web interface should have a professional look and feel, adhering to the Opportune Design System defined below.

## 3. Proposed Stack & Architecture

*   **Automation Engine:** **GitHub Actions**
    *   *Reasoning:* Provides free compute time for scheduled tasks (cron jobs), perfect for daily scraping. Integrates directly with the code repository.
*   **Scraping Script:** **Python** with `requests` (for fetching HTML) and `BeautifulSoup4` (for parsing HTML).
    *   *Reasoning:* Mature and robust libraries for web scraping. Python is well-suited for scripting and data manipulation. Runs easily within GitHub Actions.
*   **Data Storage:** **JSON file** stored within the GitHub repository.
    *   *Reasoning:* Simplest approach for a small amount of data. Free, version-controlled, and easily accessible by the frontend deployed from the same repository. Avoids the complexity and potential costs/limits of external databases on free tiers.
*   **Frontend Framework:** **Next.js (React)**
    *   *Reasoning:* Excellent for building static and server-rendered applications. Integrates well with Vercel/Netlify for free hosting. Strong community support and works seamlessly with `shadcn/ui`.
*   **UI Library:** **shadcn/ui** + **Tailwind CSS**
    *   *Reasoning:* User request. Provides beautiful, accessible components built on Tailwind CSS, allowing for rapid UI development.
*   **Hosting:** **Vercel** or **Netlify**
    *   *Reasoning:* Offer generous free tiers for hosting static sites and serverless functions (if needed later). Integrate seamlessly with GitHub for continuous deployment.
*   **AI Service (Optional):** **Groq API**
    *   *Reasoning:* User suggestion. Offers a fast inference engine potentially available with a free tier suitable for analyzing a small number of posts daily. Requires API key management.

### Architecture Overview

1.  **GitHub Action (Scheduled Daily):**
    *   Checks out the repository.
    *   Runs the Python scraping script.
2.  **Python Scraper:**
    *   Fetches HTML from `https://oia.hanyang.ac.kr/notice`.
    *   Parses the HTML using BeautifulSoup to find the notice table.
    *   Iterates through rows on the first page.
    *   Filters rows based on keywords in the title.
    *   *(Optional AI Step)*: For each filtered notice, fetches the notice detail page URL. Sends the content to Groq API for analysis/summarization.
    *   Formats the filtered data (title, link, date, optional AI summary) into a structured list.
    *   Overwrites/updates the `notices.json` file in the repository.
    *   Commits and pushes the updated `notices.json` file back to the repository.
3.  **Next.js Frontend (Hosted on Vercel/Netlify):**
    *   When a user visits the site, the Next.js application fetches the `notices.json` file (statically at build time or client-side).
    *   Renders the list of notices using React components styled with `shadcn/ui` and Tailwind CSS.
4.  **Deployment:** The push to the main branch (triggered by the GitHub Action updating `notices.json` or by code changes) automatically triggers a new deployment on Vercel/Netlify.

## 4. Risks & Challenges

*   **Website Structure Changes:** The OIA website's HTML structure may change, breaking the scraper. Requires monitoring and potential script updates.
*   **Scraping Blocks:** The university might implement measures to block scraping (e.g., IP bans, CAPTCHAs). The script should use appropriate headers (User-Agent) and potentially delays to minimize risk.
*   **Terms of Service:** Verify Hanyang OIA's terms of service regarding automated scraping. Proceed ethically and avoid excessive requests.
*   **AI Costs/Limits:** If implementing the optional AI feature, monitor Groq API usage to stay within free tier limits. API keys need secure management (e.g., GitHub Secrets).
*   **Keyword Accuracy:** The initial keyword filtering might include irrelevant posts (e.g., a general recruitment *information session* vs. a specific job *posting*). The optional AI step aims to mitigate this.

## 5. Future Considerations

*   Scraping multiple pages.
*   User accounts for saving/tracking notices.
*   Email/push notifications for new relevant posts.
*   More sophisticated relevance filtering (NLP without external AI).
*   Historical data tracking.

## 6. Implementation Plan

This project will be implemented in the following phases:

**Phase 1: Core Scraper Development**
*   [x] Finalize and test the Python script (`scraper.py`) to fetch the main notice page.
*   [x] Implement HTML parsing logic using BeautifulSoup to extract all notices (title, link, date) from the first page table.
*   [x] Implement keyword filtering logic.
*   [x] Implement logic to save the filtered notices to `notices.json` with a timestamp.
*   [x] Thoroughly test the scraper locally with the target URL.

**Phase 2: Automation Setup**
*   [x] Create a GitHub Actions workflow file (`.github/workflows/scrape.yml`).
*   [x] Configure the workflow to run on a daily schedule (e.g., `cron: '0 0 * * *'` for midnight UTC).
*   [x] Add steps to check out the code, set up Python, install dependencies (`requests`, `beautifulsoup4`).
*   [x] Add a step to execute `scraper.py`.
*   [x] Add steps to commit and push the updated `notices.json` back to the repository if changes are detected.
*   [x] Test the workflow manually and verify scheduled runs.

**Phase 3: Frontend Project Setup**
*   [x] Initialize a new Next.js project (using `create-next-app`).
*   [x] Integrate Tailwind CSS.
*   [x] Set up `shadcn/ui` following its documentation.
*   [x] Create the basic layout and page structure (e.g., `app/page.tsx`).

**Phase 4: Basic Frontend Display**
*   [x] Implement logic to fetch or read the `notices.json` data within the Next.js application (Static Site Generation (SSG) preferred for performance).
*   [x] Design the notice display using `shadcn/ui` components (e.g., `<Card>` for each notice or a `<Table>`).
*   [x] Display the notice title, date, and provide a clickable link to the original notice URL.
*   [x] Add basic styling for a clean and functional appearance.
*   [x] Display the "Last Updated" timestamp from `notices.json`.

**(Note: Detailed styling deferred to Phase 5)**

**Phase 5: Design System Implementation**
*   [ ] Set up IBM Plex Sans font in the Next.js project.
*   [ ] Implement reusable `Header` and `Footer` components based on the Design System (`7.5 Navigation`).
*   [ ] Implement the `Hero` section with brand copy (`7.0 Brand Voice & Copy`).
*   [ ] Structure the main page layout using Sections and Dividers (`7.3 Layout Guidelines`).
*   [ ] Style the existing `NoticeCard` component according to the Design System spec (`7.4 Components`).
*   [ ] Apply the Opportune color palette (`7.2 Color System`) and typography scale (`7.1 Typography`) globally.
*   [ ] Implement utility states: Empty State (`7.6 Utility States`) for when no notices are found.
*   [ ] Implement utility states: Loading Skeleton (`7.6 Utility States`) for initial page load (optional enhancement).

**Phase 6: Deployment**
*   [ ] Create a new project on Vercel (or Netlify).
*   [ ] Link the Vercel project to the GitHub repository (`aideedamsyar/OIA-Agent`).
*   [ ] Configure Vercel build settings (Framework: Next.js, Root Directory: `web`).
*   [ ] Trigger the first deployment.
*   [ ] Verify successful deployment and public URL access.
*   [ ] Verify that pushes to the main branch (including those by the GitHub Action) trigger automatic redeployments on Vercel.

**Phase 7: (Optional) AI Relevance Analysis & Summarization**
*   [ ] If pursuing, obtain a Groq API key and add it as a **GitHub Secret** for secure access within the GitHub Action.
*   [ ] Update scraper dependencies (`requirements.txt` or similar) to include the `groq` library.
*   [ ] Modify `scraper.py`:
    *   For notices passing the initial keyword filter, add function(s) to fetch the full content of the individual notice detail page using its link.
    *   Implement a **language check** on the fetched detail page text (e.g., using character range analysis) to identify and flag notices primarily in Chinese or Japanese. Store this check result (e.g., `passed_language_check: boolean`).
    *   If the language check passes (indicating likely Korean/English content):
        *   Integrate Groq API call using the `groq` library and the API key (read from environment variables set by GitHub Secrets).
        *   Construct a prompt asking the AI model (e.g., `deepseek-r1-distill-llama-70b`) to perform two tasks:
            1.  Classify if the notice is a direct job/internship opportunity (respond 'Yes' or 'No').
            2.  Provide a concise one-sentence summary of the notice.
        *   Parse the AI's response to extract the classification and the summary.
        *   Handle potential API errors or unexpected response formats gracefully.
    *   Update the data structure saved to `notices.json` to include the new fields for each notice: `passed_language_check` (boolean), `is_direct_opportunity` (boolean, derived from AI response, null/false if language check failed or AI said 'No'), and `summary` (string, from AI, null if language check failed or AI didn't provide one).
*   [ ] Modify the GitHub Actions workflow (`.github/workflows/scrape.yml`):
    *   Ensure the step installing Python dependencies uses the updated requirements file.
    *   Pass the Groq API key stored in GitHub Secrets as an environment variable (e.g., `GROQ_API_KEY`) to the `scraper.py` execution step.
*   [ ] Modify the Next.js frontend (`web/src/app/page.tsx`):
    *   Update the TypeScript interface/type definition for a `Notice` to include the new fields (`passed_language_check`, `is_direct_opportunity`, `summary`).
    *   Update the `NoticeCard` component logic:
        *   Conditionally display the `summary` text if it exists.
        *   Optionally, use `is_direct_opportunity` and `passed_language_check` to filter which notices are displayed by default, or add visual indicators (e.g., a 'Verified Job' badge using `shadcn/ui` Badge component and `--success` color from the design system) to cards that meet the criteria.

## 7. Opportune Design System

### 7.0 Brand Voice & Copy

**🎯 Tone:**
*   Professional, not corporate
*   Calm, confident, and focused
*   Uses short, declarative sentences
*   Avoids hype or fluff — just clarity and relevance

**📢 Brand Slogan (Hero Section):**
> Opportune
> Right place. Right time.
> Discover curated job and internship opportunities from Korea's top universities — all in one place.

**🗂 Section Headings + Microcopy:**

*   **🔍 Latest Opportunities**
    *   *Fresh listings updated daily from university job boards.* 
    *   *Browse internships, part-time roles, and full-time career notices — without checking every school manually.*
*   **🎓 Trusted Sources**
    *   *Handpicked from top universities.* 
    *   *We monitor official career boards from institutions like SNU, POSTECH, Yonsei, and more.*
*   **🤖 Smart Filtering**
    *   *Less noise, more signal.*
    *   *AI-powered filters surface real job listings, not just information sessions or event flyers.*
*   **📌 Save What Matters**
    *   *Stay organized with your personal watchlist (coming soon).* 
    *   *Bookmark posts and receive notifications when deadlines approach.*

**🧬 Footer Tagline:**
> Built by students, for students.
> Opportune is open-source and driven by a mission to make opportunity more accessible.

### 7.1 Typography

*Typeface: IBM Plex Sans — Bloomberg vibes, no-nonsense readability.*

**Import:**
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
```

**Tailwind Configuration:**
```typescript
// tailwind.config.ts
{
  theme: {
    extend: {
      fontFamily: {
        sans: ['"IBM Plex Sans"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
    },
  },
}
```

**Scale & Usage Examples:**

| Style           | Tailwind Class                    | Example Usage                       |
| --------------- | --------------------------------- | ----------------------------------- |
| Hero Title      | `text-4xl md:text-5xl font-bold tracking-tight` | Opportune (Brand Name)              |
| Hero Subtitle   | `text-lg text-neutral-700 mt-2`     | Right place. Right time.            |
| Page Title      | `text-3xl md:text-4xl font-bold`    | Other primary headers               |
| Section Title   | `text-xl font-semibold tracking-wide uppercase text-neutral-800 border-b pb-2` | LATEST OPPORTUNITIES            |
| Section Subhead | `text-sm text-neutral-600 mb-4`     | Curated notices...                  |
| Card Title      | `text-base font-semibold text-neutral-900` | Backend Internship @ Naver          |
| Body Text       | `text-sm text-neutral-700` or `text-neutral-900` | Notice summaries, descriptions      |
| Metadata / Label| `text-xs text-neutral-500`        | Date, tags, university name         |
| Button Text     | `text-sm font-medium uppercase`   | Action buttons                      |

### 7.2 Color System

*A modern grayscale with sharp blue accent — gives it a data-platform + editorial look.*

| Token         | Hex      | Usage                                  |
| ------------- | -------- | -------------------------------------- |
| --primary     | #3B82F6  | Accent, links, active states           |
| --primary-light| #DBEAFE  | Badges, background fills               |
| --neutral-900 | #111827  | Main text                              |
| --neutral-800 | #1F2937  | Section Headers (per Typography)       |
| --neutral-700 | #374151  | Secondary text, Hero Subtitle          |
| --neutral-600 | #4B5563  | Section Subheads                       |
| --neutral-500 | #6B7280  | Metadata / Labels                      |
| --neutral-300 | #D1D5DB  | Lines, borders                         |
| --neutral-200 | #E5E7EB  | Loading Skeleton background            |
| --neutral-100 | #F3F4F6  | Card background hover, subtle fill     |
| --background  | #F9FAFB  | Page background                        |
| --white       | #FFFFFF  | Card, panel surfaces                   |
| --success     | #10B981  | Relevance indicator, verified tags     |
| --warning     | #F59E0B  | Info sessions, cautionary tags         |

*(Note: Added/adjusted neutral shades based on typography examples)*

### 7.3 Layout Guidelines

**Page Structure Concept (Bloomberg-Inspired):**
```
┌───────────────────────────────────────────────────────────────┐
│                      Sticky Top Header                        │
│   ┌──────────────┐    ┌─────────────┐   ┌───────────────┐     │
│   │   Opportune  │    │ Home        │   │ About         │     │
└───────────────────────────────────────────────────────────────┘

┌──────────────────────────── Hero Section ─────────────────────────────┐
│  [ LOGO ]               Opportune                                     │
│                     Right place. Right time.                         │
│  Discover curated job and internship opportunities...                │
└──────────────────────────────────────────────────────────────────────┘

╭────────── Grid Divider ──────────╮
│                                  │
│     LATEST OPPORTUNITIES         │   ← Heading
│     Fresh listings updated daily │   ← Subhead
│                                  │
╰──────────────────────────────────╯

[ NoticeCard ]   [ NoticeCard ]   [ NoticeCard ]
[ NoticeCard ]   [ NoticeCard ]   [ NoticeCard ]

╭────────── Grid Divider ──────────╮
│   🎓 TRUSTED SOURCES             │
│   Posts from verified university│
╰──────────────────────────────────╯

[ UniversityCard: SNU ]   [ POSTECH ]   [ Yonsei ]

╭────────── Grid Divider ──────────╮
│   🤖 SMART FILTERING              │
│   AI hides noise, highlights jobs│
╰──────────────────────────────────╯

[ Card with AI Summary + Score Bar ]

╭────────── Footer Divider ────────╮
│   Built by students, for students│
│   GitHub · Privacy · Terms       │
╰──────────────────────────────────╯
```

**Page Shell Example:**
```tsx
<div className="min-h-screen bg-background text-neutral-900 font-sans">
  <Header /> {/* Sticky Header Component */} 
  <main className="max-w-7xl mx-auto px-6 py-12 space-y-16">
    <Hero /> {/* Hero Section Component */} 
    <Section title="Latest Opportunities" subtitle="Fresh listings updated daily from university job boards.">
      <NoticesGrid /> {/* Grid of Notice Cards */} 
    </Section>
    
    {/* Divider */} 
    <div className="border-t border-neutral-300 w-full" /> 
    
    <Section title="Trusted Sources" subtitle="Handpicked from Korea's top universities.">
      <UniversityCards /> {/* Placeholder */} 
    </Section>
    
    {/* Divider */} 
    <div className="border-t border-neutral-300 w-full" /> 
    
    <Section title="Smart Filtering" subtitle="AI surfaces real jobs, not noise.">
      <AISummaryCards /> {/* Placeholder */} 
    </Section>
  </main>
  <Footer /> {/* Footer Component */} 
</div>
```

**Dividers:**
*   Use simple borders: `<div className="border-t border-neutral-300 w-full my-8" />` or similar variants (`my-12`, `my-16`).

**Grid Layout:**
*   Main content grid for notices: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`

**Spacing Rules:**

| Item                  | Tailwind Spacing Example |
| --------------------- | ------------------------ |
| Main Content Padding  | px-6 py-12               |
| Section Vertical Space| space-y-16               |
| Card Padding          | p-6                      |
| Grid Item Gap         | gap-6                    |

### 7.4 Components

**Notice Card:**
```tsx
<Card className="bg-white border border-neutral-300 rounded-xl shadow-sm hover:shadow-md transition-all p-6 space-y-3">
  <div className="flex justify-between items-center">
    {/* Adjusted to use text sizes from Typography section */} 
    <h3 className="text-base font-semibold text-neutral-900 line-clamp-2">
      Backend Internship @ Naver
    </h3>
    {/* Requires Badge component */} 
    <Badge className="bg-primary-light text-primary text-xs font-medium px-2 py-1 rounded-full uppercase">
      POSTECH
    </Badge>
  </div>

  <p className="text-sm text-neutral-700 line-clamp-3">
    Naver is recruiting backend interns with experience in Python or Go...
  </p>

  <div className="flex justify-between items-center text-xs text-neutral-500">
    <span>2025.04.10</span>
    <a href="#" className="text-primary hover:underline">View →</a>
  </div>
</Card>
```
*(Note: Assumes existence of `Card` and `Badge` components from shadcn/ui or custom)*

**Tags and Badges:**

| Type            | Example Class                                      |
| --------------- | -------------------------------------------------- |
| Verified Posting| `bg-success/10 text-success px-2 py-0.5 rounded-full` |
| Info Session    | `bg-warning/10 text-warning px-2 py-0.5 rounded-full`|
| Keyword Tag     | `bg-neutral-100 text-neutral-700 text-xs px-2 py-1 rounded` |
*(Note: Apply these classes within a `<span>` or `Badge` component)*

### 7.5 Navigation

**Sticky Header:**
```tsx
<header className="sticky top-0 z-50 bg-white border-b border-neutral-200 px-6 py-4 flex justify-between items-center">
  {/* Adjusted to use text sizes from Typography section */} 
  <span className="text-xl font-semibold text-primary">Opportune</span>
  <nav className="flex gap-6 text-sm text-neutral-700">
    <a href="/" className="hover:text-primary">Home</a>
    <a href="/about" className="hover:text-primary">About</a>
  </nav>
</header>
```

### 7.6 Utility States

**Empty State:**
```tsx
<div className="text-center py-12 text-neutral-500">
  <p>No relevant notices today. Check back tomorrow.</p>
</div>
```

**Loading Skeleton:**
```tsx
<div className="animate-pulse bg-neutral-200 h-28 rounded-lg" />
```

### 7.7 Future Additions
*   Dark Mode: IBM Plex Sans looks gorgeous in dark themes — great for late-night job hunters.
*   Data Filters: Dropdown to filter by university or tag.
*   Compact Mode: Bloomberg-like table view for dense scanning.

### 7.8 Design Principles (Bloomberg Feel)
*   **Structure:** Use clear visual sections with grid layouts and subtle dividers (`border-t`).
*   **Whitespace:** Employ ample whitespace and breathing room (e.g., `max-w-7xl`, `px-6`, `py-12`, `space-y-16`, `gap-6`).
*   **Focus:** Data-forward, no visual fluff.
*   **Icons:** Use monochrome icons only (e.g., Lucide/Feather).
*   **Interactions:** Minimal hover effects (`hover:underline`, `hover:bg-neutral-100`).
*   **Shadows:** Avoid heavy shadows; use `shadow-sm` lightly if needed.
*   **Responsiveness:** Ensure clean mobile layout without cramming elements.
*   **Navigation:** Sticky header for persistent branding and navigation.


---

*Previous Sections (Introduction, Requirements, Stack, Plan, etc.) remain above this section.*