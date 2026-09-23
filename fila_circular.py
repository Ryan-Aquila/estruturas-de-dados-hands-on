class FilaCircular:
    def __init__(self):
        self.fila = [None] * 5
        self.front = 0
        self.rear = 0
        self.quantidade = 0

    def enqueue(self, cliente):
        if self.quantidade == 5:
            print("Fila cheia!")
            return

        self.fila[self.rear] = cliente
        self.rear = (self.rear + 1) % 5
        self.quantidade += 1
        print("Cliente adicionado!")

    def dequeue(self):
        if self.quantidade == 0:
            print("Fila vazia!")
            return

        cliente = self.fila[self.front]
        self.fila[self.front] = None
        self.front = (self.front + 1) % 5
        self.quantidade -= 1

        print("Cliente atendido:", cliente)

    def mostrar(self):
        print("\nFila:", self.fila)
        print("Front:", self.front)
        print("Rear:", self.rear)


fila = FilaCircular()

while True:
    print("\n=== FILA CIRCULAR ===")
    print("1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Mostrar fila")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        senha = input("Senha: ")
        prioridade = int(input("Prioridade (1, 2 ou 3): "))

        cliente = (nome, senha, prioridade)
        fila.enqueue(cliente)

    elif opcao == "2":
        fila.dequeue()

    elif opcao == "3":
        fila.mostrar()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
