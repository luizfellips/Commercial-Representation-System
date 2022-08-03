import pandas as pd

###funções
def find_especs_by_code(code,dataframe):
    especification = dataframe.loc[code,'ESPECIFICAÇÃO']
    return especification

def find_prices_by_code(code,dataframe):
    price = str(dataframe.loc[code,'PREÇO'])
    formatted_price = price.replace(',','.') 
    return float(formatted_price)

def gather_info(list):
    print('QUANTIDADES')
    for item in list:
        print(item[0])
    print('CÓDIGOS')
    for item in list:
        print(item[1])
        print('------------')
    print('ESPECIFICAÇÕES')
    for item in list:
        print(item[2])
    print('--------------')
    print('PREÇOS')
    for item in list:
        print(item[3])


def set_and_save_info(data,name):
    for count,tuples in enumerate(data):      
        empty_df.loc[count,'QUANTIDADE'] = tuples[0]
        empty_df.loc[count,'CÓDIGO'] = tuples[1]
        empty_df.loc[count,'ESPECIFICAÇÃO'] = tuples[2]
        empty_df.loc[count,'PREÇO'] = tuples[3]
    empty_df.set_index('QUANTIDADE',inplace=True)
        
    empty_df.to_excel(name,sheet_name='PEDIDO')

    
##loading dataframes
empty_sheet = pd.read_excel('_files/empty.xlsx')
empty_df = pd.DataFrame(empty_sheet)
product_data = pd.read_excel('_files/tabela mgo.xlsx')
product_df = pd.DataFrame(product_data)
product_df.set_index('CÓDIGO',inplace=True)


##mini programa
qtd = int(input('insira a qtd de itens: '))
data = []
for i in range(0,qtd):
    quantia = int(input('insira a quantia: '))
    code = str(input('Insira o código: ').strip().upper())
    espec = find_especs_by_code(code,product_df)
    price = find_prices_by_code(code,product_df)
    object = (quantia,code,espec,price)
    data.append(object)
gather_info(data)

            
set_and_save_info(data)
    


    