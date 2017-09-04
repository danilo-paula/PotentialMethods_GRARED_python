#encoding: utf-8
from tkinter import *

#--------------------------------------------------
#Ambiente Tkinter
#--------------------------------------------------
class Packing:
    def __init__(self, toplevel):
        
        self.frame=Frame(toplevel).grid()


        self.T_tipo_arquivo_entrada=Label(self.frame,font=('Arial','10'),
                          text='Tipo de Arquivo: ')
        self.T_tipo_arquivo_entrada.grid(row=0,column=0,rowspan=2, padx=10)
        self.var_tipo=StringVar(toplevel)
        self.var_tipo.set('excel')
        self.RB_excel=Radiobutton(self.frame, text='Excel', value='excel', variable=self.var_tipo, command=self.var_tipo.set('excel'))
        self.RB_excel.grid(row=0,column=1,sticky=W)
        self.RB_txt=Radiobutton(self.frame, text='TXT Tabulado', value='txt', variable=self.var_tipo, command=self.var_tipo.set('txt'))
        self.RB_txt.grid(row=1,column=1,sticky=W)
        
        self.T_entrada=Label(self.frame, font=('Arial','10'), text='   Arquivo de dados:')
        self.T_entrada.grid(row=0,column=2,rowspan=2,sticky=E,padx=20)
        self.var_entrada=StringVar(toplevel)
        self.var_entrada.set('GRARED_P_valores.xlsx')
        self.E_entrada=Entry(self.frame, width=30,textvar=self.var_entrada).grid(row=0,column=3,rowspan=2,sticky=W,padx=5)
        
        
raiz=Tk()
Packing(raiz)
raiz.mainloop()
