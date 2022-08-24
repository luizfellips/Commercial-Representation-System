import pandas as pd


frame = pd.read_excel('_files\\tabela krater.xlsx')
frame.set_index('CÓDIGO', inplace=True)
object = frame.loc['203.552k003','ESPECIFICAÇÃO']
print(object)