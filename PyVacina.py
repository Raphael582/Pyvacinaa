import csv
from Lib.Interface import *

tokenAcesso = 0
usuarioAtual = ""
vacinaUserAtual= []

while tokenAcesso == 0:
    resposta = menu(["Logar", "Registrar"])
    if resposta == 1:
        with open("dados.txt", "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            entradaLogin = input("Digite seu login = ")
            entradaSenha = input("Digite sua senha = ")
            for credenciais in csv_reader:
                if credenciais[2] == entradaLogin and credenciais[3] == entradaSenha:
                    tokenAcesso = 1
                    print("Bem-vindo,", credenciais[0])
                    usuarioAtual = entradaLogin
                    vacinaUserAtual.extend(credenciais[4]+credenciais[5]+credenciais[6])
                    break


    elif resposta == 2:
        with open("dados.txt", "a", newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            registroNome = input("Digite seu nome completo = ")
            registroCpf = input("Digite seu CPF formatado (Exemplo:000.000.000-00) = ")
            registroLogin = input("Digite um nome de usuário = ")
            registroSenha = input("Digite uma senha = ")
            registroConfSenha = input("Digite a confirmação da sua senha = ")
            if registroSenha == registroConfSenha:
                print("Conta criada com sucesso! mas precisamos saber mais algumas informações sobre quais vacinas você já tomou.")
                gripeEntrada = str(input("Você tomou a vacina da Gripe? Y/N = ")).upper()
                covidEntrada = str(input("Você tomou a vacina do Coronavirus? Y/N = ")).upper()
                tetanoEntrada = str(input("Você tomou a vacina contra Tétano? Y/N = ")).upper()
                csvWriter.writerow([registroNome,registroCpf,registroLogin,registroSenha,gripeEntrada,covidEntrada,tetanoEntrada])
                print("Pronto! sua conta está criada! você já pode logar!")
    else:
        print("ERRO! digite algo válido!")
while tokenAcesso == 1:
    resposta = menu(["Ver vacinas tomadas.", "Ver vacinas agendadas.", "Agendar vacinas.", "Cadastrar nova vacina."])
    if resposta == 1:









