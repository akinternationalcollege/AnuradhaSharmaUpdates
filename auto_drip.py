import os
import shutil
import datetime

unpublished_dir = "_unpublished"
posts_dir = "_posts"

os.makedirs(posts_dir, exist_ok=True)

articles = sorted(os.listdir(unpublished_dir))
if not articles:
    print("No more articles to publish.")
    exit(0)

article_to_publish = articles[0]
src = os.path.join(unpublished_dir, article_to_publish)

# Read content
with open(src, "r", encoding="utf-8") as f:
    content = f.read()

# Replace date with today's real date
today_str = datetime.datetime.now().strftime("%Y-%m-%d")
display_date = datetime.datetime.now().strftime("%B %d, %Y")

import re
content = re.sub(r'date: ".*?"', f'date: "{display_date}"', content)

# Jekyll requires filename format YYYY-MM-DD-title.md
new_filename = f"{today_str}-anuradha-sharma-update.md"
dst = os.path.join(posts_dir, new_filename)

with open(dst, "w", encoding="utf-8") as f:
    f.write(content)

os.remove(src)
print(f"Published {article_to_publish} to {dst}")
