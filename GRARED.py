#encoding: utf-8

#--------------------------------------------------
#Import das bibliotecas
#--------------------------------------------------
import numpy as np
import pandas as pd
import cx_Freeze
from tkinter import *

#--------------------------------------------------
#Ambiente Tkinter
#--------------------------------------------------
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
    #Menu Principal
    #**********************************************
def ajuda() :
    with open("Ajuda_GRARED.txt", 'r') as f: #Função que define o comando de "ajuda"
        Texto_Ajuda=f.read()  #Leitura do txt de ajuda
        root=Tk()       #Iniciando uma nova instancia para abertura de janela
        frame_janela=Frame(root) ; frame_janela.pack()  #Indica em qual instancia está, renderiza na instancia
        frame_janela.master.title("Ajuda")  #Título da janela
        frame_janela.master.geometry("800x400+15+30")  #Configurações da geometria da janela de ajuda
        Texto_Caixa_Ajuda=Label(frame_janela, text=Texto_Ajuda,foreground="black") #Indicação de qual texto e cores
        Texto_Caixa_Ajuda.pack() #Renderização do texto no frame
        Texto_Caixa_Ajuda.configure(relief="ridge", font="Arial 12 bold") #Configurações de tamanho,diferenciação e fonte do texto
janela_principal=Tk() #Iniciando uma nova instancia para abertura da janela principal
m_principal=Menu(janela_principal)  #Definição do Menu Principal
arquivo=Menu(m_principal)  #Definição do primeiro tópico "Arquivo"
m_principal.add_command(label="Ajuda",command=ajuda)  #Adição do menu "Ajuda" ao Menu Principal
janela_principal.configure(menu=m_principal)  #Torna o Menu Principal o menu do frame principal

    #Corpo do programa
    #**********************************************
t_planilha= Label(text="Por favor indique onde esta a planilha")
t_planilha.pack(side='top')
t_planilha.configure(font="Arial 12 bold")

#Fazer um botão e que quando clique salve a entry em uma variável contendo o diretório do arquivo que foi digitado
#!!!!!
caminho_planilha_informado = StringVar(janela_principal)
caminho_planilha = StringVar(janela_principal)
def aritmetica (e):
    caminho_planilha.set(caminho_planilha_informado.get())
    mostrar_c=Label(janela_principal, text=caminho_planilha)
    mostrar_c.pack()
eparcela = Entry(textvar=caminho_planilha)
eparcela.bind("<Return>", aritmetica)
eparcela.pack()

#Fazer os radiobutons e entrys
#!!!!!
b_densidade=True
b_fator_gravim=True


    #Configuradores de Janela
    #**********************************************
app=Application()  #Instanciação da Interface
app.master.title("GRARED Alpha v.0.1")  #Titulo do Cabeçalho
app.master.geometry("800x600+10+10") #Altura Tela, Largura Tela, Anda Em X, Anda Em Y. OBS:Origem é o Canto Superior Esquerdo
mainloop()  #Laço de tratamento de eventos



#--------------------------------------------------
#Variáveis de entrada
#--------------------------------------------------
planilha_entrada="GRARED_P_valores.xlsx" #!!!!Trocar no final,esta é de testes

p_mat_ler = pd.read_excel(planilha_entrada, sheetname='Plan1',header=None,skiprows=2,dtype=float) #Leitura interna da planilha
p_matriz=p_mat_ler.values.T #Salvamento da planilha lida em matriz transposta de arrays

ponto = p_matriz[0]#Identificador do ponto
g_l1= p_matriz[1]#Primeira Leitura
g_l2= p_matriz[2]#Segunda Leitura
g_l3= p_matriz[3]#Terceira Leitura

Lat_gra = p_matriz[4]#Latitude Graus
Lat_min = p_matriz[5]#Latitude Minutos
Lat_seg = p_matriz[6]#Latitude segundos


Lon_gra = p_matriz[7]#Longitude Graus
Lon_min = p_matriz[8]#Longitude Minutos
Lon_seg = p_matriz[9]#Longitude segundos

alt_m = p_matriz[10]#Altitude geométrica obtida pelos receptores GNSS em metros

hora = p_matriz[11]#Hora Local da leitura
minuto = p_matriz[12]#Minuto Local da leitura


p_atm_kpa = p_matriz[13]#Pressão atmosférica em kPa


#implementar com radiobutons
fator_gravim_lido=2#Fator gravimétrico da Região
fuso_horario =  2#Fuso-horário do local

#implementar com entry
densidade_lida=2#Densidade da parte crustal da região g/cm^3

dia = 3#Dia da leitura
mes = 12#Mês da leitura
ano = 2017#Ano da leitura
#--------------------------------------------------
#Constantes
#--------------------------------------------------
densidade_med=2.67 #Densidade média/padrão do materia crustal
fator_gravim_med=1.20 #Fator gravimétrico médio

#--------------------------------------------------
#Escolha de valores
#--------------------------------------------------
if b_densidade==False:  #Escolha entre valor padrão de densidade crustal e valor fornecido
    densidade=densidade_lida
else:
    densidade=densidade_med

if b_fator_gravim==False: #Escolha entre valor padrão de fator gravimétrico e valor fornecido
    fator_gravim=fator_gravim_lido
else:
    fator_gravim=fator_gravim_med
    

#--------------------------------------------------
#Conversões preliminares
#--------------------------------------------------
g_med_lido = (g_l1+g_l2+g_l3)/3 #Média das 3 leituras

Lat_graus_dec = Lat_gra+(Lat_min/60)+(Lat_seg/3600) #Latitude em Graus decimais
Lat_rad=np.radians(Lat_graus_dec) #Latitude em radianos

Lon_graus_dec = Lon_gra+(Lon_min/60)+(Lon_seg/3600) #Longitude em Graus decimais
Lon_rad=np.radians(Lon_graus_dec) #Longitude em radianos

alt_cm = alt_m*100 #Altitude geométrica obtida pelos receptores GNSS em centimetros


#--------------------------------------------------
#Correções e Transformações importantes
#--------------------------------------------------

    #Correção Bouguer Simples
    #**********************************************
cb=[]
for i in alt_m:
    if i>0:
        c_b=0.04192*densidade*i
        cb=np.append(cb,c_b)
    elif i<0:
        c_b=0.08384*densidade*i
        cb=np.append(cb,c_b)
    else:
        c_b=0
        cb=np.append(cb,c_b)
   
    #Correção Ar-livre
    #**********************************************
ca=0.3086*alt_m

    #Correção Precipitação, para terrenos extremamente chuvosos
    #**********************************************
cprec=0.04192*alt_m


