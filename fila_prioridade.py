import heapq

fila = []
contador = 0

clientes = [
    ("João", "01", 3),
    ("Maria", "02", 2),
    ("Pedro", "03", 3),
    ("Ana", "04", 1),
    ("Lucas", "05", 3),
    ("Carlos", "06", 2),
    ("Julia", "07", 3),
    ("Rafael", "08", 1),
    ("Beatriz", "09", 2),
    ("Gabriel", "010", 3)
]

for cliente in clientes:
    prioridade = cliente[2]

    heapq.heappush(
        fila,
        (prioridade, contador, cliente)
    )

    contador += 1

print("=== FILA DE PRIORIDADE ===")

print("\nOrdem de chegada:")
for cliente in clientes:
    print(cliente)

print("\nOrdem de atendimento:")

while len(fila) > 0:
    prioridade, contador, cliente = heapq.heappop(fila)
    print(cliente)
