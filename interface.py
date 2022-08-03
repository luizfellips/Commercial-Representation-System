from tkinter import *
from tkinter import ttk
import pandas as pd


def find_especs_by_code(code,dataframe):
    especification = dataframe.loc[code,'ESPECIFICAÇÃO']
    return especification


def find_prices_by_code(code,dataframe):
        price = str(dataframe.loc[code,'PREÇO'])
        formatted_price = price.replace(',','.') 
        return float(formatted_price)

class MainApplication:
    def __init__(self, toplevel):
        self.list_of_products = []
        self.empty_sheet = pd.read_excel('_files/empty.xlsx')
        self.empty_df = pd.DataFrame(self.empty_sheet)
        
        config = ('Verdana', 15, 'bold')
        columns = ('qtd','cod','espec','pre')
        

        self.frame = Frame(toplevel).grid()
        self.frame2 = Frame(toplevel).grid()
        
        

        self.title = Label(self.frame, text='ESTRUTURADOR DE DADOS', font=config).grid()
        
        self.labelarchive = Label(self.frame,text='Nome da tabela a ser lida: ',font=('Verdana',10,'bold')).grid()
        self.archivename = Entry(self.frame)
        self.archivename.grid()
        
        self.carregar = Button(self.frame,text='CARREGAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.carregar.grid(pady=5)
        self.carregar.bind('<Button-1>',self.load_archive)

        
        self.firstlabel = Label(self.frame, text='QUANTIDADE',
                                font=('Verdana', 10, 'bold')).grid(column=0)
        self.firstentry = Entry(self.frame)
        self.firstentry.grid()
        




        self.secondlabel = Label(self.frame, text='CÓDIGO',
                                 font=('Verdana', 10, 'bold')).grid()
        self.secondentry = Entry(self.frame)
        self.secondentry.grid(pady=5)
        self.secondentry.bind('<Return>',self.insert_infos)

        
        self.tree = ttk.Treeview(self.frame2, columns=columns, show='headings')
        self.tree.heading('qtd',text='Quantidade')
        self.tree.heading('cod',text='Código')
        self.tree.heading('espec',text='Especificação')
        self.tree.heading('pre',text='Preço')
        self.tree.grid()
        
        self.thirdlabel = Label(self.frame2, text='NOME DO ARQUIVO PARA SALVAR',
                                font=('Verdana', 10, 'bold')).grid()
        self.thirdentry = Entry(self.frame)
        self.thirdentry.grid()
        
        self.savebutton = Button(self.frame,text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.savebutton.grid(pady=5)
        
    def load_archive(self,event):
        name = self.archivename.get()
        try:
            self.product_data = pd.read_excel(f'_files/{name}.xlsx')
            self.product_df = pd.DataFrame(self.product_data)
            self.product_df.set_index('CÓDIGO',inplace=True)
            self.carregar.config(text="CARREGADO COM SUCESSO",bg='green')
        except:
            self.carregar.config(text="ERRO AO CARREGAR, VERIFIQUE O NOME",bg="red")
    
    def insert_infos(self,event):
        qtd = self.firstentry.get()
        cod = self.secondentry.get().upper()
        especs = find_especs_by_code(cod,self.product_df)
        prices = find_prices_by_code(cod,self.product_df)
        tuple_of_product = (qtd,cod,especs,prices)
        self.list_of_products.append(tuple_of_product)
        self.tree.insert('',END,values=tuple_of_product)
        



root = Tk()
MainApplication(root)
root.geometry('800x600')
root.mainloop()