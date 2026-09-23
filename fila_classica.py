fila = []

fila.append(("João", "1", 3))
fila.append(("Maria", "2", 2))
fila.append(("Pedro", "3", 3))
fila.append(("Ana", "4", 1))
fila.append(("Lucas", "5", 3))
fila.append(("Carlos", "6", 2))
fila.append(("Julia", "7", 3))
fila.append(("Rafael", "8", 1))
fila.append(("Beatriz", "9", 2))
fila.append(("Gabriel", "10", 3))

print("=== FILA CLÁSSICA ===")

print("\nOrdem de chegada:")
for cliente in fila:
    print(cliente)

print("\nOrdem de atendimento:")

while len(fila) > 0:
    cliente = fila.pop(0)
    print(cliente)
