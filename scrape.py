from bs4 import BeautifulSoup
import requests

def scrape():
    urls = ['https://espn.com/fantasy/football', 'https://bleacherreport.com/fantasy-football',
        'https://cbssports.com/fantasy/football', 'https://www.fantasypros.com/nfl/player-news.php']
    newsArr = []
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        if url == 'https://espn.com/fantasy/football':
            all_news = soup.find_all("a", class_="realStory")
            for news in all_news:
                newsObject = {
                    "headline": news.text,
                    "link": url + news.get('href'),
                    "source": "ESPN"
                }
                newsArr.append(newsObject)
        elif url == 'https://bleacherreport.com/fantasy-football':
            all_news = soup.find_all('a', class_="articleTitle")
            for news in all_news:
                newsObject = {
                    "headline": news.text,
                    "link": news.get('href'),
                    "source": "Bleacher Report"
                }
                newsArr.append(newsObject)
        elif url == 'https://cbssports.com/fantasy/football':
            all_news = soup.find_all("div", class_="latest-content")
            for news in all_news:
                urlArr = url.split("/fantasy")
                newsObject = {
                    "headline": news.text,
                    "link": urlArr[0] + news.find('a').get('href'),
                    "source": "CBS Sports"
                }
                newsArr.append(newsObject)
        elif url == 'https://www.fantasypros.com/nfl/player-news.php':
            all_news = soup.find_all("div", class_="player-news-header")
            for news in all_news:
                headline = news.find('a')
                urlArr = url.split("/nfl")
                newsObject = {
                    "headline": headline.text,
                    "link": urlArr[0] + headline.get('href'),
                    "source": "Fantasy Pros"
                }
                newsArr.append(newsObject)
    return newsArr

if __name__ == "__main__":
    scrape()   