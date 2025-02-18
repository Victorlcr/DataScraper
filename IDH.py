import matplotlib.pyplot as plt  #pip install matplotlib
import pandas as pd

#tinyurl.com/dados-idh
idh_data = pd.read_csv('https://raw.githubusercontent.com/fmassaretto/Workshop-WebScraping/main/arquivos/IDH.csv')

idh_location = idh_data['Territorialidade']
idh_income = idh_data['IDHM Renda']
idh_education = idh_data['IDHM Educação']
idh_longevity = idh_data['IDHM Longevidade']

plt.bar(idh_location, idh_longevity, label='IDHM Longevidade')
plt.bar(idh_location, idh_income, label='IDHM Renda')
plt.bar(idh_location, idh_education, label='IDHM Educação')

plt.xticks(rotation='vertical')

plt.legend(loc='center left')

plt.show()
