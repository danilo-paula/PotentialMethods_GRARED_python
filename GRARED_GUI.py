#encoding: utf-8
from tkinter import *

#--------------------------------------------------
#Ambiente Tkinter
#--------------------------------------------------
class Packing:
    def __init__(self, toplevel):
        
        self.frame1=Frame(toplevel)
        self.frame1.pack()
        self.frame2=Frame(toplevel)
        self.frame2.pack()

        self.T_tipo_arquivo_entrada=Label(self.frame1, width=15,height=6,font=('Arial','10'),
                          text='Tipo de Arquivo:')
        self.T_tipo_arquivo_entrada.pack(side=LEFT)
        self.T_caminho_entrada=Label(self.frame1, width=25,height=6,font=('Arial','10'),
                          text='Caminho do arquivo de dados:')
        self.T_caminho_entrada.pack(side=LEFT)
        
        
raiz=Tk()
Packing(raiz)
raiz.mainloop()
