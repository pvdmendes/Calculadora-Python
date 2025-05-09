from tkinter import *
from tkinter import ttk

# cores
cor1 = "#feffff"  # white/branca
cor2 = "#38576b"  
cor3 ="#272963"
cor4="#FFAB40" # Orange/laranja
cor5="#ECEFF1"

fundo = "#3b3b3b" # black/preta

#Frames
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#varaiavel todos_valores
todos_valores= ''


#criando funcao
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    
    #passando valor para tela
    valor_texto.set(todos_valores)
#Função de calcular
def calcular():
    global todos_valores    
    resultado= eval(todos_valores)
    valor_texto.set(resultado)
    
#Função de deletar 
def limpar_tela():
    global todos_valores

    todos_valores= ""
    valor_texto.set("") 



#Criando Label
valor_texto = StringVar()

app_label= Label (frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e',justify=RIGHT, font=('Ivy 18'), bg=cor2, fg=cor1)
app_label.place(x=0, y=0)





#criando botoes
b1= Button(frame_corpo,command=limpar_tela, text= "C", width=11, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2= Button(frame_corpo,command=lambda: entrar_valores('%'), text= "%", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3= Button(frame_corpo,command=lambda: entrar_valores('/'), text= "/", width=5, height=2, bg=cor4,fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)



b4= Button(frame_corpo,command=lambda: entrar_valores('7'), text= "7", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5= Button(frame_corpo,command=lambda: entrar_valores('8'), text= "8", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6= Button(frame_corpo,command=lambda: entrar_valores('9'), text= "9", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7= Button(frame_corpo,command=lambda: entrar_valores('*'), text= "*", width=5, height=2, bg=cor4,fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)


b8= Button(frame_corpo,command=lambda: entrar_valores('6'), text= "6", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9= Button(frame_corpo,command=lambda: entrar_valores('5'), text= "5", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10= Button(frame_corpo,command=lambda: entrar_valores('4'), text= "4", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11= Button(frame_corpo,command=lambda: entrar_valores('-'), text= "-", width=5, height=2, bg=cor4,fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)

b12= Button(frame_corpo,command=lambda: entrar_valores('1'), text= "1", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13= Button(frame_corpo,command=lambda: entrar_valores('2'), text= "2", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14= Button(frame_corpo,command=lambda: entrar_valores('3'), text= "3", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15= Button(frame_corpo,command=lambda: entrar_valores('+'), text= "+", width=5, height=2, bg=cor4,fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

b16= Button(frame_corpo,command=lambda: entrar_valores('0'), text= "0", width=11, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17= Button(frame_corpo,command=lambda: entrar_valores('.'), text= ".", width=5, height=2, bg=cor5, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18= Button(frame_corpo,command=calcular, text= "=", width=5, height=2, bg=cor4,fg=cor1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)






janela.mainloop()


