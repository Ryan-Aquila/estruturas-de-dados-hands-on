import random
import heapq

clientes = []

for i in range(1, 21):
    nome = "Cliente" + str(i)
    senha = str(i).zfill(3)
    prioridade = random.randint(1, 3)

    clientes.append((nome, senha, prioridade))

print("===== clientes na ordem que chegaram =====")

for cliente in clientes:
    print(cliente)

print("\n===== fila normal =====")

fila = clientes.copy()

while len(fila) > 0:
    cliente = fila.pop(0)
    print(cliente)

print("\n===== fila circular =====")

fila_circular = [None] * 5
front = 0
rear = 0
quantidade = 0

for cliente in clientes:
    if quantidade == 5:
        atendido = fila_circular[front]
        fila_circular[front] = None
        front = (front + 1) % 5
        quantidade -= 1

        print(atendido)

    fila_circular[rear] = cliente
    rear = (rear + 1) % 5
    quantidade += 1

    print("front:", front, "| rear:", rear)

while quantidade > 0:
    atendido = fila_circular[front]
    fila_circular[front] = None
    front = (front + 1) % 5
    quantidade -= 1

    print(atendido)

print("\n===== fila por prioridade =====")

fila_prioridade = []
contador = 0

for cliente in clientes:
    prioridade = cliente[2]

    heapq.heappush(
        fila_prioridade,
        (prioridade, contador, cliente)
    )

    contador += 1

while len(fila_prioridade) > 0:
    prioridade, contador, cliente = heapq.heappop(fila_prioridade)
    print(cliente, "- prioridade:", prioridade)
