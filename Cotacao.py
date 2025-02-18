import pandas as pd

sheet = pd.read_csv('https://raw.githubusercontent.com/fmassaretto/Workshop-WebScraping/main/arquivos/TabelaA%C3%A7%C3%B5es.csv')
formated = sheet.dropna(how='any')

filtered = formated[
    (formated['Val. Min'] > 20) &
    (formated['Val. Max'] < 50) &
    (formated['Var. Ano (%)'] > 0)
]

print(filtered)
