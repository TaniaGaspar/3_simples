"""projeto que visa criar uma calculadora para mais  facilmente fazer uma regra de 3 simples
precisa de 4 entradas 2x2
|---|---|
|-1-|-2-|
|---|---|
|-3-|-4-|
|---|---|
se 1 for x ou null --> (3*2)/4
se 2 for x ou null --> (1*4)/3
se 3 for x ou null --> (1*4)/2
se 4 for x ou null --> (3*2)/1

primeiro vou fazer a lógica de programação, depois faço com interface
"""
import PySimpleGUI as sg

class EcraPrincipal:
    def __init__(self):
        layout = [
            [sg.Text('n1'), sg.Input(size=(10,0),key='n1'),sg.Text(' --- '),sg.Text('n2'),sg.Input(size=(10,0),key='n2')],
            [sg.Text('n3'), sg.Input(size=(10,0),key='n3'),sg.Text(' --- '),sg.Text('n4'),sg.Input(size=(10,0),key='n4')],
            [sg.Button('Calcular'), sg.Button('Sair')],
            [sg.Output(size=(40,20))]
        ]

        self.janela = sg.Window("Regra de 3 simples").layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
                       
            n1 = int(self.values['n1'])
            n2 = int(self.values['n2'])
            n3 = int(self.values['n3'])
            n4 = int(self.values['n4'])

            if self.button=='Sair' or self.button==sg.WIN_CLOSED:
                break

            if n1==0:
                resultado= (n3*n2)/n4
                print(resultado , '<--', n2)
                print(n3 , '---' , n4)
                print('----------')
            elif n2==0:
                resultado= (n1*n4)/n3
                print(n1 , '-->', resultado)
                print(n3 , '---' , n4)
                print('----------')
            elif n3==0:
                resultado= (n1*n4)/n2
                print(n1 , '---', n2)
                print(resultado , '<--' , n4)
                print('----------')
            elif n4==0:
                resultado= (n3*n2)/n1
                print(n1 , '---', n2)
                print(n3 , '-->' , resultado)
                print('----------')
            else:
                print("ocorreu um erro")

tela = EcraPrincipal()
tela.Iniciar()

"""n1=int(input('numero 1:'))
print(n1)
n2=int(input('numero 2:'))
print(n2)
n3=int(input('numero 3:'))
print(n3)
n4=int(input('numero 4:'))
print(n4)

if n1==0:
    resultado= (n3*n2)/n4
    print(resultado)
elif n2==0:
    resultado= (n1*n4)/n3
    print(resultado)
elif n3==0:
    resultado= (n1*n4)/n2
    print(resultado)
elif n4==0:
    resultado= (n3*n2)/n1
    print(resultado)
else:
    print("ocorreu um erro")"""