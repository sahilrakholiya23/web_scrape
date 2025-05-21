import requests 
from  bs4 import BeautifulSoup


def fatch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f" Error data not found {url} :{e}")
        return None
    
def parse_page(content):
    soup =BeautifulSoup(content, 'html.parser')
    results = []

    for a_tag in soup.find_all('a' , href=True):
        title= a_tag.get_text().strip()
        link = a_tag['href']
        results.append((title,link))

    return results


def scrape_website(url):
    print(f"Strating Scrape for : {url}")
    page_content = fatch_page(url)

    if not page_content:
        print(f" data not found in this {url}")
        return

    parsed_data =  parse_page(page_content)
    print(f"Scriping Complete for {url}. Found {len(parsed_data)} links")
    for title, link in parsed_data:
        print(f"Title:{title} , Link: {link}")
        print("\n")


if __name__ =="__main__":
   url = input("Enter website URL:")
   scrape_website(url)
