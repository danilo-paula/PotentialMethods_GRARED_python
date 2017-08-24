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



