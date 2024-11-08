# scraper.py

import requests
from bs4 import BeautifulSoup
from db_handler import save_to_db  # Import the save_to_db function

def scrape_mdn_js_tutorials():
    url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    tutorials = []
    for section in soup.find_all("h2"):
        title = section.text
        link = url + "#" + title.replace(" ", "_")
        tutorials.append({"title": title, "link": link})

    return tutorials

# Usage example
if __name__ == "__main__":
    tutorials = scrape_mdn_js_tutorials()
    save_to_db(tutorials)  # Now this function is defined and will save to the database
