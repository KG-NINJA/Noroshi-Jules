# System verification report

## What was checked
- Confirmed `src/main.py` generates a daily article HTML file, updates `public/articles.json`, and rebuilds `public/index.html`.
- Verified the Jinja2 templates used for rendering the article and index pages.

## Evidence
- Ran `python src/main.py`, which reported successful generation and index rebuild.
- The generator selected a topic based on the day-of-year and created a deterministic article payload.

## How to reproduce
1. Install dependencies: `pip install -r requirements.txt`
2. Run the generator: `python src/main.py`
3. Open `public/index.html` in a browser to confirm the archive page lists the latest article.
