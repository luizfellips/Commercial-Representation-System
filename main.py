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
        
        config = ('Verdana', 15, 'bold')
        columns = ('qtd','cod','espec','pre')
        

        self.frame = Frame(toplevel).grid()
        self.frame2 = Frame(toplevel).grid()
        
        

        self.title = Label(self.frame, text='ESTRUTURADOR DE DADOS', font=config).grid()
        
        self.labelarchive = Label(self.frame,text='Nome da tabela a ser lida: ',font=('Verdana',10,'bold')).grid()
        self.archivename = Entry(self.frame)
        self.archivename.grid()
        self.archivename.bind('<Return>',self.load_archive)
        
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
        self.addproduct = Button(self.frame,text='adicionar',width=15,fg='black',bg='white',border=2,relief='groove')
        self.addproduct.grid(pady=5)
        self.addproduct.bind('<Button-1>',self.insert_infos)
        self.deleteproduct = Button(self.frame,text='deletar',width=15,fg='black',bg='white',border=2,relief='groove')
        self.deleteproduct.grid(pady=5)
        self.deleteproduct.bind('<Button-1>',self.delete_item)
        
        self.tree = ttk.Treeview(self.frame2, columns=columns, show='headings')
        self.tree.heading('qtd',text='Quantidade',anchor=CENTER)
        self.tree.heading('cod',text='Código',anchor=CENTER)
        self.tree.heading('espec',text='Especificação',anchor=CENTER)
        self.tree.heading('pre',text='Preço',anchor=CENTER)
        self.tree.column('cod',width=50)
        self.tree.column('qtd',width=50)
        self.tree.column('pre',width=50)
        self.tree.column('espec',width=400)
        self.tree.grid(padx=10)
        
        self.thirdlabel = Label(self.frame2, text='NOME DO ARQUIVO PARA SALVAR',
                                font=('Verdana', 10, 'bold')).grid()
        self.thirdentry = Entry(self.frame)
        self.thirdentry.grid()
        
        self.savebutton = Button(self.frame,text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.savebutton.grid(pady=5)
        self.savebutton.bind('<Button-1>',self.save_to_file)
        
    def load_archive(self,event):
        name = self.archivename.get()
        try:
            self.product_data = pd.read_excel(f'_files/{name}')
            self.product_df = pd.DataFrame(self.product_data)
            self.product_df.set_index('CÓDIGO',inplace=True)
            self.carregar.config(text="CARREGADO COM SUCESSO",bg='green',fg='white',width=40,relief='groove')
            self.carregar.after(1500,lambda:self.carregar.config(text="CARREGAR",width=15,fg='black',bg='white',border=2,relief='groove'))
        except:
            self.carregar.config(text="ERRO AO CARREGAR, VERIFIQUE O NOME",bg="red",fg='white',width=50,relief='groove')
            self.carregar.after(1500,lambda:self.carregar.config(text="CARREGAR",width=15,fg='black',bg='white',border=2,relief='groove'))

    
    def insert_infos(self,event):
        def reset_button():
            self.addproduct.config(text='adicionar',width=15,fg='black',bg='white',border=2,relief='groove')
        try:
            qtd = self.firstentry.get()
            cod = self.secondentry.get().upper().strip()
            if cod.isnumeric():    
                especs = find_especs_by_code(int(cod),self.product_df)
                prices = find_prices_by_code(int(cod),self.product_df)
            else:
                especs = find_especs_by_code(cod,self.product_df)
                prices = find_prices_by_code(cod,self.product_df)
            tuple_of_product = (qtd,cod,especs,prices)
            self.list_of_products.append(tuple_of_product)
            self.tree.insert('',END,values=tuple_of_product)
            self.addproduct.config(text='SUCESSO',fg='white',bg='green')
            self.addproduct.after(1000,reset_button)
            self.firstentry.delete(0, END)
            self.secondentry.delete(0, END)
            self.firstentry.focus_force()
        except:
            self.addproduct.config(text="INFORMAÇÕES INVÁLIDAS",fg='white',bg='red',width=30)
            self.addproduct.after(1000,reset_button)

        
        
    def delete_item(self,event):
        selected_items = self.tree.selection()
        for selected_item in selected_items:          
            for i in range(0,len(self.list_of_products)):
                for item in self.list_of_products:
                    if item[1] == self.tree.item(selected_item)['values'][1]:
                        self.list_of_products.remove(item)  
                        break      
            self.tree.delete(selected_item)       
            
            
    
    def save_to_file(self,event):
        name = self.thirdentry.get()
        try:
            empty_df = pd.DataFrame(columns=['QUANTIDADE','CÓDIGO','ESPECIFICAÇÃO','PREÇO'])
            print(self.list_of_products)
            for count,tuples in enumerate(self.list_of_products):      
                empty_df.loc[count,'QUANTIDADE'] = tuples[0]
                empty_df.loc[count,'CÓDIGO'] = tuples[1]
                empty_df.loc[count,'ESPECIFICAÇÃO'] = tuples[2]
                empty_df.loc[count,'PREÇO'] = tuples[3]
            if name.endswith('.xlsx'):
                empty_df.set_index('QUANTIDADE',inplace=True)    
                empty_df.to_excel(f'C:\\Users\\fellip\\Desktop\\excelproject\\saved_files\\{name}',sheet_name='PEDIDO')
                self.savebutton.config(text='SALVO COM SUCESSO',fg='white',bg='green',border=3,width=25,relief='groove')
                self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove'))
            else:
                self.savebutton.config(text='ERRO  AO SALVAR, VERIFIQUE AS INFORMAÇÕES',fg='white',bg='red',border=2,width=50)
            self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove'))
        except:    
            self.savebutton.config(text='ERRO TÉCNICO AO SALVAR',fg='white',bg='red',border=2,width=30)
            self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove'))
            



root = Tk()
MainApplication(root)
root.geometry('575x600')
root.mainloop()