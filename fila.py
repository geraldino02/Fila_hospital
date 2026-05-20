import heapq  # biblioteca que implementa a heap (min-heap)

# Classe que representa um paciente
class Paciente:
    def __init__(self, nome, prioridade, descricao):
        self.nome = nome
        self.prioridade = prioridade
        self.descricao = descricao

    # Define como o objeto será exibido
    def __repr__(self):
        return f"{self.nome} ({self.descricao})"


# Classe que representa o sistema do hospital
class Hospital:
    def __init__(self):
        self.fila = []
        self.contador = 0  # controla ordem de chegada

    def inserir_paciente(self, nome, prioridade, descricao):
        paciente = Paciente(nome, prioridade, descricao)

        # prioridade + ordem de chegada
        heapq.heappush(
            self.fila,
            (prioridade, self.contador, paciente)
        )

        self.contador += 1

        print(f"Paciente {nome} inserido como {descricao}")

    def atender_paciente(self):
        if not self.fila:
            print("Fila vazia!")
            return
        
        prioridade, ordem, paciente = heapq.heappop(self.fila)

        print(f"Atendendo paciente: {paciente.nome} ({paciente.descricao})")

    def mostrar_fila(self):
        if not self.fila:
            print("Fila vazia!")
            return
        
        print("\nPacientes aguardando atendimento:")

        for prioridade, ordem, paciente in self.fila:
            print(f"{paciente.nome} ({paciente.descricao})")

# Programa principal (menu)
hospital = Hospital()

while True:
    print("\n===== SISTEMA HOSPITALAR =====")
    print("1 - Inserir paciente")
    print("2 - Atender paciente")
    print("3 - Mostrar fila")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        nome = input("Nome do paciente: ")

        print("\nClassificação de prioridade:")
        print("1 - Emergência")
        print("2 - Urgente")
        print("3 - Pouco urgente")
        print("4 - Não urgente")

        prioridade = int(input("Digite a prioridade: "))

        # Define a descrição da prioridade
        if prioridade == 1:
            descricao = "Emergência"
        elif prioridade == 2:
            descricao = "Urgente"
        elif prioridade == 3:
            descricao = "Pouco urgente"
        elif prioridade == 4:
            descricao = "Não urgente"
        else:
            print("Prioridade inválida!")
            continue

        hospital.inserir_paciente(nome, prioridade, descricao)

    elif opcao == 2:
        hospital.atender_paciente()

    elif opcao == 3:
        hospital.mostrar_fila()

    elif opcao == 0:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
