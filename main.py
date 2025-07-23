class Paciente:
    def __init__(self, nome): #construtor
        self.nome = nome
        self.prontuario = []
        self.receitas = []
        self.exames = []
        self.consultas = []

    def registrar_prontuario(self, info):
        self.prontuario.append(info)

    def adicionar_receita(self, receita):
        self.receitas.append(receita)

    def solicitar_exame(self, exame):
        self.exames.append(exame)

    def agendar_consulta(self, dia, medico):
        self.consultas.append((dia, medico))

    def __str__(self):
        return f"Paciente: {self.nome}"


class Hospital:
    def __init__(self): #construtor
        self.pacientes = []
        self.leitos = []
        self.estoque = {}
        self.escalonamento = {}
        self.emergencias = []

    def cadastrar_paciente(self, nome):
        paciente = Paciente(nome)
        self.pacientes.append(paciente)
        print(f"Paciente {nome} cadastrado com sucesso.")

    def encontrar_paciente(self, nome):
        for paciente in self.pacientes:
            if paciente.nome.lower() == nome.lower():
                return paciente
        return None

    def agendar_consulta(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            dia = input("Digite o dia da consulta: ")
            medico = input("Qual a especialidade do médico? ")
            paciente.agendar_consulta(dia, medico)
            print(f"Consulta agendada para {dia} com médico {medico}.")
        else:
            print("Paciente não encontrado.")

    def registrar_prontuario(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            info = input("Digite a informação para o prontuário: ")
            paciente.registrar_prontuario(info)
            print("Informação registrada.")
        else:
            print("Paciente não encontrado.")

    def gerar_receita(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            receita = input("Digite o(s) medicamento(s): ")
            paciente.adicionar_receita(receita)
            print("Receita adicionada.")
        else:
            print("Paciente não encontrado.")

    def solicitar_exame(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            exame = input("Digite o exame a ser solicitado: ")
            paciente.solicitar_exame(exame)
            print("Exame solicitado.")
        else:
            print("Paciente não encontrado.")

    def alocar_leito(self, nome):
        paciente = self.encontrar_paciente(nome)
        if paciente:
            leito = f"Leito-{len(self.leitos) + 1}"
            self.leitos.append((leito, paciente.nome))
            print(f"{paciente.nome} alocado no {leito}")
        else:
            print("Paciente não encontrado.")

    def menu(self):
        print("\n--- Sistema de Gestão Hospitalar ---")
        print("1 - Cadastrar paciente")
        print("2 - Agendar consulta")
        print("3 - Registro médico")
        print("4 - Faturamento (em construção)")
        print("5 - Gerar receitas")
        print("6 - Solicitar exame")
        print("7 - Alocar leito")
        print("8 - Gerenciar estoque (em construção)")
        print("9 - Escalonamento de pessoal (em construção)")
        print("10 - Gerenciar emergência (em construção)")
        print("0 - Sair")


# Execução
hospital = Hospital()

while True:
    hospital.menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Encerrando sistema.")
        break
    elif opcao == '1':
        nome = input("Nome do paciente: ")
        hospital.cadastrar_paciente(nome)
    elif opcao == '2':
        nome = input("Nome do paciente: ")
        hospital.agendar_consulta(nome)
    elif opcao == '3':
        nome = input("Nome do paciente: ")
        hospital.registrar_prontuario(nome)
    elif opcao == '4':
        print("Faturamento em construção...")
    elif opcao == '5':
        nome = input("Nome do paciente: ")
        hospital.gerar_receita(nome)
    elif opcao == '6':
        nome = input("Nome do paciente: ")
        hospital.solicitar_exame(nome)
    elif opcao == '7':
        nome = input("Nome do paciente: ")
        hospital.alocar_leito(nome)
    elif opcao == '8':
        print("Gestão de estoque em construção...")
    elif opcao == '9':
        print("Escalonamento em construção...")
    elif opcao == '10':
        print("Gestão de emergência em construção...")
    else:
        print("Opção inválida.")
