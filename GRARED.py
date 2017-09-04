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
class Packing:
    def __init__(self, toplevel):
        self.frame=Frame(toplevel).grid()


        #ENTRADA DE DADOS
        #*******************************************************************************
        self.T_entrada_de_dados=Label(self.frame,font=('Arial','10','bold','underline'),
                                     text='Entrada de dados')
        self.T_entrada_de_dados.grid(row=0,column=11,columnspan=9,sticky=S,pady=27)
        
        self.T_tipo_arquivo_entrada=Label(self.frame,font=('Arial','10','bold'),
                          text='Tipo de Arquivo: ')
        self.T_tipo_arquivo_entrada.grid(row=1,column=0,columnspan=4,rowspan=2,sticky=E)
        self.var_tipo=StringVar(toplevel)
        self.var_tipo.set('excel')
        self.RB_excel=Radiobutton(self.frame, text='Excel', value='excel', variable=self.var_tipo)
        self.RB_excel.grid(row=1,column=4,columnspan=4,sticky=W)
        self.RB_txt=Radiobutton(self.frame, text='TXT Tabulado', value='txt', variable=self.var_tipo)
        self.RB_txt.grid(row=2,column=4,columnspan=4,sticky=W)
        
        self.T_entrada=Label(self.frame, font=('Arial','10','bold'), text='Arquivo de dados:')
        self.T_entrada.grid(row=1,column=8,columnspan=4,rowspan=2,sticky=E)
        self.var_entrada=StringVar(toplevel)
        self.var_entrada.set('GRARED_P_exemplo.xlsx')
        self.E_entrada=Entry(self.frame, width=30,textvar=self.var_entrada)
        self.E_entrada.grid(row=1,column=12,columnspan=6,rowspan=2,sticky=W)
        
        self.T_conv=Label(self.frame, font=('Arial','10','bold'), text='Tabela de Conversão:')
        self.T_conv.grid(row=1,column=18,columnspan=4,rowspan=2,sticky=E)
        self.var_conv=StringVar(toplevel)
        self.var_conv.set('Tab_conv_G996.txt')
        self.E_conv=Entry(self.frame, width=30,textvar=self.var_conv)
        self.E_conv.grid(row=1,column=22,columnspan=6,rowspan=2,sticky=E,padx=15)

        #Variáveis gerais
        #********************************************************************
        self.T_dados_do_l=Label(self.frame,font=('Arial','10','bold','underline'),
                        text='Dados do levantamento')
        self.T_dados_do_l.grid(row=3,column=11,columnspan=9,sticky=S,pady=27)
        #Dia
        self.T_dia=Label(self.frame,font=('Arial','10','bold'),
                        text='Dia')
        self.T_dia.grid(row=4,column=2,rowspan=2)
        self.var_dia=DoubleVar(toplevel)
        self.var_dia.set(int(1))
        self.E_dia=Entry(self.frame, width=4, textvar=self.var_dia)
        self.E_dia.grid(row=6,column=2)

        #Mes
        self.T_mes=Label(self.frame,font=('Arial','10','bold'),
                        text='Mês')
        self.T_mes.grid(row=4,column=3,rowspan=2)
        self.var_mes=DoubleVar(toplevel)
        self.var_mes.set(int(1))
        self.E_mes=Entry(self.frame, width=4, textvar=self.var_mes)
        self.E_mes.grid(row=6,column=3)

        #Ano
        self.T_ano=Label(self.frame,font=('Arial','10','bold'),
                        text='Ano')
        self.T_ano.grid(row=4,column=4,columnspan=2,rowspan=2)
        self.var_ano=DoubleVar(toplevel)
        self.var_ano.set(int(2017))
        self.E_ano=Entry(self.frame, width=6, textvar=self.var_ano)
        self.E_ano.grid(row=6,column=4,columnspan=2)

        #Fuso-Horário
        self.T_fuso=Label(self.frame,font=('Arial','10','bold'),
                        text='Fuso')
        self.T_fuso.grid(row=4,column=8,columnspan=2)
        self.T_horario=Label(self.frame,font=('Arial','10','bold'),
                        text='Horário')
        self.T_horario.grid(row=5,column=8,columnspan=2)
        self.var_fuso_horario=DoubleVar(toplevel)
        self.var_fuso_horario.set(int(-3))
        self.E_fuso_horario=Entry(self.frame, width=4, textvar=self.var_fuso_horario)
        self.E_fuso_horario.grid(row=6,column=8,rowspan=2,sticky=E)
        
        
        def gerar_saida():
            tipo_arquivo=self.var_tipo.get()
            nome_arquivo=self.E_entrada.get()
            planilha_conv=self.var_conv.get()

            dia=float(self.E_dia.get())
            mes=float(self.E_mes.get())
            ano=float(self.E_ano.get())
            fuso_horario=float(self.E_fuso_horario.get())
            densidade=2.67
            fator_grav=1.20
            acel_primeira_est=980788.312

            #_______________________________________
            #_______________________________________
            if tipo_arquivo=='excel':
                planilha_entrada=nome_arquivo 

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
            elif tipo_arquivo=='txt':
                planilha_entrada=nome_arquivo
                ponto,g_l1,g_l2,g_l3,Lat_gra,Lat_min,Lat_seg,Lon_gra,Lon_min,Lon_seg,alt_m,hora,minuto,p_atm_kpa=np.loadtxt(planilha_entrada, skiprows=1,unpack=True)


            gc1,gc2,gf0=np.loadtxt(planilha_conv,skiprows=1,unpack=True)
            
        #Conversões e cálculos preliminares
        #--------------------------------------------------
            Lat_graus_dec = Lat_gra+(Lat_min/60)+(Lat_seg/3600) #Latitude em Graus decimais
            Lat_rad=np.radians(Lat_graus_dec) #Latitude em radianos

            Lon_graus_dec = Lon_gra+(Lon_min/60)+(Lon_seg/3600) #Longitude em Graus decimais
            Lon_rad=np.radians(Lon_graus_dec) #Longitude em radianos

            alt_cm = alt_m*100 #Altitude geométrica obtida pelos receptores GNSS em centimetros

            hora_dec=(hora)+(minuto/(60))
            hora_utc=(hora-fuso_horario)
            
            #Cálculo de Séculos Julianos à partir de 31/dez/1899
            dia_c=dia+(hora_utc/24)+(minuto/(60*24))
            jd_inicial=(1461*(1899+4800+(12-14)/12))/4+(367*(12-2-12*(( 12-14)/12)))/12-(3*((1899+4900+(12-14)/12)/100))/4+31-32075
            jd =(1461*(ano+4800+(mes-14)/12))/4+(367*(mes-2-12*(( mes-14)/12)))/12-(3*((ano+4900+(mes-14)/12)/100))/4+dia_c-32075
            jc=((jd-jd_inicial)*24*60)/52596000

            #Conversão de acel. Grav. instrumental para mGal
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

                
        #Correções e Transformações importantes
        #--------------------------------------------------
            #Cálculo de Aceleração do GRS67
            g_teor67=978031.8*(1+0.0053024*((np.sin(Lat_rad))**2)-0.0000059*((np.sin(2*Lat_rad))**2))

            #Cálculo de Aceleração do GRS80
            g_teor80=978032.7*(1+0.0053024*((np.sin(Lat_rad))**2)-0.0000058*((np.sin(2*Lat_rad))**2))

            #Cálculo de Aceleração do GRS84
            g_teor84=(9.7803267714*((1+0.00193185138639*((np.sin(Lat_rad))**2))/((1-0.00669437999013*((np.sin(Lat_rad))**2)**(1/2)))))*(100000)

            #Correção da deriva instrumental
            delta_t=np.zeros(1)
            contador2=int(1)
            while len(delta_t)!=len(hora_dec):
                dt=hora_dec[contador2]-hora_dec[0]
                delta_t=np.append(delta_t,dt)
                contador2=contador2+1 
            if ponto[0] == ponto[-1]:
                delta_t[-1]=hora_dec[-1]-hora_dec[0]
                delta_g=g_conv[-1]-g_conv[0]
                cd=(-delta_g/delta_t[-1])*delta_t

            #Correção Bouguer Simples
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
            ca=0.3086*alt_m

            
            print(g_conv+ca+cb+cd)
            #_______________________________________
            #_______________________________________            
        self.B_entrada_import=Button(text='Reduzir Dados e exportar para arquivos',command=gerar_saida)
        self.B_entrada_import.grid(row=11,column=11,columnspan=9)


raiz=Tk()
Packing(raiz)
raiz.mainloop()
