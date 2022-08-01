from tkinter import *
from tkinter import ttk



class MainApplication:
    def __init__(self, toplevel):
        config = ('Verdana', 15, 'bold')
        columns = ('qtd','cod','espec','pre')

        self.frame = Frame(toplevel).grid()
        self.frame2 = Frame(toplevel).grid()
        
        

        self.title = Label(self.frame, text='DATA STRUCTURAE', font=config).grid()
        
        self.labelarchive = Label(self.frame,text='Nome da tabela a ser lida: ',font=('Verdana',10,'bold')).grid()
        self.archivename = Entry(self.frame)
        self.archivename.grid()
        
        self.firstlabel = Label(self.frame, text='QUANTIDADE',
                                font=('Verdana', 10, 'bold')).grid(column=0)
        self.firstentry = Entry(self.frame)
        self.firstentry.grid()
        




        self.secondlabel = Label(self.frame, text='CÓDIGO',
                                 font=('Verdana', 10, 'bold')).grid()
        self.secondentry = Entry(self.frame)
        self.secondentry.grid(pady=5)

        
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
        
        self.savebutton = Button(self.frame,text='SALVAR',width=15,fg='black',bg='white',border=2,relief='raised')
        self.savebutton.grid(pady=5)



root = Tk()
MainApplication(root)
root.geometry('900x600')
root.mainloop()