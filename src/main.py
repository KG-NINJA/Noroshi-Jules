import os
import json
import datetime
from jinja2 import Environment, FileSystemLoader
from generator import ContentGenerator

# Configuration
OUTPUT_DIR = "public"
TEMPLATE_DIR = "src/templates"
DB_FILE = os.path.join(OUTPUT_DIR, "articles.json")

def load_history():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(DB_FILE, "w") as f:
        json.dump(history, f, indent=4)

def main():
    # Ensure output dir exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Setup Jinja2
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    article_template = env.get_template("article.html")
    index_template = env.get_template("index.html")

    # Generate Content
    gen = ContentGenerator()
    data = gen.generate_daily_content()

    # Create filename based on date and title slug
    slug = data["title"].lower().replace(" ", "-").replace("'", "")[:50]
    filename = f"{data['date']}-{slug}.html"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # Render Article
    print(f"Generating article: {data['title']}")
    html_content = article_template.render(**data)

    with open(filepath, "w") as f:
        f.write(html_content)

    # Update History
    history = load_history()

    # Remove entry if it already exists for this filename (update scenario)
    history = [h for h in history if h["filename"] != filename]

    # Add new entry
    new_entry = {
        "filename": filename,
        "title": data["title"],
        "description": data["description"],
        "date": data["date"],
        "topic": data["topic"],
        "keywords": data["keywords"]
    }
    history.insert(0, new_entry) # Add to top

    save_history(history)

    # Rebuild Index
    print("Rebuilding index...")
    index_html = index_template.render(articles=history)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w") as f:
        f.write(index_html)

    print("Success! Content published to public/")

if __name__ == "__main__":
    main()
