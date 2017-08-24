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



#!!!!!implementar com desizantes
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fuso_horario =-3#Fuso-horário do local
fator_gravim_lido=1.22#Fator gravimétrico da Região

#!!!!!!!!!!implementar com entry
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

densidade_lida=2#Densidade da parte crustal da região g/cm^3

dia = 31#Dia da leitura
mes = 10#Mês da leitura
ano = 1996#Ano da leitura
#--------------------------------------------------
#Constantes
#--------------------------------------------------
densidade_med=2.67 #Densidade média/padrão do materia crustal
fator_gravim_med=1.20 #Fator gravimétrico médio

M_l=7.34581119761*10**(25)#Massa da lua em gramas
M_s=1.9884158*10**(33)#Massa do sol em gramas
G=6.67428*10**(-8) #Constante gravitacional universal
a=6.378137*10**(8)#Raio equatorial da Terra em cm
c=3.844031*10**(10)#Distância média entre o centro da Terra e da Lua em cm
c_s=1.49597870691*10**(13)#Distância média entre o centro da Terra e do Sol em cm 
e=0.05490#Ecentricidade da órbita lunar
m=0.074804#Taxa média de movimento do Sol em relação à  Lua
w_t=(23+(27/60)+(8.26/3600))#Obliquidade da ecliptica em 1 de Janeiro de 1900 em Graus decimais
i=5+(8/60)+(43.3546/3600)#Ângulo entre a órbita lunar e o plano da ecliptica em Graus decimais

#!!!!!!!!!!Pode mudar com GRS67/80/84, ver http://www.ufrgs.br/engcart/Teste/refer_exp.html
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
f=(1/298.257222101)#Achatamento do elipsoide

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
g_med_lido = (g_l1+g_l2+g_l3)/3 #Média das 3 leituras

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

    #Correção do Efeito de Maré, também chamado de atração Luni-Solar
    #**********************************************
#CORRIGIR URGENTEMENTE SENOS E COSSENOS PARA ENTRADA EM RADIANOS
        #Componente Lunar
        #----------------
b=a-(a*f) #2.6.1.1.1.1.1
e_e2=(a**2-b**2)/(b**2) #2.6.1.1.1.1
Ç=(1/(1+e_e2*np.sin(Lat_rad)**2))**(0.5) #2.6.1.1.1
r=Ç*a+alt_cm #2.6.1.1
a_=1/(c*e**2) #2.6.1.2.1
s=(270+26/60+11.72/3600)+(1336*360+1108406.05/3600)*jc+(7.128/3600)*jc**2+(0.0072/3600*jc**3) #2.6.1.2.2 
p=(334+19/60+46.42/3600)+(11*360+392522.51/3600)*jc-(37.15/3600)*jc**2-(0.036/3600)*jc**3 #2.6.1.2.3 
h_s=(279+41/60+48.05/3600)+(129602768.11/3600)*jc+(1.08/3600)*jc**2 #2.6.1.2.4  
d_l=1/((1/c)+a_*e*np.cos(s-p)+a_*e**2*np.cos(2*(s-p))+(15/8)*a_*m*e*np.cos(s-2*h_s+p)+a_*m**2*np.cos(2*(s-h_s))) #2.6.1.2
n_lambda=(259+10/60+57.12/3600)-(5*360+482912.63/3600)*jc+(7.58/3600)*jc**2+(0.008/3600)*jc**3 
I=np.arccos(np.cos(w_t)*np.cos(i)-np.sin(w_t)*np.sin(i)*np.cos(n_lambda)) #2.6.1.3.1 !!!!!!!!!!!!!!!Arco que deve ser convertido
v=np.arcsin(np.sin(i)*np.sin(n_lambda))/np.sin(I) #2.6.1.3.2.1  !!!!!!!!!!!!!!!!!!!!!!!!Arco que deve ser convertido
t_a=(15*((hora_utc+minuto/60)-12)-Lon_graus_dec) #2.6.1.3.2.2 
X=(t_a+h_s-v) #2.6.1.3.2 
seno_alfa=np.sin(w_t)*np.sin(n_lambda)*np.sin(I) #2.6.1.3.3.1.1.1.1
cosseno_alfa=np.cos(n_lambda)*np.cos(v)+np.sin(n_lambda)*np.sin(v)*np.cos(w_t) #2.6.1.3.3.1.1.1.2
alfa=2*np.arctan(seno_alfa/(1+cosseno_alfa)) #2.6.1.3.3.1.1.1 !!!!!!!Arco que deve ser convertido  --->Reaveriguar valores associados, caso resultado final seja incompativel
E=n_lambda-alfa #2.6.1.3.3.1.1
sigma=s-E #2.6.1.3.3.1 
l=sigma-2*e*np.sin(s-p)+(5/4)*e**2*np.sin(2*(s-p))+(15/4)*m*e*np.sin(s-2*h_s+p)+1.375*m**2*np.sin(2*(s-h_s)) #2.6.1.3.3 
cosseno_t_l=np.sin(Lat_rad)*np.sin(I)*np.sin(l)+np.cos(Lat_rad)*(np.cos(l/2)**2*np.cos(l+X)) #2.6.1.3 
C_l=(((G*M_l*r)/(d_l**3))*(3*cosseno_t_l**2-1)+((3/2)*((G*M_l*r**2)/(d_l**4)))*(5*cosseno_t_l**3-3*cosseno_t_l)) #2.6.1

        #Componente Solar
        #----------------
e_1=1.675104*10**(-2)-4.180*10**(-5)*jc-1.26*10**(-7)*jc**2 #2.6.1.1
a1_=1/(c_s*(1-e_1**2)) #2.6.1.2
p_s=(281+13/60+15/3600)+(6189.03/3600)*jc+(1.63/3600)*jc**2+(0.012/3600)*jc**3 #2.6.2.1.3 
d_s=1/(c_s+a1_*e_1*np.cos(h_s-p_s)) #2.6.2.1 --->Reaveriguar valores associados, caso resultado final seja incompativel
l_s=h_s+2*e_1*np.sin(h_s-p_s) #2.6.2.2.1
X_s=t_a+h_s #2.6.2.2.2
t_s=np.sin(Lat_rad)*np.sin(w_t)*np.sin(l_s)+np.cos(Lon_rad)*(np.cos(w_t/2)**2*np.cos(l_s-X_s)+np.sin(w_t/2)**2*np.cos(l_s-X_s)) #2.6.2.2
C_s=((G*M_s*r)/(d_s**3))*(3*np.cos(t_s)**2-1) #2.6.2

cls=(C_l+C_s)*fator_gravim #2.6



