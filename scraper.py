import requests
from bs4 import BeautifulSoup
from db_handler import save_to_db

# Scrape MDN JavaScript tutorials
def scrape_mdn_js_tutorials():
    url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tutorials = []
    
    for section in soup.find_all("h2"):
        title = section.text.strip()
        link = url + "#" + title.replace(" ", "_")
        tutorials.append({"title": title, "link": link, "platform": "MDN"})
    
    return tutorials

# Scrape Codecademy Python courses
def scrape_codecademy_python_courses():
    url = "https://www.codecademy.com/catalog/language/python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    courses = []
    
    for course in soup.find_all("a", class_="course-card"):
        title = course.text.strip()
        link = "https://www.codecademy.com" + course.get("href")
        courses.append({"title": title, "link": link, "platform": "Codecademy"})
    
    return courses

# Scrape Udemy Python courses
def scrape_udemy_python_courses():
    url = "https://www.udemy.com/courses/search/?q=python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    courses = []
    
    for course in soup.find_all("div", class_="course-card"):
        title = course.find("div", class_="course-title").text.strip()
        link = "https://www.udemy.com" + course.find("a")["href"]
        courses.append({"title": title, "link": link, "platform": "Udemy"})
    
    return courses

# Scrape Coursera Python courses
def scrape_coursera_python_courses():
    url = "https://www.coursera.org/courses?query=python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    courses = []
    
    for course in soup.find_all("li", class_="ais-InfiniteHits-item"):
        title = course.find("h2").text.strip()
        link = "https://www.coursera.org" + course.find("a")["href"]
        courses.append({"title": title, "link": link, "platform": "Coursera"})
    
    return courses

# Scrape freeCodeCamp Python tutorials
def scrape_freecodecamp_python_courses():
    url = "https://www.freecodecamp.org/news/tag/python/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    
    for article in soup.find_all("h2"):
        title = article.text.strip()
        link_tag = article.find("a")
        
        # Check if the anchor tag exists before accessing its 'href'
        if link_tag:
            link = link_tag["href"]
            # If the link is relative, prepend the base URL
            if not link.startswith("http"):
                link = "https://www.freecodecamp.org" + link
            articles.append({"title": title, "link": link, "platform": "freeCodeCamp"})
    
    return articles


# Scrape edX Python courses
def scrape_edx_python_courses():
    url = "https://www.edx.org/learn/python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    courses = []
    
    for course in soup.find_all("div", class_="card"):
        title = course.find("h3").text.strip()
        link = "https://www.edx.org" + course.find("a")["href"]
        courses.append({"title": title, "link": link, "platform": "edX"})
    
    return courses

# Scrape all tutorials from all platforms
def scrape_all_tutorials():
    tutorials = []
    tutorials += scrape_mdn_js_tutorials()
    tutorials += scrape_codecademy_python_courses()
    tutorials += scrape_udemy_python_courses()
    tutorials += scrape_coursera_python_courses()
    tutorials += scrape_freecodecamp_python_courses()
    tutorials += scrape_edx_python_courses()
    
    # Save all tutorials to the database
    save_to_db(tutorials)

# Usage
if __name__ == "__main__":
    scrape_all_tutorials()
