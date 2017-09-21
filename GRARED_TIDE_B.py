# -*- coding: utf-8 -*-
import numpy as np

radum=0.01745329251

#entradas
dia=18
mes=2
ano=2011

ano_c=ano+mes/12+(dia+0.5)/365.25
fuso=0
hora=8+10/60
lat=(-(22+44/60))
long=(-(90+30/60))
alt=0
fator_grav=1.17

#constantes
radum=0.01745329251

M_l=7.34581119761e25
M_s=1.9884158e33
G =6.67428e-8
c_s=1.49597870691e13
w_t=(23+(27/60)+(8.26/3600))
i=(5+(8/60)+(43.3546/3600))
f=1/298.257222101
c=3.844031e10
e=0.05490
m=0.074804
a=6.378136e8

#transformações
b=a-(a*f)
e_e2=(a**2-b**2)/b**2
C=(1/(1+e_e2*(np.sin(lat)**2)))**0.5
r=C*a+100*alt
a_=1/(c*(1-e**2))
tj=(ano_c*365.25-((1899+1+(31.5/365.25))*365.25))/(100*365.25)
t_a=15*((hora-fuso)-12)-long

s=(270+(26/60)+(11.72/3600))+(1336*360+1108406.05/3600)*tj+(7.128/3600)*tj**2+(0.0072/3600)*tj**3
p=(334+(19/60)+(46.42/3600))+(11*360+392522.51/3600)*tj-(37.15/3600)*tj**2-(0.036/3600)*tj**3
h_s=(279+(41/60)+(48.05/3600))+(129602768.11/3600)*tj+(1.080/3600)*tj**2
N_l=(259+(10/60)+(43.3546/3600))-(5*360+482912.63/3600)*tj+(7.58/3600)*tj**2+(0.008/3600)*tj**3

cosI=np.cos(w_t*radum)*np.cos(i*radum)-np.sin(w_t*radum)*np.sin(i*radum)*np.cos(N_l*radum)
senI=(1-cosI**2)**0.5
I=np.arctan(senI/cosI)#Rad

senv=np.sin(i*radum)*np.sin(N_l*radum)/np.sin(I)
cosv=(1-senv**2)**0.5
v=np.arctan(senv/cosv) #Rad


senA=np.sin(w_t*radum)*np.sin(N_l*radum)/np.sin(I)
cosA=(1-senA**2)**0.5 #Advindo de Igc-1
cosA2=np.cos(N_l*radum)*np.cos(v)+np.sin(N_l*radum)*np.sin(v)*np.cos(w_t*radum) #Recomendado
A=np.arctan(senA/cosA)
A2=np.arctan(senA/cosA2)
eps=N_l-A #--------------Decidir na comparação entre A e A2-----------------

sigma=s-eps
l=sigma+2*e*np.sin((s-p)*radum)+5/4*e**2*np.sin(2*(s-p)*radum)+15/4*m*e*np.sin((s-2*h_s+p)*radum)+11/8*m**2*np.sin(2*(s-h_s)*radum) #Rad
X=t_a*radum+h_s*radum-v #Rad

cosT=np.sin(lat*radum)*np.sin(I)*np.sin(l)+np.cos(lat*radum)*(np.cos(I/2)**2*np.cos(l-X)+np.sin(I/2)**2*np.cos(l+X))
senT=(1-cosT**2)**0.5
T=np.arctan(senT/cosT) #Rad

d_l=1/(1/c+a_*e*np.cos((s-p)*radum)+a_*e**2*np.cos(2*(s-p)*radum)+15/8*a_*m*e*np.cos((s-2*h_s+p)*radum)+a_*m**2*np.cos(2*(s-h_s)*radum))
c_l=(G*M_l*r)/(d_l**3)*(3*np.cos(T)**2-1)+3/2*(G*M_l*r**2)/(d_l**4)*(5*np.cos(T)**3-3*np.cos(T)) #----Decidir entr np.cos(T) e cosT----


e_1=1.675101e-2-4.180e-5*tj-1.26e-7*tj**2
_a_1=1/(c_s*(1-e_1**2))
p_s=(281+(13/60)+(15/3600))+6189.03/3600*tj+1.63/3600*tj**2+0.012/3600*tj**3
d_s=1/(1/(c_s+_a_1*e_1*np.cos((h_s-p_s)*radum)))
l_s=h_s*radum+2*e_1*np.sin((h_s-p_s)*radum) #Rad
X_s=t_a*radum+h_s*radum #Rad

cosT_s=np.sin(lat*radum)*np.sin(w_t*radum)*np.sin(l_s)+np.cos(long*radum)*(np.cos((w_t*radum)/2)**2*np.cos(l_s/X_s)+np.sin((w_t*radum)/2)**2*np.cos(l_s/X_s))
senT_s=(1-cosT_s**2)**0.5
T_s=np.arctan(senT_s/cosT_s) 
c_s=(G*M_s*r)/(d_s**3)*(3*np.cos(T_s)**2-1)

c_ls=(c_s+c_l)*10000*1.17
print(c_l,c_s,c_ls)
