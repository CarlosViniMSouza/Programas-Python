from tkinter import *
class Fatias:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width=200, height=200)
        self.canvas.pack()
        self.frame = Frame(raiz)
        self.frame.pack()
        self.altura = 200  # Altura do canvas
        self.canvas.create_oval(25, self.altura - 25, 175,
                                self.altura - 175,
                                fill='deepskyblue', outline='blue')
        fonte = ('Comic Sans MS', '14', 'bold')
        Label(self.frame, text='Fatia: ', font=fonte, fg='yellow').pack(side=LEFT)
        self.porcentagem = Entry(self.frame, fg='red',
                                 font=fonte, width=5)
        self.porcentagem.focus_force()
        self.porcentagem.pack(side=LEFT)

        Label(self.frame, text='%', font=fonte, fg='green').pack(side=LEFT)
        self.botao = Button(self.frame, text='Desenhar',
                            command=self.cortar, font=fonte,
                            fg='darkblue', bg='deepskyblue')
        self.botao.pack(side=LEFT)

    def cortar(self):
        arco = self.canvas.create_arc
        fatia = float(self.porcentagem.get()) * 359.9 / 100.
        arco(25, self.altura - 25,
            175, self.altura - 175,
            fill='black', outline='black',
            extent=fatia)
        self.porcentagem.focus_force()
instancia = Tk()
Fatias(instancia)
instancia.mainloop()