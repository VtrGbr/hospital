'''def cadastro(nome):
    pacientes = []
    pacientes.append(nome)

    print("Cadastro concluido")
    return pacientes


def agendar(marcacao):
    marcacao.lowercase()

    if marcacao == "agendar":
        dia = input("Digite o dia da consulta")
        medico = input("Qual a especialidade de medico voce vai?")

        print(f"Consulta marcada para  o dia {dia} e médico {medico} ")
    elif marcacao == "cancelar":
        print("Sua consulta foi cancelada")
    elif marcacao == "remarcar":
        dia = input("Qual dia deseja remarcar?")
    else:
        print("opcao invalida")


def registroMedico():
    paciente
    prontuario = {
        'paciente' = 
    }
'''
def menu():
    print("1 - Cadastrar paciente")
    print("2 - agendamento de consulta")
    print("3 - registro medico do paciente")
    print("4 - faturamento")
    print("5 - gerar receitas")
    print("6 - solicitar exame")
    print("7 - alocar leitos")
    print("8 - estoque")
    print("9 - escalonamento de pessoal")
    print("10 - servico de emergencia")

menu()
pacientes= []
opcao = input("Digite qual funcao voce quer executar ( para sair digite sair)")
opcao.lower()

while opcao != "sair":
    if opcao == '1':
        pac = input("Digite o nome do paciente")
        pacientes.append(pac)

        print(f"paciente {pac} cadastrado")

    elif opcao == '2':
        print("Digite a opcao desejada")
        print("1 - agendar, 2 - cancelar, 3 - remarcar")
        marcacao = input()
        marcacao.lowercase()

        if marcacao == 1:
            dia = input("Digite o dia da consulta")
            medico = input("Qual a especialidade de medico voce vai?")

            print(f"Consulta marcada para  o dia {dia} e médico {medico} ")
        elif marcacao == 2:
            print("Sua consulta foi cancelada")
        elif marcacao == 3:
            dia = input("Qual dia deseja remarcar?")
        else:
            print("opcao invalida")


    elif opcao == '3':
        registro = []
        informacao = input("Digite a informacao sobre o paciente")
        registro.append(informacao)

    elif opcao == '4':
        print("Em andamento")

    elif opcao == '5':
        while True:
            pessoa = input("Gerar receita pra qual paciente?")
            receita = []
            for paciente in pacientes:
                if pessoa in paciente:
                    remedio = input("Qual medicamento(s) deseja passar ao paciente?")
                    receita.append(remedio)
                    
                    break
                else:
                    print("Esse paciente nao foi cadastrado")  
            desejo = input("Deseja prescesver para outro paciente? [sim/nao]")
            desejo.lower()
            if desejo == "nao":
                break
        

    elif opcao == '6':
        while True:
            pessoa = input("Solicitar exame para qual paciente?")
            solicitacao = []
            for paciente in pacientes:
                if pessoa in paciente:
                    exame = input("Qual exame deseja solicitar?")
                    solicitacao.append(remedio)

                    print(f"{exame} solicitado.")
                    
                    break
                else:
                    print("Esse paciente nao foi cadastrado")  
            desejo = input("Deseja solicitar para outro paciente? [sim/nao]")
            desejo.lower()
            if desejo == "nao":
                break




    elif opcao == "7":
        print(f"Alocando um leito para o paciente {pacientes.pop()}")
    elif opcao == "8":
        print("Em andamento...")
    elif opcao == "9":
        print("em andamento...")
    elif opcao == "10":
        print("Em andamento...")
        
