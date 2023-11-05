import requests
from bs4 import BeautifulSoup
import random


user_agents = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"]

def retrieve_articles(search_query):


    base_url = 'https://scholar.google.com/scholar'
    params = {
        'as_q': search_query,
    }

    agent_idx = random.randint(0, len(user_agents) - 1)    
    response = requests.get(base_url, params=params, headers = {'User-Agent':user_agents[agent_idx]})
    res = list()
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles_el = soup.select('h3', class_='gs_rt')

        for title_el in titles_el:
            a_tag = title_el.find('a')
            title = a_tag.get_text()
            link = a_tag.get('href')
            res.append({title:link})
    else:
        return f"Failed to retrieve the webpage: Status code {response.status_code}"
    
    return res


if __name__ == "__main__":
    retrieve_articles("climate change")
