import requests
from bs4 import BeautifulSoup
import json

def get_latest_stories():
    url = "https://time.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        featured_voices_list = soup.find('ul', class_='featured-voices__list')
        h3_texts = [h3.get_text(strip=True) for h3 in featured_voices_list.find_all('h3')]
        first_anchor_links = [li.a['href'] for li in featured_voices_list.find_all('li')]

        stories = []
        for title, url in zip(h3_texts, first_anchor_links):
            stories.append({'title': title, 'url': url})

        return json.dumps(stories, indent=4)
    else:
        print("Error: Unable to fetch data from Time.com")
        return json.dumps({"error": "Failed to retrieve stories"})


def get_time_stories():
    latest_stories = get_latest_stories()
    return latest_stories
print(get_time_stories())


