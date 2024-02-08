from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


cor1 = "#36353b" #preto


#criando a janela

janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)


# dividindo a tela 

# parte de cima
frame_cima = Frame(janela, width=310, height=50, relief='flat')
frame_cima.grid(row=0, column=0, pady=1,padx=0,sticky=NSEW)


#parte de baixo

frame_baixo = Frame(janela, width=310, height=250, relief='flat' )
frame_baixo.grid(row=1, column=0, pady=1,padx=0,sticky=NSEW)


# configurando frame acima

l_nome = Label(frame_cima, text='LOGIN',anchor=NE, font=('Ivy 25'),  fg=cor1)
l_nome.place(x=5,y=5)




credenciais = ['admin', '123456']



# verificar senha


def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome =='admin' and senha == 'admin':

         
        messagebox.showinfo('Seja bem vindo')
    elif credenciais[0] == nome and credenciais[1] == senha:
         
         messagebox.showinfo('Seja bem vindo '+ credenciais[0])


    # deletar itens presentes
         for widget in frame_baixo.winfo_children():
            widget.destroy()
         for widget in frame_cima.winfo_children():
            widget.destroy() 
        
         nova_janela()      

    else:
        messagebox.showwarning('Nome ou senha incorreto!')
           

#funcção apos verificação
        
def nova_janela():
    l_nome = Label(frame_cima, text='Usuario :'+ credenciais[0],anchor=NE, font=('Ivy 20'),  fg=cor1)
    l_nome.place(x=5,y=5)

    l_linha = Label(frame_cima, text='',width=275, anchor=NW, font=('Ivy 1'),  bg=cor5)
    l_linha.place(x=10,y=45)

    l_nome = Label(frame_baixo, text='Seja bem vindo :'+ credenciais[0],anchor=NE, font=('Ivy 20'),  fg=cor1)
    l_nome.place(x=5,y=130)



# configurando frame baixo

l_nome = Label(frame_baixo, text='Nome *',anchor=NW, font=('Ivy 10'),  fg=cor1)
l_nome.place(x=10,y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("",15),highlightthickness=1, relief='solid')
e_nome.place(x=14,y=50)



l_pass = Label(frame_baixo, text='Senha *',anchor=NW, font=('Ivy 10'),  fg=cor1)
l_pass.place(x=10,y=95)
e_pass = Entry(frame_baixo, width=25, justify='left',show='*', font=("",15),highlightthickness=1, relief='solid')
e_pass.place(x=14,y=130)



b_confimar = Button(frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, font=('Ivy 9'),  fg=cor1,relief=RAISED)
b_confimar.place(x=15,y=180)



janela.mainloop()