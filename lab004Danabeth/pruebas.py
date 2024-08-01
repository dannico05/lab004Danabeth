def listar_productos():
    for producto in productos:
        print(producto)

producto1 = {
    "codigo": "1",
    "nombre": "nda",
}
producto2 = {
    "codigo": 2,
    "nombre": "nda",
}
productos = [producto1, producto2]

listar_productos()

