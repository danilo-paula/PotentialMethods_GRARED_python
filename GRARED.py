# -*- coding: utf-8 -*-

#--------------------------------------------------
#Import das bibliotecas
#--------------------------------------------------
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from tkinter import *

#--------------------------------------------------
#Ambiente Tkinter
#--------------------------------------------------
class Packing:
    def __init__(self, toplevel):
        self.frame=Frame(toplevel).grid()

        
        #Variáveis de entrada      
        self.var_tipo=StringVar(toplevel)
        self.var_tipo.set('excel')
        self.var_aba=StringVar(toplevel)
        self.var_aba.set('Plan1')
        self.var_entrada=StringVar(toplevel)
        self.var_entrada.set('GRARED_P_exemplo.xlsx')
        self.var_conv=StringVar(toplevel)
        self.var_conv.set('Tab_conv_G996.txt')

        self.var_dia=DoubleVar(toplevel)
        self.var_dia.set(int(1))
        self.var_mes=DoubleVar(toplevel)
        self.var_mes.set(int(1))
        self.var_ano=DoubleVar(toplevel)
        self.var_ano.set(int(2017))
        self.var_fuso_horario=DoubleVar(toplevel)
        self.var_fuso_horario.set(int(-3))
        self.var_densidade=DoubleVar(toplevel)
        self.var_densidade.set(float(2.67))
        self.var_fator_grav=DoubleVar(toplevel)
        self.var_fator_grav.set(float(1.20))
        self.var_acel_absoluta=DoubleVar(toplevel)

        self.var_free_air=IntVar(toplevel)
        self.var_free_air.set(int(1))
        self.var_bouguer=IntVar(toplevel)
        self.var_bouguer.set(int(1))
        self.var_patm=IntVar(toplevel)
        self.var_patm.set(int(1))

        self.var_elipsoide=StringVar(toplevel)
        self.var_elipsoide.set('grs84')

        self.var_saida_txt=StringVar(toplevel)
        self.var_saida_txt.set('dados_reduzidos.dat')
        self.var_saida_excel=StringVar(toplevel)
        self.var_saida_excel.set('dados_reduzidos.xlsx')

        #ENTRADA DE DADOS
        #*******************************************************************************
        self.T_entrada_de_dados=Label(self.frame,font=('Arial','10','bold','underline'),
                                     text='Entrada de dados')
        self.T_entrada_de_dados.grid(row=0,column=11,columnspan=9,sticky=S,pady=27)
        
        self.T_tipo_arquivo_entrada=Label(self.frame,font=('Arial','10','bold'),
                          text='Tipo de Arquivo: ')
        self.T_tipo_arquivo_entrada.grid(row=1,column=0,columnspan=4,rowspan=2,sticky=E)
        def muda_valor_aba_excel():
            self.var_aba.set('Plan1')
            self.var_entrada.set('GRARED_P_exemplo.xlsx')
        def muda_valor_aba_txt():
            self.var_aba.set('-------------Não Há--------------')
            self.var_entrada.set('GRARED_P_exemplo.txt')
        self.RB_excel=Radiobutton(self.frame, text='Excel', value='excel', variable=self.var_tipo, command=muda_valor_aba_excel)
        self.RB_excel.grid(row=1,column=4,columnspan=4,sticky=W)
        self.RB_txt=Radiobutton(self.frame, text='DAT/TXT', value='txt', variable=self.var_tipo, command=muda_valor_aba_txt)
        self.RB_txt.grid(row=2,column=4,columnspan=4,sticky=W)
        self.T_entrada=Label(self.frame, font=('Arial','10','bold'), text='Arquivo de dados:')
        self.T_entrada.grid(row=1,column=8,columnspan=4,sticky=E)
        self.E_entrada=Entry(self.frame, width=30,textvar=self.var_entrada)
        self.E_entrada.grid(row=1,column=12,columnspan=6,sticky=W)
        self.T_aba=Label(self.frame, font=('Arial','10','bold'), text='Se excel, qual aba?')
        self.T_aba.grid(row=2,column=8,columnspan=4,sticky=E)
        self.E_aba=Entry(self.frame, width=30,textvar=self.var_aba)
        self.E_aba.grid(row=2,column=12,columnspan=6,sticky=W)
  
        self.T_conv=Label(self.frame, font=('Arial','10','bold'), text='    Tabela de Conversão:')
        self.T_conv.grid(row=1,column=18,columnspan=4,rowspan=2,sticky=E)
        self.E_conv=Entry(self.frame, width=30,textvar=self.var_conv)
        self.E_conv.grid(row=1,column=22,columnspan=6,rowspan=2,sticky=E,padx=15)

        #DADOS DO LEVANTAMENTO
        #********************************************************************
        self.T_dados_do_l=Label(self.frame,font=('Arial','10','bold','underline'),
                        text='Dados do levantamento')
        self.T_dados_do_l.grid(row=3,column=11,columnspan=9,sticky=S,pady=27)
        #Dia
        self.T_dia=Label(self.frame,font=('Arial','10','bold'),
                        text='Dia')
        self.T_dia.grid(row=4,column=2,rowspan=2)
        self.E_dia=Entry(self.frame, width=4, textvar=self.var_dia)
        self.E_dia.grid(row=6,column=2)

        #Mes
        self.T_mes=Label(self.frame,font=('Arial','10','bold'),
                        text='Mês')
        self.T_mes.grid(row=4,column=3,rowspan=2)
        self.E_mes=Entry(self.frame, width=4, textvar=self.var_mes)
        self.E_mes.grid(row=6,column=3)

        #Ano
        self.T_ano=Label(self.frame,font=('Arial','10','bold'),
                        text='Ano')
        self.T_ano.grid(row=4,column=4,columnspan=2,rowspan=2)
        self.E_ano=Entry(self.frame, width=6, textvar=self.var_ano)
        self.E_ano.grid(row=6,column=4,columnspan=2)

        #Fuso-Horário
        self.T_fuso=Label(self.frame,font=('Arial','10','bold'),
                        text='Fuso')
        self.T_fuso.grid(row=4,column=8,columnspan=2)
        self.T_horario=Label(self.frame,font=('Arial','10','bold'),
                        text='Horário')
        self.T_horario.grid(row=5,column=8,columnspan=2)
        self.E_fuso_horario=Entry(self.frame, width=5, textvar=self.var_fuso_horario)
        self.E_fuso_horario.grid(row=6,column=8,sticky=E)

        #Densidade crustal local
        self.T_densidade=Label(self.frame,font=('Arial','10','bold'),
                        text='Densidade')
        self.T_densidade.grid(row=4,column=11,columnspan=3)
        self.T_crustal=Label(self.frame,font=('Arial','10','bold'),
                        text='Crust. (cgs)')
        self.T_crustal.grid(row=5,column=11,columnspan=3)
        self.E_densidade=Entry(self.frame, width=6, textvar=self.var_densidade)
        self.E_densidade.grid(row=6,column=11,columnspan=3)

        #Fator Gravimétrico
        self.T_fator=Label(self.frame,font=('Arial','10','bold'),
                        text='Fator')
        self.T_fator.grid(row=4,column=15,columnspan=3)
        self.T_grav=Label(self.frame,font=('Arial','10','bold'),
                        text='Gravimétrico')
        self.T_grav.grid(row=5,column=15,columnspan=3)
        self.E_fator_grav=Entry(self.frame, width=6, textvar=self.var_fator_grav)
        self.E_fator_grav.grid(row=6,column=15,columnspan=3)

        #Aceleração grav. absoluta da Primeira estação
        self.T_acel_absoluta=Label(self.frame,font=('Arial','10','bold'),
                        text='Aceleração grav. absoluta da Primeira estação (mGal)')
        self.T_acel_absoluta.grid(row=4,column=19,columnspan=9,rowspan=2, padx=10)
        self.E_acel_absoluta=Entry(self.frame, textvar=self.var_acel_absoluta)
        self.E_acel_absoluta.grid(row=6,column=19,columnspan=9)

        #ESCOLHA DAS CORREÇÕES
        #********************************************************************
        self.T_edas=Label(self.frame,font=('Arial','10','bold','underline'),
                        text='Escolha das correções')
        self.T_edas.grid(row=7,column=11,columnspan=9,sticky=S,pady=27)

        self.CB_free_air=Checkbutton(text='Free-Air', var=self.var_free_air)
        self.CB_free_air.grid(row=8,column=7,columnspan=4,sticky=N,pady=15)
        self.CB_bouguer=Checkbutton(text='Bouguer Simples', var=self.var_bouguer)
        self.CB_bouguer.grid(row=8,column=12,columnspan=5,sticky=N,pady=15)
        self.CB_patm=Checkbutton(text='Presão Atmosférica', var=self.var_patm)
        self.CB_patm.grid(row=8,column=18,columnspan=5,sticky=N,pady=15)             

        self.T_elipsoide=Label(self.frame, font=('Arial','10','bold'), text='Elipsoide de referência:')
        self.T_elipsoide.grid(row=9,column=8,columnspan=6)
        self.RB_grs67=Radiobutton(self.frame, text='GRS67', value='grs67', variable=self.var_elipsoide)
        self.RB_grs67.grid(row=9,column=13,columnspan=3)
        self.RB_grs80=Radiobutton(self.frame, text='GRS80', value='grs80', variable=self.var_elipsoide)
        self.RB_grs80.grid(row=9,column=17,columnspan=3)
        self.RB_grs84=Radiobutton(self.frame, text='GRS84', value='grs84', variable=self.var_elipsoide)
        self.RB_grs84.grid(row=9,column=21,columnspan=3)

        #SAÍDA DOS DADOS
        #********************************************************************        
        self.T_erdas=Label(self.frame,font=('Arial','10','bold','underline'),
                        text='Saída de dados')
        self.T_erdas.grid(row=10,column=11,columnspan=9,sticky=S,pady=27)

        self.T_saida_txt=Label(self.frame, font=('Arial','10','bold'),text='Saída DAT/TXT:')
        self.T_saida_txt.grid(row=11,column=5, columnspan=3)
        self.E_saida_txt=Entry(self.frame, width=30,textvar=self.var_saida_txt)
        self.E_saida_txt.grid(row=11,column=8, columnspan=6)
        self.T_saida_excel=Label(self.frame, font=('Arial','10','bold'),text='Saída Excel:')
        self.T_saida_excel.grid(row=11,column=15, columnspan=3)
        self.E_saida_excel=Entry(self.frame, width=30,textvar=self.var_saida_excel)
        self.E_saida_excel.grid(row=11,column=18, columnspan=6)
            #_______________________________________
            #_______________________________________        
        def gerar_saida():
            #Captura das informações da GUI
            tipo_arquivo=self.var_tipo.get()
            aba=self.var_aba.get()
            nome_arquivo=self.E_entrada.get()
            planilha_conv=self.var_conv.get()

            dia=float(self.E_dia.get())
            mes=float(self.E_mes.get())
            ano=float(self.E_ano.get())
            fuso_horario=float(self.E_fuso_horario.get())
            densidade=float(self.E_densidade.get())
            fator_grav=float(self.E_fator_grav.get())
            g_ref=float(self.E_acel_absoluta.get())

            wx_free_air=int(self.var_free_air.get())
            wx_bouguer=int(self.var_bouguer.get())
            wx_patm=int(self.var_patm.get())
            elipsoide=self.var_elipsoide.get()
            
            saida_txt=self.E_saida_txt.get()
            saida_excel=self.E_saida_excel.get()

            
            #Importação condicional da tabela de dados
            if tipo_arquivo=='excel':
                planilha_entrada=nome_arquivo 

                p_mat_ler = pd.read_excel(planilha_entrada, sheetname=aba,header=None,skiprows=2,dtype=float) #Leitura interna da planilha
                p_matriz=p_mat_ler.values.T #Salvamento da planilha lida em matriz transposta de arrays

                ponto = p_matriz[0]#Identificador do ponto
                g_l1= p_matriz[1]#Primeira Leitura
                g_l2= p_matriz[2]#Segunda Leitura
                g_l3= p_matriz[3]#Terceira Leitura

                hora = p_matriz[3]#Hora Local da leitura
                minuto = p_matriz[4]#Minuto Local da leitura

                h_instrumento=p_matriz[5]

                Lat_gra = p_matriz[6]#Latitude Graus
                Lat_min = p_matriz[7]#Latitude Minutos
                Lat_seg = p_matriz[8]#Latitude segundos

                Lon_gra = p_matriz[9]#Longitude Graus
                Lon_min = p_matriz[10]#Longitude Minutos
                Lon_seg = p_matriz[11]#Longitude segundos
    
                alt_m = p_matriz[12]#Altitude geométrica obtida pelos receptores GNSS em metros

                p_atm_kpa = p_matriz[13]#Pressão atmosférica em kPa
                
            elif tipo_arquivo=='txt':
                planilha_entrada=nome_arquivo
                ponto,g_l1,g_l2,g_l3,hora,minuto,h_instrumento,Lat_gra,Lat_min,Lat_seg,Lon_gra,Lon_min,Lon_seg,alt_m,p_atm_kpa=np.loadtxt(planilha_entrada, skiprows=1,unpack=True)


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
            
        #Correções e Transformações importantes
        #--------------------------------------------------
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
                
            #Correção de maré (A ser implementado)#########################
            ####################################################################
            clsa=0
            g_cls=g_conv+clsa
            cls=np.zeros(len(ponto))
            ####################################################################
            
            #Correção de Altura Instrumental
            c_ai=0.308596*h_instrumento
            g_ai=g_cls+c_ai
            
            #Correção da deriva instrumental
            delta_t=np.zeros(1)
            contador2=int(1)
            while len(delta_t)!=len(hora_dec):
                dt=hora_dec[contador2]-hora_dec[0]
                delta_t=np.append(delta_t,dt)
                contador2=contador2+1 
            if ponto[0] == ponto[-1]:
                delta_t[-1]=hora_dec[-1]-hora_dec[0]
                delta_g=g_ai[-1]-g_ai[0]
                cd=(-delta_g/delta_t[-1])*delta_t
                g_cd=g_ai+cd
                
            #Cálculo de Aceleração lida absoluta
            g_abs=g_ref+(g_cd-g_cd[0])

            #Acelerações teóricas
            if elipsoide=='grs67':
                #Cálculo de Aceleração do GRS67
                g_teor=978031.8*(1+0.0053024*((np.sin(Lat_rad))**2)-0.0000059*((np.sin(2*Lat_rad))**2))
            elif elipsoide=='grs80':
                #Cálculo de Aceleração do GRS80
                g_teor=978032.7*(1+0.0053024*((np.sin(Lat_rad))**2)-0.0000058*((np.sin(2*Lat_rad))**2))
            elif elipsoide=='grs84':
            #Cálculo de Aceleração do GRS84
                g_teor=(9.7803267714*((1+0.00193185138639*((np.sin(Lat_rad))**2))/((1-0.00669437999013*((np.sin(Lat_rad))**2)**(1/2)))))*(100000)
            
            #Correção Bouguer Simples
            if wx_bouguer==0:
                cb=np.zeros(len(ponto))
            elif wx_bouguer==1:
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
            if wx_free_air==0:
                ca=np.zeros(len(ponto))
            elif wx_free_air==1:
                ca=0.308596*alt_m
        
            #Correção de Pressão atmosférica
            if wx_patm==0:
                catm=np.zeros(len(ponto))
            elif wx_patm==1:
                catm=-0.036*p_atm_kpa

            #Cálculo de redução
            g_abs_corr=g_abs+ca+cb+catm
            red=g_abs_corr-g_teor
                
        #Sáida dos dados
        #--------------------------------------------------
            #Excel
            df_pt1=pd.DataFrame({'Ponto':ponto})
            df_pt2=pd.DataFrame({'Leitura média Gravímetro':g_med_lido})
            df_pt3=pd.DataFrame({'Leitura média covertida p/ mGal':g_conv})
            df_pt4=pd.DataFrame({'Correção de Maré':cls})
            df_pt5=pd.DataFrame({'Correção de Altura instrumental':c_ai})            
            df_pt6=pd.DataFrame({'Correção Deriva':cd})
            df_pt7=pd.DataFrame({'Acel. corr. Deriva, Maré e Alt. Instr.':g_cd}) 
            df_pt8=pd.DataFrame({'Correção Free-air':ca})
            df_pt9=pd.DataFrame({'Correção Boug. S.':cb})
            df_pt10=pd.DataFrame({'Correção P. Atm':catm})
            df_pt11=pd.DataFrame({'Acel. corr. Completa':g_abs_corr})
            df_pt12=pd.DataFrame({'Aceleração Teórica':g_teor})
            df_pt13=pd.DataFrame({'Anomalia Grav, Remoção efeitos Lat':red})
            excel_writer=ExcelWriter(saida_excel)
            cont_df=0
            for df in (df_pt1,df_pt2, df_pt3, df_pt4,df_pt5,df_pt6,df_pt7,df_pt8,df_pt9,df_pt10,df_pt11,df_pt12,df_pt13):
                df.to_excel(excel_writer, sheet_name='Plan1', startcol=cont_df,index=False)
                cont_df=cont_df+1
            excel_writer.save()
            #DAT/TXT
            qmm1=['       ']
            qmm=pd.DataFrame({'       ':qmm1})
            for df2 in (df_pt1, qmm,df_pt2, qmm,df_pt3, qmm,df_pt4,  qmm,df_pt5,  qmm,df_pt6,  qmm,df_pt7,  qmm,df_pt8,  qmm,df_pt9,  qmm,df_pt10,  qmm,df_pt11,  qmm,df_pt12,  qmm,df_pt13):
                df2.to_csv(saida_txt, header=True, index=False, mode='a')
            #_______________________________________
            #_______________________________________            
        self.B_entrada_import=Button(text='Reduzir Dados e Gerar Arquivos',command=gerar_saida)
        self.B_entrada_import.grid(row=12,column=11,columnspan=9,pady=20)

        self.T_autoria=Label(self.frame, font=('Times New Roman','7','bold','italic'),foreground="gray",
                             text='Programa  por  Danilo  de  Paula (danilo_p@usp.br),  do  GEOLIT-IAG-USP')
        self.T_autoria.grid(row=13,column=0,columnspan=11,sticky=W)


raiz=Tk()
raiz.wm_title("GRARED   v.Alpha 0.3")
raiz.geometry("+10+10")
Packing(raiz)
raiz.mainloop()
