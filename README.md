# KGNINJA Auto-Spreader System

KGNINJA Auto-Spreader is a small publishing pipeline that generates daily knowledge articles,
stores metadata, and rebuilds an archive page for quick discovery. It is designed to
systematically diffuse KGNINJA information via static HTML output so it can be hosted on any
static hosting service.

## What this system does

- **Generates daily content** based on curated topics.
- **Publishes a new article HTML file** into the `public/` directory.
- **Updates the archive index** so the newest content is visible immediately.
- **Persists metadata** in `public/articles.json` for dashboards or analytics tools.

## How to run it

```bash
pip install -r requirements.txt
python src/main.py
```

After running the generator, open `public/index.html` in a browser to view the archive page.

## Diffusion & impact dashboard

A lightweight dashboard lives in `docs/dashboard/index.html`. It reads
`public/articles.json` (if available) to show diffusion activity such as total articles,
latest publish date, and topic mix. If `public/` is missing, the dashboard will fall back to
placeholder values so it is safe to open anytime.

To view it locally:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000/docs/dashboard/> in your browser.

## Repository layout

- `src/` - Content generator and templates.
- `public/` - Generated output (ignored by git).
- `docs/` - Operational documentation and dashboards.
