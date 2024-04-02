from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

links = []

#for link in links:
#    print('https://repositorio.usm.cl' + str(link) + '?show=full')

for i in range(1,76):
    url = "https://repositorio.usm.cl/handle/11673/21679/discover?rpp=100&etal=0&group_by=none&page=" + str(i)
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    results_mother = soup.find('div', {"id": "aspect_discovery_SimpleSearch_div_search-results"})
    results = results_mother.find_all('a')

    for result in results:
        if result['href'] not in links:
            links.append(result['href'])

with open('thesis-links.txt', 'w') as f:
    for link in links:
        f.write(f"{'https://repositorio.usm.cl' + str(link) + '?show=full'}\n")

print(len(links))