import pandas as pd


frame = pd.read_excel('_files\\tabela mgo.xlsx')
frame['PREÇO'] = frame['PREÇO'].apply(lambda x: x.replace(',','.').strip() if isinstance(x,str) else x)
frame = frame.astype({"PREÇO": float})
frame = frame.sort_values(by=['PREÇO'])
print(frame)