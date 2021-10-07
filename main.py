import re

texto = input('Formatos:\n- CPF: 111.222.333-44: \n- E-mail: asvc@...: \n- Placa de veículo: xxx/XXX-123 \nEntrada: ')

formatoCPF = re.compile(r'([\d]{3}\.){2}[\d]{3}-[\d]{2}') #Formato CPF
formatoEmail = re.compile(r'^[\w._-]+@[\w]+\.[\a-z]') #Formato e-mail
formatoPlaca = re.compile(r'^[a-zA-Z]{3}-\d{4}') #Formato placa

#Se a entrada combinar com formato CPF
if formatoCPF.match(texto):
    CPFsemPonto = re.sub(r'[^\w\s]', '', texto) #Retira os pontos do CPF para manipulação
    CPFsemNum = CPFsemPonto[:-2] #Retira os 2 ultimos digitos para verificar

#Calculo para validar os digitos
    digitoUm = 0
    digitoDois = 0
    multiplicador = 10
    contador = 0
    for i in CPFsemNum: #Calculo para descobrir o primeiro digito
        contador += int(i) * multiplicador
        multiplicador -= 1
    modDivisao = contador % 11
    if modDivisao <= 10 and modDivisao> 0:
        digitoUm = 11 - modDivisao
    CPFsemNum += str(digitoUm)
    multiplicador = 11
    contador = 0

    for i in CPFsemNum: #Calculo para descobrir o segundo digito
        contador += int(i) * multiplicador
        multiplicador -= 1
    modDivisao = contador % 11
    if modDivisao <= 10 and modDivisao> 0:
        digitoDois = 11 - modDivisao
    CPFsemNum += str(digitoDois)

#Compara os dois ultimos digitos do CPF informado e do calculado
    if CPFsemNum[-2::] == texto[-2::]:
        print("É um CPF válido")
    else:
        print('Não é um CPF válido')

#Se a entrada combinar com formato e-mail
elif formatoEmail.match(texto):
    print("É um e-mail válido")
#Se a entrada combinar com formato Placa
elif formatoPlaca.match(texto):
    print("É um formato de placa válido")
#Se não combinar com nenhum formato
else:
    print('Não é um formato válido')
