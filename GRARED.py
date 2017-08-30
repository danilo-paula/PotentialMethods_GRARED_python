#encoding: utf-8

#--------------------------------------------------
#Import das bibliotecas
#--------------------------------------------------
import numpy as np
import pandas as pd
import cx_Freeze
from tkinter import *

#--------------------------------------------------
#Variáveis de entrada
#--------------------------------------------------
planilha_entrada="GRARED_P_valores.xlsx" #!!!!Trocar no final para "GRARED_P.xlsx", esta é de testes
                                         #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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



planilha_conv="Tab_conv_G996.txt"
gc1,gc2,gf0=np.loadtxt(planilha_conv,skiprows=1,unpack=True)

#!!!!!implementar com desizantes
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fuso_horario =-3#Fuso-horário do local
fator_gravim_lido=1.22#Fator gravimétrico da Região

#!!!!!!!!!!implementar com entry
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
g_ref=9.8

densidade_lida=2.5#Densidade da parte crustal da região g/cm^3

dia = 31#Dia da leitura
mes = 10#Mês da leitura
ano = 1996#Ano da leitura
#--------------------------------------------------
#Constantes
#--------------------------------------------------
densidade_med=2.67 #Densidade média/padrão do materia crustal
fator_gravim_med=1.20 #Fator gravimétrico médio

#--------------------------------------------------
#Escolha de valores
#--------------------------------------------------

#Fazer os radiobutons e entrys
#!!!!!
b_densidade=True
b_fator_gravim=True

#!!!!!!!!!!implementar com check butons
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if b_densidade==False:  #Escolha entre valor padrão de densidade crustal e valor fornecido
    densidade=densidade_lida
else:
    densidade=densidade_med

if b_fator_gravim==False: #Escolha entre valor padrão de fator gravimétrico e valor fornecido
    fator_gravim=fator_gravim_lido
else:
    fator_gravim=fator_gravim_med
    

#--------------------------------------------------
#Conversões e cálculos preliminares
#--------------------------------------------------

Lat_graus_dec = Lat_gra+(Lat_min/60)+(Lat_seg/3600) #Latitude em Graus decimais
Lat_rad=np.radians(Lat_graus_dec) #Latitude em radianos

Lon_graus_dec = Lon_gra+(Lon_min/60)+(Lon_seg/3600) #Longitude em Graus decimais
Lon_rad=np.radians(Lon_graus_dec) #Longitude em radianos

alt_cm = alt_m*100 #Altitude geométrica obtida pelos receptores GNSS em centimetros

hora_utc=(hora-fuso_horario)
    #Cálculo de Séculos Julianos à partir de 31/dez/1899
    #**********************************************
dia_c=dia+(hora_utc/24)+(minuto/(60*24))
jd_inicial=(1461*(1899+4800+(12-14)/12))/4+(367*(12-2-12*(( 12-14)/12)))/12-(3*((1899+4900+(12-14)/12)/100))/4+31-32075
jd =(1461*(ano+4800+(mes-14)/12))/4+(367*(mes-2-12*(( mes-14)/12)))/12-(3*((ano+4900+(mes-14)/12)/100))/4+dia_c-32075
jc=((jd-jd_inicial)*24*60)/52596000

    #Cinversão de G instrumental para mGal
    #**********************************************
g_med_lido = (g_l1+g_l2+g_l3)/3 #Média das 3 leituras
g_conv=[]
contador=int(0)
while len(g_conv) != len(g_med_lido): #Até a lista de acel. Grav. em mGals, não tiver o mesmo tamanho que a lista da acel. Grav. lida faça isso:
    for item in gc1:                                #   Pegue um valor N de sua tabela de leituras, iniciando com o primeiro valor e indo até o ultimo,
        diferença=g_med_lido[contador]-item         # faça a diferença entre esse N e todos os valores de gc1, se 0<=Diferença<100, então aplique a conversão
        if diferença < 100 and diferença>=0:        # e adicione o resultado na lista de acel. Grav. em mGals, até ter feito tudo isto com todos os valores da
            gc1l=gc1.tolist()                       # tabela de leitura.
            gc_pos=gc1l.index(item)                 
            gp=gc2[gc_pos]+(gf0[gc_pos]*(diferença))
            g_conv=np.append(g_conv,gp) 
    contador=contador+1

#--------------------------------------------------
#Correções e Transformações importantes
#--------------------------------------------------
    #Cálculo de Aceleração do GRS67
    #**********************************************
g_teor67=978031.8*(1+0.0053024*((np.sin(Lat_rad))**2)-0.0000059*((np.sin(2*Lat_rad))**2))

    #Cálculo de Aceleração do GRS80
    #**********************************************
g_teor80=978032.7*(1+0.0053024*((np.sin(Lat_rad))**2)-0.0000058*((np.sin(2*Lat_rad))**2))

    #Cálculo de Aceleração do GRS84
    #**********************************************
g_teor84=(9.7803267714*((1+0.00193185138639*((np.sin(Lat_rad))**2))/((1-0.00669437999013*((np.sin(Lat_rad))**2)**(1/2)))))*(100000)

    #Correção da deriva instrumental
    #**********************************************


    #Correção Bouguer Simples
    #**********************************************
cb=[]
for item in alt_m:
    if item>0:
        c_b=0.04192*densidade*item
        cb=np.append(cb,c_b)
    elif item<0:
        c_b=0.08384*densidade*item
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
