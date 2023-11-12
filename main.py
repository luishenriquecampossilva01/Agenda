from tkinter.ttk import *
from tkinter import*
from tkinter import messagebox



#cores

co0 = "#f0f3f5"
co1 = "#f0f3f5"
co2 = "#feffff"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#6f9fbd"
co6 = "#93cd95"

#criando janela 
janela = Tk()
janela.title("")
janela.geometry('500x450')
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style = Style(janela)
style.theme_use('clam')

#Frames

frame_cima = Frame(janela,width=500,height=50,bg=co3,relief='flat')
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=150,bg=co1,relief='flat')
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=248,bg=co2,relief='flat')
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)

#configurando frame_cima

l_nome = Label(frame_cima,text='Agenda Telefonica',anchor=NE,font=('Arial 20 bold'),bg=co3,fg=co1)
l_nome.place(x=5,y=5)

l_linha = Label(frame_cima,text='',width=500,anchor=NE,font=('Arial 1'),bg=co2,fg=co1)
l_linha.place(x=0,y=45)

janela.mainloop()

