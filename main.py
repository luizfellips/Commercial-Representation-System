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
        secondcolumns = ('cod','espec','pre')
        

        self.frame = Frame(toplevel).grid()
        self.frame2 = Frame(toplevel).grid()
        
        

        self.title = Label(self.frame, text='ESTRUTURADOR DE DADOS', font=config).grid(row=0)
        
        self.labelarchive = Label(self.frame,text='Nome da tabela a ser lida: ',font=('Verdana',10,'bold')).grid(row=1,sticky=N)
        self.archivename = Entry(self.frame)
        self.archivename.grid(pady=25,row=1,sticky=N)
        self.archivename.bind('<Return>',self.load_archive)
        
        self.carregar = Button(self.frame,text='CARREGAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.carregar.grid(pady=50,row=1,sticky=N)
        self.carregar.bind('<Button-1>',self.load_archive)
        
        self.tituloespec = Label(self.frame,text='PROCURAR ESPECIFICAÇÃO',font=('Verdana',10,'bold')).grid(pady=75,row=1,sticky=N)
        self.especification = Entry(self.frame)
        self.especification.grid(pady=100,row=1,sticky=N)
        self.procurar = Button(self.frame,text='PROCURAR/RESETAR',width=19,fg='black',bg='white',border=2,relief='groove')
        self.procurar.grid(pady=125,row=1,sticky=N)
        self.procurar.bind('<Button-1>',self.search_for_infos)
        self.qtdlabel = Label(self.frame, text='QUANTIDADE',
                                font=('Verdana', 10, 'bold')).grid(row=1,sticky=S,pady=100)
        self.quantiaentry = Entry(self.frame)
        self.quantiaentry.grid(row=1,sticky=S,pady=82)
        self.addproductone = Button(self.frame,text='ADICIONAR',width=19,fg='black',bg='white',border=2,relief='groove')
        self.addproductone.grid(row=1,sticky=S,pady=50)
        self.addproductone.bind('<Button-1>',self.pull_infos)

        
        
        
        
        self.firstlabel = Label(self.frame, text='QUANTIDADE',
                                font=('Verdana', 10, 'bold')).grid(row=2,sticky=N)
        self.firstentry = Entry(self.frame)
        self.firstentry.grid(row=2,sticky=N,pady=25)


        self.secondlabel = Label(self.frame, text='CÓDIGO',
                                 font=('Verdana', 10, 'bold')).grid(row=2,sticky=N,pady=50)
        self.secondentry = Entry(self.frame)
        self.secondentry.grid(row=2,sticky=N,pady=75)
        self.secondentry.bind('<Return>',self.insert_infos)
        self.addproduct = Button(self.frame,text='ADICIONAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.addproduct.bind('<Button-1>',self.insert_infos)
        self.addproduct.grid(row=2,sticky=N,pady=100)
        self.deleteproduct = Button(self.frame,text='DELETAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.deleteproduct.bind('<Button-1>',self.delete_item)
        self.deleteproduct.grid(row=2,sticky=N,pady=125)
        
        
        self.secondtreetitle = Label(self.frame2,text='PRODUTOS',font=config).grid(row=0,column=1,sticky=N)
        self.secondtree = ttk.Treeview(self.frame2, columns=secondcolumns, show='headings')
        self.secondtree.heading('cod',text='Código',anchor=CENTER)
        self.secondtree.heading('espec',text='Especificação',anchor=CENTER)
        self.secondtree.heading('pre',text='Preço',anchor=CENTER)
        self.secondtree.column('cod',width=50)
        self.secondtree.column('pre',width=50)
        self.secondtree.column('espec',width=400)
        self.secondtree.grid(pady=15,padx=15,row=1,column=1,sticky=N)
        
        self.treetitle = Label(self.frame2,text='SUA CONSULTA',font=config).grid(row=1,column=1,sticky=S)
        self.tree = ttk.Treeview(self.frame2, columns=columns, show='headings')
        self.tree.heading('qtd',text='Quantidade',anchor=CENTER)
        self.tree.heading('cod',text='Código',anchor=CENTER)
        self.tree.heading('espec',text='Especificação',anchor=CENTER)
        self.tree.heading('pre',text='Preço',anchor=CENTER)
        self.tree.column('cod',width=50)
        self.tree.column('qtd',width=50)
        self.tree.column('pre',width=50)
        self.tree.column('espec',width=400)
        self.tree.grid(padx=15,row=2,column=1,sticky=N)
        
        self.thirdlabel = Label(self.frame, text='NOME DO ARQUIVO PARA SALVAR',
                                font=('Verdana', 10, 'bold')).grid(pady=180,row=2,sticky=N)
        self.thirdentry = Entry(self.frame)
        self.thirdentry.grid(pady=200,row=2,sticky=N)

        
        self.savebutton = Button(self.frame,text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove')
        self.savebutton.grid(pady=225,row=2,sticky=N)
        self.savebutton.bind('<Button-1>',self.save_to_file)
        
        
    
    
    def load_archive(self,event):
        name = self.archivename.get()
        try:
            self.secondtree.delete(*self.secondtree.get_children())
            self.product_data = pd.read_excel(f'_files/{name}')
            self.product_df = pd.DataFrame(self.product_data)
            self.carregar.config(text="CARREGADO COM SUCESSO",bg='green',fg='white',width=40,relief='groove')
            self.carregar.after(1500,lambda:self.carregar.config(text="CARREGAR",width=15,fg='black',bg='white',border=2,relief='groove'))
            cods = self.product_df['CÓDIGO'].tolist()
            especs = self.product_df['ESPECIFICAÇÃO'].tolist()
            prices = self.product_df['PREÇO'].tolist()
            for i in range(0,len(self.product_df)):
                entire_list = (cods[i],especs[i],prices[i])
                self.secondtree.insert('',END,values=entire_list)

            
        except:
            self.carregar.config(text="ERRO AO CARREGAR, VERIFIQUE O NOME",bg="red",fg='white',width=40,relief='groove')
            self.carregar.after(1500,lambda:self.carregar.config(text="CARREGAR",width=15,fg='black',bg='white',border=2,relief='groove'))

    
    def search_for_infos(self,event):
        try:
            espec = self.especification.get()
            self.secondtree.delete(*self.secondtree.get_children())
            dataoccurrences = self.product_df[self.product_df['ESPECIFICAÇÃO'].str.contains(espec,case=False) == True]
            cods = dataoccurrences['CÓDIGO'].tolist()
            especs = dataoccurrences['ESPECIFICAÇÃO'].tolist()
            prices = dataoccurrences['PREÇO'].tolist()
            for i in range(0,len(dataoccurrences)):
                entire_list = (cods[i],especs[i],prices[i])
                self.secondtree.insert('',END,values=entire_list)
            self.procurar.config(text='SUCESSO',bg='green',fg='white')
            self.addproductone.after(1500,lambda: self.procurar.config(text='PROCURAR/RESETAR',width=19,fg='black',bg='white',border=2,relief='groove'))
        except:
            self.procurar.config(text='UM ERRO OCORREU',bg='red',fg='white')
            self.procurar.after(1500,lambda: self.procurar.config(text='PROCURAR/RESETAR',width=19,fg='black',bg='white',border=2,relief='groove'))
            
        
    def pull_infos(self,event):
        qtd = self.quantiaentry.get()
        if qtd.isnumeric():
            try:
                selected_items = self.secondtree.selection()
                for selected_item in selected_items:
                    cod = self.secondtree.item(selected_item)['values'][0]
                    espec = self.secondtree.item(selected_item)['values'][1]
                    price = self.secondtree.item(selected_item)['values'][2]
                    tuple_of_products = (qtd,cod,espec,price)
                    self.list_of_products.append(tuple_of_products)
                    self.tree.insert('',END,values=tuple_of_products)
                self.addproductone.config(text='SUCESSO',bg='green',fg='white')
                self.addproductone.after(1500,lambda: self.addproductone.config(text='ADICIONAR',width=19,fg='black',bg='white',border=2,relief='groove'))
            except:
                self.addproductone.config(text='UM ERRO OCORREU',bg='red',fg='white')
                self.addproductone.after(1500,lambda: self.addproductone.config(text='ADICIONAR',width=19,fg='black',bg='white',border=2,relief='groove'))
        else:
            self.addproductone.config(text='UM ERRO OCORREU',bg='red',fg='white')
            self.addproductone.after(1500,lambda: self.addproductone.config(text='ADICIONAR',width=19,fg='black',bg='white',border=2,relief='groove'))
    
        
        
        
    def insert_infos(self,event):
        def reset_button():
            self.addproduct.config(text='adicionar',width=15,fg='black',bg='white',border=2,relief='groove')
        try:
            self.product_df.set_index('CÓDIGO',inplace=True)
        except:
            self.addproduct.config(text="UM ERRO OCORREU",fg='white',bg='red',width=30)
            self.addproduct.after(1000,reset_button)
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
            self.product_df.reset_index(inplace=True)
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
            for count,tuples in enumerate(self.list_of_products):      
                empty_df.loc[count,'QUANTIDADE'] = tuples[0]
                empty_df.loc[count,'CÓDIGO'] = tuples[1]
                empty_df.loc[count,'ESPECIFICAÇÃO'] = tuples[2]
                empty_df.loc[count,'PREÇO'] = tuples[3]
            if name.endswith('.xlsx'):
                empty_df.set_index('QUANTIDADE',inplace=True)    
                empty_df.to_excel(f'saved_files\\{name}',sheet_name='PEDIDO')
                self.savebutton.config(text='SALVO COM SUCESSO',fg='white',bg='green',border=3,width=25,relief='groove')
                self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove'))
            else:
                self.savebutton.config(text='ERRO  AO SALVAR, VERIFIQUE AS INFORMAÇÕES',fg='white',bg='red',border=2,width=40)
            self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove'))
        except:    
            self.savebutton.config(text='ERRO TÉCNICO AO SALVAR',fg='white',bg='red',border=2,width=30)
            self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15,fg='black',bg='white',border=2,relief='groove'))
            



root = Tk()
MainApplication(root)
root.geometry('950x580')
root.mainloop()