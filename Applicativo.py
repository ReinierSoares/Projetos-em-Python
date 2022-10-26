from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
	[sg.Text('Usuário'),sg.Input(key='usuario',size=(20,0))],
	[sg.Text('Senha'),sg.Input(key='senha', password_char='*',size=(20,0))],
	[sg.Checkbox('Salvar o login?')],
	[sg.Button('Entrar')]
]
#JANELA
janela = sg.Window('Tela',layout)

while True:
		eventos, valores = janela.read()
		if eventos == sg.WINDOW_CLOSED:
			break
		if eventos == 'Entrar':
			if valores['usuario'] == 'jhonatan' and valores['senha']=='123456':
				print('salvo')
			