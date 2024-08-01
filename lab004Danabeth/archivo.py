def guardar_inventario(productos):
    with open("inventario.txt", "w") as file:
        file.write(productos)
    print(f"Inventario guardado exitosamente en txt")


def cargar_inventario():
    with open("inventario.txt", "r") as file:
        data = file.read()
        return data
