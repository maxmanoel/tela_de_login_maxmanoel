#importa as bibliotecas

from tkinter import* #importa todos os modulos do tkinder
from tkinter import messagebox #importa modulo de caixas de mensagem do tkinder
from tkinter import ttk #importa modulo widgets tematicos do tkinder
from DataBase import DataBase #importa a classe Database do modulo Database

#cria a janela 
jan = Tk() #cria uma instancia da janela principal 
jan.title("SL Sytens - Painel de acesso") #define o titulo da janela 
jan.geometry("600x300") # define o tamanho da janela 
jan.configure(background="white") #configura a cor de fundo da janela 
jan.resizable(width=False) #empede que a janela seja redimensionada 

#comando para deixar a tela transparente 
jan.attributes("-alpha", 0.9) #define a transparencia da janela (0.0 a 1.0)

#definir icone da janela 
jan.iconbitmap(default="icons/1LogoIcon.con") #define o icone da janela 


#carregar a imagem 
logo = PhotoImage(file="icons/Logosergio.png") #carrega a imagem da logo

#cria frame 
LeftFrame = Frame(jan, width=200, height=300,bg="MIDNIGHTBLUE",relief="raise") #cria uma frame a esquerda 
LeftFrame.pack(side=LEFT) #posiciona o frame a esquerda 
RightFrame.pack(side=RIGHT) #POSICIONA O FRAME A DIREITA

#ADICONA LOGO
LogoLabel = Label(LeftFrame, image=logo,bg="MIDNIGHTBLUE") #cria um label para imagem do logo 
LogoLabel.place(x=50,y=100) #posiciona o label no frame esquerdo

#adicona campos de usuario e senha 
UsuarioLabel = Label(RightFrame, text="Usuario: ", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") #cria um label para usuario 
UsuarioLabel.place(x=5, y=100) #posicona o label no frame direito

UsuarioEntry = ttk.Entry(RightFrame, width=30) #cria um campo de entrada para o usuario
UsuarioEntry.place(x=120, y=115) #posicona o campo de entrada 

SenhaLabel = Label(RightFrame, text= "Senha: ",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White") #cria um label para senha





