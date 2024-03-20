import requests
import re
import json

def get_latest_stories():
    url = "https://time.com"
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        title_pattern = r'<h3 class="featured-voices__list-item-headline display-block">(.*?)</h3>'
        url_pattern = r'<a href="(.*?)">'

        titles = re.findall(title_pattern, html_content)
        urls = re.findall(url_pattern, html_content)

        stories = []
        for title, url in zip(titles, urls):
            stories.append({'title': title.strip(), 'url': url})

        return json.dumps(stories, indent=4)
    else:
        print("Error: Unable to fetch data from Time.com")
        return json.dumps({"error": "Failed to retrieve stories"})


def get_time_stories():
    latest_stories = get_latest_stories()
    return latest_stories

print(get_time_stories())



