import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, 'html.parser')
links = [span.a for span in  soup.select(".titleline")]
subtext = soup.select(".subtext")

def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key= lambda x: x["votes"])

def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_vote(hn)

pprint.pprint(create_custom_hn(links, subtext))