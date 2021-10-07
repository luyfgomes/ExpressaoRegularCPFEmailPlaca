# -*- coding: utf-8 -*-
import re
import PySimpleGUI as sg

layout = [[sg.Text("Digite uma das informações abaixo para saber se é valido:")],
          [sg.Text("Formatos:\n -CPF: 111.222.333-44: \n -E-mail: asvc@...: \n -Placa de veículo: xxx/XXX-1234 \n")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button("Validar"), sg.Button("Sair")]]

# Definição dos formatos da entrada para combinar com CPF, e-mail e placa
formatoCPF = re.compile(r'([\d]{3}\.){2}[\d]{3}-[\d]{2}')
formatoEmail = re.compile(r'^[\w._-]+@[\w]+.[\a-z]{4}')
formatoPlaca = re.compile(r'^[a-zA-Z]{3}-\d{4}')

window = sg.Window("Teste de Validação", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break

    # Se a entrada combinar com formato CPF
    if formatoCPF.match(values['-INPUT-']):
        CPFsemPonto = re.sub(r'[^\w\s]', '', values['-INPUT-'])  # Retira os pontos do CPF para manipulação
        CPFsemNum = CPFsemPonto[:-2]  # Retira os 2 ultimos digitos para verificar

        # Calculo para validar os digitos
        digitoUm = 0
        digitoDois = 0
        multiplicador = 10
        contador = 0
        for i in CPFsemNum:  # Calculo para descobrir o primeiro digito
            contador += int(i) * multiplicador
            multiplicador -= 1
        modDivisao = contador % 11
        if 10 >= modDivisao > 0:
            digitoUm = 11 - modDivisao
        CPFsemNum += str(digitoUm)
        multiplicador = 11
        contador = 0

        for i in CPFsemNum:  # Calculo para descobrir o segundo digito
            contador += int(i) * multiplicador
            multiplicador -= 1
        modDivisao = contador % 11
        if 10 >= modDivisao > 0:
            digitoDois = 11 - modDivisao
        CPFsemNum += str(digitoDois)

        if CPFsemNum[-2::] == values['-INPUT-'][-2::]:
            window['-OUTPUT-'].update(values['-INPUT-'] + "\tCPF Valido", text_color='yellow')
        else:
            window['-OUTPUT-'].update(values['-INPUT-'] + "\tCPF Invalido", text_color='red')

    elif formatoEmail.match(values['-INPUT-']):
        window['-OUTPUT-'].update(values['-INPUT-'] + "\tE-mail Valido", text_color='yellow')
    elif formatoPlaca.match(values['-INPUT-']):
        window['-OUTPUT-'].update(values['-INPUT-'] + "\t Placa Valida", text_color='yellow')
    else:
        window['-OUTPUT-'].update(values['-INPUT-'] + "\t Formato Invalido", text_color='red')

window.close()
