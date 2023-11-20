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

l_nome = Label(frame_baixo,text='Nome *',anchor=NW,font=('Ivy 10 '),bg=co1,fg=co4)
l_nome.place(x=10,y=20)

e_nome = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1,)
e_nome.place(x=80,y=20)


l_sexo = Label(frame_baixo,text='Sexo *',anchor=NW,font=('Ivy 10 '),bg=co1,fg=co4)
l_sexo.place(x=10,y=50)
c_sexo = Combobox(frame_baixo,width=27)
c_sexo.place(x=80,y=50)
c_sexo['value']=('','F','M')



l_tel = Label(frame_baixo,text='Telefone *',anchor=NW,font=('Ivy 10 '),bg=co1,fg=co4)
l_tel.place(x=10,y=80)
e_tel = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1,)
e_tel.place(x=80,y=80)

l_email = Label(frame_baixo,text='E-mail *',anchor=NW,font=('Ivy 10 '),bg=co1,fg=co4)
l_email.place(x=10,y=110)
e_email = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1,)
e_email.place(x=80,y=110)

b_procurar = Button(frame_baixo,text='Buscar',font=('Ivy 8 bold '),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_procurar.place(x=290,y=20)

e_procurar = Entry(frame_baixo,width=16,justify='left',font=('',11),highlightthickness=1,)
e_procurar.place(x=347,y=21)

b_ver = Button(frame_baixo,text='Ver dados',width=10,font=('Ivy 8 bold '),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_ver.place(x=290,y=50)

b_adicionar = Button(frame_baixo,text='Adicionar',width=10,font=('Ivy 8 bold '),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_adicionar.place(x=400,y=50)

b_atualizar = Button(frame_baixo,text='Atualizar',width=10,font=('Ivy 8 bold '),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_atualizar.place(x=400,y=80)

b_deletar = Button(frame_baixo,text='Deletar',width=10,font=('Ivy 8 bold '),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_deletar.place(x=400,y=110)

janela.mainloop()

