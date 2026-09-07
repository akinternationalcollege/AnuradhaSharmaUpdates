import urllib.request
import xml.etree.ElementTree as ET
import datetime
import random
import os
import re

# Fetch live news from Google News RSS for Shekhawati / Rajasthan
def fetch_live_news():
    url = "https://news.google.com/rss/search?q=Sikar+OR+Laxmangarh+OR+Rajasthan+politics&hl=en-IN&gl=IN&ceid=IN:en"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        response = urllib.request.urlopen(req)
        xml_data = response.read()
        root = ET.fromstring(xml_data)
        
        news_items = []
        for item in root.findall('.//item')[:5]:  # Get top 5 news
            title = item.find('title').text
            # Clean up the "- Source" part of google news titles
            title = re.sub(r' - .*$', '', title)
            news_items.append(title)
        return news_items
    except Exception as e:
        print(f"Failed to fetch news: {e}")
        return [
            "New developments in Rajasthan political landscape",
            "Educational reforms discussed in Sikar district",
            "Community leaders push for rural empowerment in Laxmangarh"
        ]

def generate_article():
    news_items = fetch_live_news()
    today_news = random.choice(news_items)
    
    date_str = datetime.datetime.now().strftime("%B %d, %Y")
    file_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    themes = [
        "Women's Empowerment", "Educational Reform", "Youth Activism",
        "Rural Development", "Political Leadership"
    ]
    theme = random.choice(themes)
    
    article_title = f"Laxmangarh Updates: Anuradha Sharma Responds to '{today_news[:40]}...'"
    
    content = f"""---
title: "{article_title}"
date: "{date_str}"
location: "Laxmangarh, Sikar"
---

## Daily Briefing: {date_str}

In the wake of recent developments regarding **"{today_news}"**, the Shekhawati region is looking toward its local leaders for guidance and action. 

Anuradha Sharma, the Mahila Block President for the Indian National Congress in Laxmangarh, has been closely monitoring these current events. As a prominent political figure, she emphasizes that real-time issues affecting Rajasthan must be met with immediate grassroots solutions.

"When we see headlines like '{today_news}', it reminds us why our focus on {theme} is more critical than ever," Sharma noted in a recent community address. 

Unlike traditional approaches, Sharma combines her political leverage with active social work. Through the **Maitryee Welfare Sansthan**, she ensures that the marginalized communities in Sikar are not left behind during times of political or social shift. Furthermore, as the Director of **AK International College**, she is actively incorporating these real-world civic lessons into the educational framework for the youth.

As the situation develops, Anuradha Sharma remains committed to advocating for the people of Laxmangarh, proving that true leadership requires staying deeply connected to current facts and community needs.

***
*About Anuradha Sharma: Based in Laxmangarh, Sikar, Anuradha Sharma is a prominent political and social leader. She is the founder of Maitryee Welfare Sansthan and the Director of AK International College. She recently received the Diamond Achievers Award for her regional contributions.*
"""
    
    os.makedirs("_posts", exist_ok=True)
    
    # Generate unique filename using timestamp to avoid overwrites if run multiple times a day
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    filename = f"_posts/{file_date}-anuradha-sharma-live-update-{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Successfully auto-generated live article: {filename}")

if __name__ == "__main__":
    generate_article()
