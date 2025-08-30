inventario = [
    {"id": 1, "nombre": "Manzanas", "precio": 1000, "cantidad": 10},
    {"id": 2, "nombre": "Peras", "precio": 1200, "cantidad": 8},
    {"id": 3, "nombre": "Naranjas", "precio": 800, "cantidad": 15}
]

def mostrar_inventario():
    if len(inventario) == 0:
        print("Inventario vacío.")
    else:
        for producto in inventario:
            print(f"{producto['id']}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = int(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    nuevo_id = len(inventario) + 1
    inventario.append({"id": nuevo_id, "nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado.")

def actualizar_producto():
    mostrar_inventario()
    opcion = int(input("ID del producto a actualizar: "))
    for producto in inventario:
        if producto["id"] == opcion:
            producto["nombre"] = input("Nuevo nombre: ")
            producto["precio"] = int(input("Nuevo precio: "))
            producto["cantidad"] = int(input("Nueva cantidad: "))
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    mostrar_inventario()
    opcion = int(input("ID del producto a eliminar: "))
    for producto in inventario:
        if producto["id"] == opcion:
            inventario.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

def facturar():
    mostrar_inventario()
    opcion = int(input("ID del producto a facturar: "))
    cantidad = int(input("Cantidad: "))
    for producto in inventario:
        if producto["id"] == opcion:
            if producto["cantidad"] >= cantidad:
                subtotal = producto["precio"] * cantidad
                iva = subtotal * 0.19
                total = subtotal + iva
                producto["cantidad"] -= cantidad
                print(f"\nFactura: {producto['nombre']} x{cantidad}")
                print(f"Subtotal: {subtotal}")
                print(f"IVA (19%): {iva}")
                print(f"Total: {total}")
            else:
                print("No hay suficiente cantidad.")
            return
    print("Producto no encontrado.")

def main():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1) Mostrar Inventario")
        print("2) Agregar Producto")
        print("3) Actualizar Producto")
        print("4) Eliminar Producto")
        print("5) Facturar")
        print("0) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            facturar()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

main()
