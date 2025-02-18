from re import T
import requests
import datetime as dt
from bs4 import BeautifulSoup

EVENTS = {}

for i in range(1,10):
  if (i == 1):
    URL = "https://cultura.jundiai.sp.gov.br/agenda-cultural/"
  else:
    URL = f"https://cultura.jundiai.sp.gov.br/agenda-cultural/page/{1}/"

  page_request = requests.get(URL)
  soup = BeautifulSoup(page_request.content, 'html.parser')

  events_list = soup.find_all('div', class_='noticia-lista')

for event in events_list:
  title = event.find('div', class_='titulo-lista').text
  date = event.find('span', class_='data-lista').text
  place = event.find('div', class_='resumo-lista').text

  link = event.find('a')['href']
  inter_page = requests.get(link)
  intern_soup = BeautifulSoup(inter_page.content, 'html.parser')

  event_info = intern_soup.find_all('p')

  EVENTS[title] = {
      'Date': date,
      'Place': place,
      'Info': event_info
  }

  print(EVENTS)
