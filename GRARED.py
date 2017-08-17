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
g_med_lido = p_matriz[1] #Gravidade Lida no equipamento

fator_gravim = p_matriz[2]#Fator gravimétrico da Região

Lat_gra = p_matriz[3]#Latitude Graus
Lat_min = p_matriz[4]#Latitude Minutos
Lat_seg = p_matriz[5]#Latitude segundos


Lon_gra = p_matriz[6]#Longitude Graus
Lon_min = p_matriz[7]#Longitude Minutos
Lon_seg = p_matriz[8]#Longitude segundos

alt_m = p_matriz[9]#Altitude geométrica obtida pelos receptores GNSS em metros

hora = p_matriz[10]#Hora Local da leitura
minuto = p_matriz[11]#Minuto Local da leitura

dia = p_matriz[12]#Dia da leitura
mes = p_matriz[13]#Mês da leitura
ano = p_matriz[14]#Ano da leitura
fuso_horario = p_matriz[15]#Fuso-horário do local

azim_navio_gra = p_matriz[16]#Azimute de navegação Graus
azim_navio_min = p_matriz[17]#Azimute de navegação Minutos
azim_navio_seg = p_matriz[18]#Azimute de navegação Segundos
v_navio = p_matriz[19]#Velocidade da embarcação em nós

densidade_crustal = p_matriz[20]#Densidade da parte crustal da região g/cm^3

p_atm_kpa = p_matriz[21]#Pressão atmosférica em kPa


#--------------------------------------------------
#Constantes
#--------------------------------------------------
densidade_med=2.67 #Densidade média/padrão do materia crustal
fator_gravim_med=1.20 #Fator gravimétrico médio

#--------------------------------------------------
#Conversões preliminares
#--------------------------------------------------
Lat_graus_dec=Lat_gra+(Lat_min/60)+(Lat_seg/3600) #Latitude em Graus decimais
Lat_rad=np.radians(Lat_graus_dec) #Latitude em radianos

Lon_graus_dec=Lon_gra+(Lon_min/60)+(Lon_seg/3600) #Longitude em Graus decimais
Lon_rad=np.radians(Lon_graus_dec) #Longitude em radianos

alt_cm=alt_m*100 #Altitude geométrica obtida pelos receptores GNSS em centimetros


#--------------------------------------------------
#Correções e Transformações importantes
#--------------------------------------------------

    #Correção Bouguer
    #**********************************************
