from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import json

def generate_json_from_url(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find('table')
    table_rows = table.find_all('tr')

    data = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text)
        data.append(row_data)

    df = pd.DataFrame(data)
    df = df.drop(2, axis=1)

    # Convertir el DataFrame a un diccionario
    result = {}

    for index, row in df.iterrows():
        key = row[0]
        value = row[1]
        
        if key in result:
            # Si la clave ya existe en el resultado, agrega el valor a la lista
            if not isinstance(result[key], list):
                result[key] = [result[key]]
            result[key].append(value)
        else:
            result[key] = value

    # Convertir el resultado a JSON sin espacios en blanco ni indentaciones
    json_output = json.dumps(result, separators=(',', ':'), ensure_ascii=False)
    return json_output

def generate_json_list_from_file(file_path, num_urls):
    json_list = []
    with open(file_path, 'r') as file:
        for i in range(num_urls):
            line = file.readline().strip()
            if not line:
                break
            json_data = generate_json_from_url(line)
            json_list.append(json_data)
    return json_list

def save_json_list_to_file(json_list, file_path):
    with open(file_path, 'w') as file:
        file.write('[' + ','.join(json_list) + ']')

file_path = "thesis-links.txt"  # Nombre del archivo que contiene las URLs
num_urls_to_read = 100  # Cantidad de URL a leer del archivo

json_list = generate_json_list_from_file(file_path, num_urls_to_read)
save_json_list_to_file(json_list, 'documents-trial.json')
