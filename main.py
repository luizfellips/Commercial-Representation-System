from tkinter import *
from tkinter import ttk
import pandas as pd

def find_especs_by_code(code,dataframe):
    especification = dataframe.loc[code,'ESPECIFICAÇÃO']
    return especification


def find_prices_by_code(code,dataframe):
    price = str(dataframe.loc[code,'PREÇO']).strip()
    formatted_price = price.replace(',','.') 
    final_price = formatted_price.removeprefix('R$').strip()
    return float(final_price)

class MainApplication:
    def __init__(self, toplevel):
        self.list_of_products = []
        self.sum_of_products = 0
        
        root.title('ANALYSIS SYSTEM')
        pic = PhotoImage(file = 'icon.png')
        root.iconphoto(False,pic)
        root.call("source",'themes\\azure.tcl')
        root.call('set_theme','dark')
    
        

        root.geometry('1250x660')
        
            
        
        
        config = ('Verdana', 15, 'bold')
        columns = ('qtd','cod','espec','pre','tot')
        secondcolumns = ('cod','espec','pre')
        

        self.frame = Frame(toplevel).grid()
        self.frame2 = Frame(toplevel).grid()
        self.alphabetic_variable = IntVar()
        self.alphabetic_checkbox = ttk.Checkbutton(self.frame,text='ORDEM ALFABÉTICA',
                                                   variable=self.alphabetic_variable,onvalue=1,offvalue=0,
                                                   command=self.set_alphabetic)
        self.alphabetic_checkbox.place(x=960,y=43)
        
        self.ascending_variable = IntVar()
        self.ascending_checkbox = ttk.Checkbutton(self.frame,text='PREÇO CRESCENTE',
                                                   variable=self.ascending_variable,onvalue=1,offvalue=0,
                                                   command=self.set_ascending)
        
        self.ascending_checkbox.place(x=960,y=83)
        
        self.descending_variable = IntVar()
        self.descending_checkbox = ttk.Checkbutton(self.frame,text='PREÇO DECRESCENTE',
                                                   variable=self.descending_variable,onvalue=1,offvalue=0,
                                                   command=self.set_descending)
        
        self.descending_checkbox.place(x=960,y=123)
        


        self.title = ttk.Label(self.frame, text='ESTRUTURADOR DE DADOS', font=config).grid(row=0)
        
        self.labelarchive = ttk.Label(self.frame,text='Nome da tabela a ser lida: ',font=('Verdana',10,'bold')).grid(row=1,sticky=N)
        self.archivename = ttk.Entry(self.frame)
        self.archivename.place(x=65,y=53)
        self.archivename.bind('<Return>',self.load_archive)
        
        self.carregar = ttk.Button(self.frame,text='CARREGAR',width=15)
        self.carregar.place(x=230,y=53)
        self.carregar.bind('<Button-1>',self.load_archive)
        
        self.tituloespec = ttk.Label(self.frame,text='PROCURAR ESPECIFICAÇÃO',font=('Verdana',10,'bold')).place(x=65,y=100)
        self.especification = ttk.Entry(self.frame)
        self.especification.bind('<Return>',self.search_for_infos)
        self.especification.place(x=65,y=120)
        self.procurar = ttk.Button(self.frame,text='PROCURAR/RESET',width=16)
        self.procurar.place(x=230,y=120)
        self.procurar.bind('<Button-1>',self.search_for_infos)
        self.qtdlabel = ttk.Label(self.frame, text='QUANTIDADE',
                                font=('Verdana', 10, 'bold')).place(x=65,y=160)
        self.quantiaentry = ttk.Entry(self.frame)
        self.quantiaentry.bind('<Return>',self.pull_infos)
        self.quantiaentry.place(x=65,y=180)
        self.addproductone = ttk.Button(self.frame,text='ADICIONAR',width=19)
        self.addproductone.place(x=230,y=180)
        self.addproductone.bind('<Button-1>',self.pull_infos)

        
        
        
        
        self.firstlabel = ttk.Label(self.frame, text='QUANTIDADE',
                                font=('Verdana', 10, 'bold')).place(x=90,y=310)
        self.firstentry = ttk.Entry(self.frame)
        self.firstentry.place(x=90,y=330)


        self.secondlabel = ttk.Label(self.frame, text='CÓDIGO',
                                 font=('Verdana', 10, 'bold')).place(x=90,y=370)
        self.secondentry = ttk.Entry(self.frame)
        self.secondentry.place(x=90,y=390)
        self.secondentry.bind('<Return>',self.insert_infos)
        self.addproduct = ttk.Button(self.frame,text='ADICIONAR',width=15)
        self.addproduct.bind('<Button-1>',self.insert_infos)
        self.addproduct.place(x=90,y=430)
        self.deleteproduct = ttk.Button(self.frame,text='DELETAR',width=15)
        self.deleteproduct.bind('<Button-1>',self.delete_item)
        self.deleteproduct.place(x=90,y=470)
        
        
        self.secondtreetitle = ttk.Label(self.frame2,text='PRODUTOS',font=config).place(x=610,y=8)
        self.secondtree = ttk.Treeview(self.frame2, columns=secondcolumns, show='headings')
        self.secondtree.heading('cod',text='Código',anchor=CENTER)
        self.secondtree.heading('espec',text='Especificação',anchor=CENTER)
        self.secondtree.heading('pre',text='Preço',anchor=CENTER)
        self.secondtree.column('cod',width=50)
        self.secondtree.column('pre',width=50)
        self.secondtree.column('espec',width=400)
        self.secondtree.grid(pady=15,padx=15,row=1,column=1,sticky=N)
        
        self.treetitle = ttk.Label(self.frame2,text='SUA CONSULTA',font=config).place(x=584,y=303)
        self.tree = ttk.Treeview(self.frame2, columns=columns, show='headings')
        self.tree.heading('qtd',text='Quantidade',anchor=CENTER)
        self.tree.heading('cod',text='Código',anchor=CENTER)
        self.tree.heading('espec',text='Especificação',anchor=CENTER)
        self.tree.heading('pre',text='Preço',anchor=CENTER)
        self.tree.heading('tot',text='Total',anchor=CENTER)
        self.tree.column('cod',width=50)
        self.tree.column('qtd',width=50)
        self.tree.column('pre',width=50)
        self.tree.column('espec',width=400)
        self.tree.column('tot',width=90)
        self.tree.grid(padx=15,row=2,column=1,sticky=N)
        
        self.thirdlabel = ttk.Label(self.frame, text='NOME DO ARQUIVO PARA SALVAR',
                                font=('Verdana', 10, 'bold')).grid(pady=180,row=2,sticky=N)
        self.thirdentry = ttk.Entry(self.frame)
        self.thirdentry.grid(pady=200,row=2,sticky=N)

        
        self.savebutton = ttk.Button(self.frame,text='SALVAR',width=15)
        self.savebutton.place(x=90,y=585)
        self.savebutton.bind('<Button-1>',self.save_to_file)
        
        self.totaltitle = ttk.Label(self.frame,text='TOTAL:',font=('Verdana', 13, 'bold')).place(x=1040,y=330)
        self.totalentrybox = ttk.Entry(self.frame,width=15)
        self.totalentrybox.place(x=1040,y=360)
    
    
    
    
    def set_descending(self):
        var = self.descending_variable.get()
        if var == 1:
            self.secondtree.delete(*self.secondtree.get_children())
            descending_df = self.product_df.sort_values(by=['PREÇO'],ascending=False)
            cods = descending_df['CÓDIGO'].tolist()  
            especs = descending_df['ESPECIFICAÇÃO'].tolist()
            prices = descending_df['PREÇO'].tolist()
            codslist = []
            for item in cods:
                new_item = str(item).strip().upper()
                codslist.append(new_item)  
            finalprices = []
            for item in prices:
                price = str(item)
                formatted_price = price.replace(',','.')
                formatted_price = formatted_price.replace('PREÇO','00000000')
                final_price = formatted_price.removeprefix('R$').strip()
                finalprices.append(float(final_price))
            for i in range(0,len(descending_df)):
                entire_list = (cods[i],especs[i],prices[i])
                self.secondtree.insert('',END,values=entire_list)
        elif var == 0:
            self.secondtree.delete(*self.secondtree.get_children())
            cods = self.product_df['CÓDIGO'].tolist()
            especs = self.product_df['ESPECIFICAÇÃO'].tolist()
            prices = self.product_df['PREÇO'].tolist()
            codslist = []
            for item in cods:
                new_item = str(item).strip().upper()
                codslist.append(new_item)  
            finalprices = []
            for item in prices:
                price = str(item)
                formatted_price = price.replace(',','.')
                formatted_price = formatted_price.replace('PREÇO','00000000')
                final_price = formatted_price.removeprefix('R$').strip()
                finalprices.append(float(final_price))
                
            for i in range(0,len(self.product_df)):
                entire_list = (codslist[i],especs[i],finalprices[i])
                self.secondtree.insert('',END,values=entire_list)
                
                
                
    def set_ascending(self):
        var = self.ascending_variable.get()
        if var == 1:
            self.secondtree.delete(*self.secondtree.get_children())
            ascending_df = self.product_df.sort_values(by=['PREÇO'])
            cods = ascending_df['CÓDIGO'].tolist()  
            especs = ascending_df['ESPECIFICAÇÃO'].tolist()
            prices = ascending_df['PREÇO'].tolist()
            codslist = []
            for item in cods:
                new_item = str(item).strip().upper()
                codslist.append(new_item)  
            finalprices = []
            for item in prices:
                price = str(item)
                formatted_price = price.replace(',','.')
                formatted_price = formatted_price.replace('PREÇO','00000000')
                final_price = formatted_price.removeprefix('R$').strip()
                finalprices.append(float(final_price))
            for i in range(0,len(ascending_df)):
                entire_list = (cods[i],especs[i],prices[i])
                self.secondtree.insert('',END,values=entire_list)
        elif var == 0:
            self.secondtree.delete(*self.secondtree.get_children())
            cods = self.product_df['CÓDIGO'].tolist()
            especs = self.product_df['ESPECIFICAÇÃO'].tolist()
            prices = self.product_df['PREÇO'].tolist()
            codslist = []
            for item in cods:
                new_item = str(item).strip().upper()
                codslist.append(new_item)  
            finalprices = []
            for item in prices:
                price = str(item)
                formatted_price = price.replace(',','.')
                formatted_price = formatted_price.replace('PREÇO','00000000')
                final_price = formatted_price.removeprefix('R$').strip()
                finalprices.append(float(final_price))
                
            for i in range(0,len(self.product_df)):
                entire_list = (codslist[i],especs[i],finalprices[i])
                self.secondtree.insert('',END,values=entire_list)
            
        
    def set_alphabetic(self):
        var = self.alphabetic_variable.get()
        if var == 1:
            self.secondtree.delete(*self.secondtree.get_children())
            alphabetic_df = self.product_df.sort_values(by=['ESPECIFICAÇÃO'])
            cods = alphabetic_df['CÓDIGO'].tolist()  
            especs = alphabetic_df['ESPECIFICAÇÃO'].tolist()
            prices = alphabetic_df['PREÇO'].tolist()
            codslist = []
            for item in cods:
                new_item = str(item).strip().upper()
                codslist.append(new_item)  
            finalprices = []
            for item in prices:
                price = str(item)
                formatted_price = price.replace(',','.')
                formatted_price = formatted_price.replace('PREÇO','00000000')
                final_price = formatted_price.removeprefix('R$').strip()
                finalprices.append(float(final_price))
            for i in range(0,len(alphabetic_df)):
                entire_list = (cods[i],especs[i],prices[i])
                self.secondtree.insert('',END,values=entire_list)
        elif var == 0:
            self.secondtree.delete(*self.secondtree.get_children())
            cods = self.product_df['CÓDIGO'].tolist()
            especs = self.product_df['ESPECIFICAÇÃO'].tolist()
            prices = self.product_df['PREÇO'].tolist()
            codslist = []
            for item in cods:
                new_item = str(item).strip().upper()
                codslist.append(new_item)  
            finalprices = []
            for item in prices:
                price = str(item)
                formatted_price = price.replace(',','.')
                formatted_price = formatted_price.replace('PREÇO','00000000')
                final_price = formatted_price.removeprefix('R$').strip()
                finalprices.append(float(final_price))
                
            for i in range(0,len(self.product_df)):
                entire_list = (codslist[i],especs[i],finalprices[i])
                self.secondtree.insert('',END,values=entire_list)
            
    
    def load_archive(self,event):
        name = self.archivename.get()
        self.secondtree.delete(*self.secondtree.get_children())
        self.product_data = pd.read_excel(f'_files/{name}')
        self.product_df = pd.DataFrame(self.product_data)
        self.product_df.dropna(inplace=True)
        self.product_df.drop(self.product_df[self.product_df['PREÇO'].astype(str).str.contains('PREÇO',case=False)].index,inplace=True)
        self.product_df['PREÇO'] = self.product_df['PREÇO'].apply(lambda x: x.replace(',','.').strip() if isinstance(x,str) else x)
        self.product_df = self.product_df.astype({"PREÇO": float})
        self.carregar.config(text="SUCESSO",width=15)
        self.carregar.after(1500,lambda:self.carregar.config(text="CARREGAR",width=15))
        cods = self.product_df['CÓDIGO'].tolist()
        especs = self.product_df['ESPECIFICAÇÃO'].tolist()
        prices = self.product_df['PREÇO'].tolist()
        codslist = []
        for item in cods:
            new_item = str(item).strip().upper()
            codslist.append(new_item)  
        finalprices = []
        for item in prices:
            price = str(item)
            formatted_price = price.replace(',','.')
            formatted_price = formatted_price.replace('PREÇO','00000000')
            final_price = formatted_price.removeprefix('R$').strip()
            finalprices.append(float(final_price))
            
        for i in range(0,len(self.product_df)):
            entire_list = (codslist[i],especs[i],finalprices[i])
            self.secondtree.insert('',END,values=entire_list)

            

    
    def search_for_infos(self,event):
        espec = self.especification.get()
        self.secondtree.delete(*self.secondtree.get_children())
        dataoccurrences = self.product_df[self.product_df['ESPECIFICAÇÃO'].str.contains(espec,case=False) == True]
        cods = dataoccurrences['CÓDIGO'].tolist()  
        especs = dataoccurrences['ESPECIFICAÇÃO'].tolist()
        prices = dataoccurrences['PREÇO'].tolist()
        for i in range(0,len(dataoccurrences)):
            entire_list = (cods[i],especs[i],prices[i])
            self.secondtree.insert('',END,values=entire_list)
        self.procurar.config(text='SUCESSO')
        self.addproductone.after(1500,lambda: self.procurar.config(text='PROCURAR/RESETAR',width=19))

            
        
    def pull_infos(self,event):
        qtd = self.quantiaentry.get()

        if qtd.isnumeric():
            selected_items = self.secondtree.selection()
            for selected_item in selected_items:
                cod = self.secondtree.item(selected_item)['values'][0]
                espec = self.secondtree.item(selected_item)['values'][1]
                price = self.secondtree.item(selected_item)['values'][2]
                treatmentprice = str(price).strip().replace(',','.')
                total = float(treatmentprice)*float(qtd)
                tuple_of_products = (float(qtd),cod,espec,float(treatmentprice),f'R${total :.2f}')
                self.list_of_products.append(tuple_of_products)
                self.tree.insert('',END,values=tuple_of_products)
            self.addproductone.config(text='SUCESSO')
            self.addproductone.after(1500,lambda: self.addproductone.config(text='ADICIONAR',width=19))
            self.especification.delete(0,END)
            self.quantiaentry.delete(0,END)
            self.update_sum()
        else:
            self.addproductone.config(text='UM ERRO OCORREU')
            self.addproductone.after(1500,lambda: self.addproductone.config(text='ADICIONAR',width=19))
    
    def update_sum(self):
        self.sum_of_products = 0
        for item in self.list_of_products:
            multiplied_result = item[3]*item[0]
            self.sum_of_products += multiplied_result
            
        formatted_price = f'R${self.sum_of_products :.2f}'
        self.totalentrybox.delete(0,'end')
        self.totalentrybox.insert(0,formatted_price)
        
        
        
        
    def insert_infos(self,event):
        def reset_button():
            self.addproduct.config(text='adicionar',width=15)
        self.product_df.set_index('CÓDIGO',inplace=True)
        qtd = self.firstentry.get()
        cod = self.secondentry.get().upper().strip()
        if cod.isnumeric():    
            especs = find_especs_by_code(int(cod),self.product_df)
            prices = find_prices_by_code(int(cod),self.product_df)
        else:
            especs = find_especs_by_code(str(cod),self.product_df)
            prices = find_prices_by_code(str(cod),self.product_df)
        total = float(prices)*float(qtd)
        tuple_of_product = (float(qtd),cod,especs,float(prices),f'R${total :.2f}')
        self.list_of_products.append(tuple_of_product)
        self.tree.insert('',END,values=tuple_of_product)     
        self.addproduct.config(text='SUCESSO')
        self.addproduct.after(1000,reset_button)
        self.firstentry.delete(0, END)
        self.secondentry.delete(0, END)
        self.firstentry.focus_force()
        self.product_df.reset_index(inplace=True)
        self.update_sum()

        

        
    def delete_item(self,event):
            selected_items = self.tree.selection()
            for selected_item in selected_items:          
                for i in range(0,len(self.list_of_products)):
                    for item in self.list_of_products:
                        if item[1] == self.tree.item(selected_item)['values'][1]:
                            self.list_of_products.remove(item)  
                            break      
                self.tree.delete(selected_item)   
                self.update_sum()
                
            
            
    
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
                self.savebutton.config(text='SALVO COM SUCESSO',width=25)
                self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15))
            else:
                self.savebutton.config(text='ERRO  AO SALVAR, VERIFIQUE AS INFORMAÇÕES',width=44)
            self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15))
        except:    
            self.savebutton.config(text='ERRO TÉCNICO AO SALVAR',fg='white',bg='red',border=2,width=30)
            self.savebutton.after(1500,lambda:self.savebutton.config(text='SALVAR',width=15))
            
        



if __name__ == '__main__':
    root = Tk()
    MainApplication(root)
    root.mainloop()
