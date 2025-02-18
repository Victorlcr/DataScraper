import requests
from bs4 import BeautifulSoup

# Encoder de ASCII

url = "https://www.w3schools.com/tags/ref_urlencode.ASP"

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

table = soup.find('table', class_='ws-table-all notranslate')
tr = soup.find_all('tr')

th = table.find_all('th')
character = th[0].text
utf_8 = th[2].text

Encode = {}

for row in tr:
  td = row.find_all('td')
  if td:  # Checa se o td nao esta vazio
    char = td[0].text
    char = char.replace('space', ' ')
    char_set = td[2].text

    if not char.isalnum():
      Encode[char] = char_set

text = str(input('Preencha o campo para converter caracteres em codificação ASCII:'))
separed_text = list(text)

for char in separed_text:
  if char in Encode:
        decoded_text = {Encode[char]}
  else:
        decoded_text = {char}

  converted = map(str, decoded_text)
  formated_text = ''.join(converted)

  print(formated_text, end='')
