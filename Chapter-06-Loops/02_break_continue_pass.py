# Break, Continue y Pass

for i in range(10):

    if i == 3:
        print("Saltando 3 (continue)")
        continue

    if i == 7:
        print("Deteniendo en 7 (break)")
        break

    if i == 5:
        pass  # no hace nada

    print(i)