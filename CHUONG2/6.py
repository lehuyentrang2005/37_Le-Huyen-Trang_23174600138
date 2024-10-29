import requests
import xml.dom.minidom
import csv

def download_rss(url):
    response = requests.get(url)
    with open('rss_feed.xml', 'wb') as file:
        file.write(response.content)
    print("RSS feed downloaded and saved as rss_feed.xml.")

def parse_rss_to_dict(xml_file):
    doc = xml.dom.minidom.parse(xml_file)
    items = doc.getElementsByTagName("item")
    news_list = []
    
    for item in items:
        news_dict = {
            "title": item.getElementsByTagName("title")[0].firstChild.nodeValue,
            "link": item.getElementsByTagName("link")[0].firstChild.nodeValue,
            "description": item.getElementsByTagName("description")[0].firstChild.nodeValue,
            "pubDate": item.getElementsByTagName("pubDate")[0].firstChild.nodeValue,
        }
        news_list.append(news_dict)
    
    return news_list

def save_to_csv(news_list, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=news_list[0].keys())
        writer.writeheader()
        writer.writerows(news_list)
    print(f"News items saved to {filename}.")

def main():
    url = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"
    download_rss(url)
    news_list = parse_rss_to_dict('rss_feed.xml')
    save_to_csv(news_list, 'news_items.csv')

if __name__ == "__main__":
    main()
