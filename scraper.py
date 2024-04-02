import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen

def extract_data(url, indent=0):
    data = []
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    ul_elements = soup.find_all('ul', class_='ds-artifact-list list-unstyled')

    for ul in ul_elements:
        li_elements = ul.find_all('li', class_='ds-artifact-item odd')

        for li in li_elements:
            div_element = li.find('div', class_='artifact-description')
            a_element = div_element.find('a')
            
            href = a_element.get('href')
            text = a_element.text.strip()

            print("  " * indent + text)  # Print with appropriate indentation
            data.append([href, text])
            data += extract_data('https://repositorio.usm.cl' + href, indent + 1)  # Recursively call extract_data for each href link

    return data

if __name__ == "__main__":
    url = "https://repositorio.usm.cl/handle/11673/21679"
    result = extract_data(url)
