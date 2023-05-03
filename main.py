from tkinter import *
from tkinter import scrolledtext
from tkinter import Tk, StringVar, ttk
import tkinter.font as tkFont
from tkinter import messagebox


################# tkcalendar ###############
from tkcalendar import Calendar, DateEntry
from datetime import date

################ importando view ######

from view import *



################# cores ###############

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

################# criando janela ###############

janela = Tk ()
janela.title ("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


################# Frames ####################

frameCima = Frame(janela, width=310, height=50, bg=co2,  relief="flat",)
frameCima.grid(row=0, column=0)

frameBaixo = Frame(janela,width=310, height=403,bg=co1, relief="flat")
frameBaixo.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameDireita = Frame(janela,width=588, height=403,bg=co1, relief="flat")
frameDireita.grid(row=0, column=1,rowspan=2, pady=0, padx=1, sticky=NSEW)


app_ = Label(frameCima, text="Formulário de Consultoria", anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1)
app_.place(x=10,y=20)

global tree

# funcao inserir

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    dia = cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()
    
    lista_inserir = [nome, email, telefone, dia, estado, assunto]
    
    if e_nome.get()=='':
        messagebox.showerror('Erro', 'Preencha todos os campos')
    else:
        inserir_form(lista_inserir)

        messagebox.showinfo(
            'Sucesso', 'Os dados foram inseridos com sucesso')
        
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        
        for widget in frameDireita.winfo_children():
            widget.destroy()

        mostrar()


# funcao atualizar

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        cal.delete(0, 'end')
        e_estado.delete(0, 'end')
        e_assunto.delete(0, 'end')
        
        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_tel.insert(0, treev_lista[3])
        cal.insert(0, treev_lista[4])
        e_estado.insert(0, treev_lista[5])
        e_assunto.insert(0, treev_lista[6])
        
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_tel.get()
            dia = cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()
            
            lista_atualizar = [nome, email, telefone, dia, estado, assunto, valor]
            
            if e_nome.get()=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
            else:
                atualizar_form(lista_atualizar)

                messagebox.showinfo(
                    'Sucesso', 'Os dados foram atualizados com sucesso')
                
                e_nome.delete(0, 'end')
                e_email.delete(0, 'end')
                e_tel.delete(0, 'end')
                cal.delete(0, 'end')
                e_estado.delete(0, 'end')
                e_assunto.delete(0, 'end')
                
                botao_confirmar.destroy()
                
                for widget in frameDireita.winfo_children():
                    widget.destroy()

                mostrar()
        botao_confirmar = Button(frameBaixo, command=update, text="Confirmar", width=10, height=1, bg=co2, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
        botao_confirmar.place(x=105, y=380)
 

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela')
        
    

# funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        
        deletar_form([valor])
        print(valor)
        
        messagebox.showinfo(
            'Sucesso', 'Os dados foram deletados com sucesso')


        for widget in frameDireita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror(
            'Erro', 'Seleciona um dos dados na tabela')




l_nome = Label(frameBaixo, text="Nome *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameBaixo, width=45, justify='left',relief="solid")
e_nome.place(x=15, y=40)

l_email = Label(frameBaixo, text="email *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_email.place(x=10, y=70)
e_email = Entry(frameBaixo, width=45, justify='left',relief="solid")
e_email.place(x=15, y=100)

l_tel = Label(frameBaixo, text="telefone *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_tel.place(x=10, y=130)
e_tel = Entry(frameBaixo, width=45, justify='left',relief="solid")
e_tel.place(x=15, y=160)

l_cal = Label(frameBaixo, text="Data da consulta *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=190)
cal = DateEntry(frameBaixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
cal.place(x=15, y=220)

l_estado = Label(frameBaixo, text="Estado da consulta *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_estado.place(x=160, y=190)
e_estado  = Entry(frameBaixo, width=20, justify='left',relief="solid")
e_estado.place(x=160, y=220)

l_assunto = Label(frameBaixo, text="Consulta sobre *", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_assunto.place(x=10, y=260)
e_assunto = Entry(frameBaixo, width=45, justify='left',relief="solid")
e_assunto.place(x=15, y=290)


botao_inserir = Button(frameBaixo, command=inserir, text="Inserir", width=10, height=1, bg=co6, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
botao_inserir.place(x=15, y=340)

botao_atualizar = Button(frameBaixo, command=atualizar, text="Atualizar", width=10, height=1, bg=co2, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
botao_atualizar.place(x=105, y=340)

botao_deletar = Button(frameBaixo, command=deletar, text="Deletar", width=10, height=1, bg=co7, fg=co1, font=('Ivy 7 bold'), relief=RAISED, overrelief=RIDGE)
botao_deletar.place(x=190, y=340)


################# frame tree ####################

# funcao para mostrar
def mostrar():

    # creating a treeview with dual scrollbars
    list_header = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']

    df_list = selecionar_form()
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(
        frameDireita, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(
        frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in df_list:
        tree.insert('', 'end', values=item)
        
    

mostrar()
    


janela.mainloop ()