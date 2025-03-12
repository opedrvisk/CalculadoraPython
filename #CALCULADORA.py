#CALCULADORA

from tkinter import *

def apertar(num):

    global resultado

    resultado = resultado + str(num)
    resultado_label.set(resultado)



def igual():
   
    global resultado

    try:

        total = str(eval(resultado))

        resultado_label.set(total)
 
        resultado = total

    except SyntaxError:

        resultado_label.set('erro de sintaxe!!')
    
        resultado = ''    
    
    except ZeroDivisionError:

        resultado_label.set('erro aritimético!!')
    
        resultado = ''


def apagar():

    global resultado

    resultado_label.set('')

    resultado = ''
    



window = Tk()
window.title('calculadora do pedrovisk')
window.geometry('500x500')

resultado = ''

resultado_label = StringVar()

label = Label(window,textvariable=resultado_label,font=('consolas',20), bg='white', width=24, height=2) 
label.pack()

frame = Frame(window)
frame.pack()

botao1 = Button(frame, text = 1, height=4, width=9, font=35,
                command=lambda: apertar(1))
botao1.grid(row=0, column=0)

botao2 = Button(frame,text = 2, height=4, width=9,font=35,
                command=lambda: apertar(2))
botao2.grid(row=0, column=1)

botao3 = Button(frame,text = 3, height=4, width=9,font=35,
                command=lambda: apertar(3))
botao3.grid(row=0, column=2)

botao4 = Button(frame,text = 4, height=4, width=9,font=35,
                command=lambda: apertar(4))
botao4.grid(row=1, column=0)

botao5 = Button(frame,text = 5, height=4, width=9,font=35,
                command=lambda: apertar(5))
botao5.grid(row=1, column=1)

botao6 = Button(frame,text = 6, height=4, width=9,font=35,
                command=lambda: apertar(6))
botao6.grid(row=1, column=2)

botao7 = Button(frame,text = 7, height=4, width=9,font=35,
                command=lambda: apertar(7))
botao7.grid(row=2, column=0)

botao8 = Button(frame,text = 8, height=4, width=9,font=35,
                command=lambda: apertar(8))
botao8.grid(row=2, column=1)

botao9 = Button(frame,text = 9, height=4, width=9,font=35,
                command=lambda: apertar(9))
botao9.grid(row=2, column=2)

botao0 = Button(frame,text = 0, height=4, width=9,font=35,
                command=lambda: apertar(0))
botao0.grid(row=3, column=0)

botaosoma = Button(frame,text = '+', height=4, width=9,font=35,
                command=lambda: apertar('+'))
botaosoma.grid(row=0, column=3)

botaosub = Button(frame,text = '-', height=4, width=9,font=35,
                command=lambda: apertar('-'))
botaosub.grid(row=1, column=3)

botaomulti = Button(frame,text = '*', height=4, width=9,font=35,
                command=lambda: apertar('*'))
botaomulti.grid(row=2, column=3)

botaodiv = Button(frame,text = '/', height=4, width=9,font=35,
                command=lambda: apertar('/'))
botaodiv.grid(row=3, column=3)

botaoigual = Button(frame,text = '=', height=4, width=9,font=35,
                command=igual)
botaoigual.grid(row=3, column=2)

botaodecimal = Button(frame,text = '.', height=4, width=9,font=35,
                command=lambda: apertar('.'))
botaodecimal.grid(row=3, column=1)

botaoapagar = Button(window,text='APAGAR',height=4,width=12,font=35,
                command= apagar)
botaoapagar.pack()



window.mainloop()
