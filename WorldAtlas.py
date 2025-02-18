from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import pandas as pd

URL = 'https://www.worldatlas.com/articles/which-are-the-world-s-largest-technology-companies.html'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#table = soup.find('table')
table = soup.table
tbody = table.tbody
rows = tbody.find_all('tr')

companies = []
reveneus = []

for row in rows:
  companies.append(row.findAll('td')[1].text)
  reveneus.append(float(row.findAll('td')[2].text.strip('$')))

data = {'Companhia': companies, 'Faturamento': reveneus}
df = pd.DataFrame(data)

plt.bar(df['Companhia'], df['Faturamento'])
plt.xlabel('Empresa')
plt.ylabel('Faturamento')
plt.xticks(rotation='vertical')

plt.show()
