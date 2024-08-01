import archivo as a


class GestionProductos:
    def __init__(self, pid_producto, pnombre, pmarca, pprecio, pexistencias, ppais):
        self.id_producto = pid_producto
        self.nombre = pnombre
        self.marca = pmarca
        self.precio = pprecio
        self.existencias = pexistencias
        self.pais = ppais
        self.proveedor = {
            "codigo": self.id_producto,
            "nombre": self.nombre,
            "pais": self.pais,
        }

    def mostrar_informacion(self):
        print(f"Codigo o id del producto: {self.id_producto}, Nombre: {self.nombre}, marca: {self.marca}, precio: {self.precio}")


class CrudProductos:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, pid_producto, pcodigo, pnombre, pmarca, pprecio, pexistencias):
        producto = {
            "id": pid_producto,
            "codigo": pcodigo,
            "nombre": pnombre,
            "marca": pmarca,
            "precio": pprecio,
            "existencias": pexistencias,
        }

        self.productos.append(producto)

        print(f"Producto {pnombre} agregago con exito")  # o return

    def buscar_producto(self, pid_producto):
        for producto in self.productos:
            if producto["id"] == pid_producto:
                return producto
        return None

    def eliminar_producto(self, pid_producto):
        producto = self.buscar_producto(pid_producto)
        if producto:
            self.productos.remove(producto)
            print(f"Producto: {producto.nombre} eliminado con exito")
        else:
            print(f"Producto no eliminado")

    def modificar_precio(self, id_producto, precio_nuevo):
        producto = self.buscar_producto(id_producto)
        if producto:
            if precio_nuevo:
                producto.precio = precio_nuevo
            print(f"Precio de producto: {producto.nombre} modificado con éxito.")
        else:
            print("Producto no encontrado.")

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def guardar_inventario(self):
        for producto in self.productos:
            producto = f"Nombre del producto: {producto.nombre}, codigo: {producto.codigo}"
            a.guardar_inventario(producto)

    def cargar_inventario(self):
        a.cargar_inventario()


gestion = CrudProductos()


def mostrar_menu():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar Precio de producto")
    print("4. Listar productos")
    print("5. Buscar producto")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


def agregar_producto():
    global gestion
    while True:
        try:
            pid_producto = int(input("Ingrese el id del producto: "))
            pnombre = input("Ingrese el nombre del producto: ")
            pmarca = input("Ingrese el marca del producto: ")
            pprecio = int(input("Ingrese el precio del producto: "))
            pexistencias = int(input("Ingrese el existencias del producto: "))
            ppasis = input("Ingrese el pais del producto: ")
            gestion.agregar_producto(pid_producto, pnombre, pmarca, pprecio, pexistencias, ppasis)
            break
        except ValueError:
            print("Opcion invalida. Intente de nuevo")


def eliminar_producto():
    global gestion
    while True:
        try:
            pid_producto = input("Ingrese el id del producto que desea eliminar: ")
            gestion.eliminar_producto(pid_producto)
            break
        except ValueError:
            print("Opcion invalida. Intente de nuevo")


def actualizar_precio_producto():
    global gestion
    while True:
        try:
            pid_producto = input("Ingrese el id del producto al cual le desea modificar el precio: ")
            precio_nuevo = int(input("Ingrese el nuevo precio del producto: "))
            gestion.modificar_precio(pid_producto, precio_nuevo)
            break
        except ValueError:
            print("Opcion invalida. Intente de nuevo")


def buscar_producto():
    global gestion
    while True:
        try:
            pid_producto = input("Ingrese el id del producto que desea buscar: ")
            gestion.buscar_producto(pid_producto)
            break
        except ValueError:
            print("Opcion invalida. Intente de nuevo")


def menu_principal():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            actualizar_precio_producto()
        elif opcion == "4":
            gestion.listar_productos()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            gestion.guardar_inventario()
        elif opcion == "7":
            gestion.cargar_inventario()
        elif opcion == "8":
            break
        else:
            print("Opción inválida.")


if __name__ == '__main__':
    menu_principal()
