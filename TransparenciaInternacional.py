import requests
from bs4 import BeautifulSoup #pip install BeautifulSoup

url = 'https://transparenciainternacional.org.br/ipc'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', id='table_1')
tbody = table.find('tbody')
tr = tbody.find_all('tr')

ICP = {}

for row in tr:
  td = row.find_all('td')
  posicao = td[5].text
  pais = td[2].text
  pts = td[1].text

  ICP = {
      'País': pais,
      'Posição': posicao,
      'Pontos': pts
  }

  print(ICP)
