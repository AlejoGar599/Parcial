#Alejandro García, Juan Andrés Daza
def mostrar_productos(productos):
    for codigo in productos:
        print(codigo, productos[codigo][0], "$", productos[codigo][1], "Cantidad:", productos[codigo][2])

def registrar_producto(productos, pedido, codigo, cantidad):
    if codigo not in productos:
        print("Producto no encontrado")
    elif cantidad <= 0:
        print("Cantidad no valida")
    elif cantidad > productos[codigo][2]:
        print("No hay suficientes unidades disponibles")
    else:
        nombre = productos[codigo][0]
        precio = productos[codigo][1]
        existencias = productos[codigo][2]
        subtotal = precio * cantidad
        pedido.append((codigo, nombre, cantidad, subtotal))
        productos[codigo] = (nombre, precio, existencias - cantidad)
        print("Producto agregado al pedido")

def calcular_total(pedido):
    total = 0
    for i in range(len(pedido)):
        total = total + pedido[i][3]
    return total

def pedir_producto():
    print("-----Catalogo-----")
    mostrar_productos(productos)
    codigo = int(input("Codigo del producto: "))
    cantidad = int(input("Cantidad: "))
    registrar_producto(productos, pedido, codigo, cantidad)

def mostrar_resumen():
    total = calcular_total(pedido)
    if total >= 50000:
        descuento = total * 0.10
    else:
        descuento = 0
    total_final = total - descuento
    print("========== RESUMEN DEL PEDIDO ==========")
    print("Producto  Cantidad  Subtotal")
    print("-----------------------------------------")

    for i in range(len(pedido)):
        print(pedido[i][1], pedido[i][2], pedido[i][3])

    print("-----------------------------------------")
    print("Total : $" + str(int(total)))
    print("Descuento : $" + str(int(descuento)))
    print("TOTAL A PAGAR : $" + str(int(total_final)))
    print("========================================")

def menu_principal():
    while True:
        print("========== CAFETERIA ==========")
        print("1. Mostrar productos")
        print("2. Hacer un pedido")
        print("3. Finalizar pedido")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            pedir_producto()
        elif opcion == "3":
            mostrar_resumen()
            break
        else:
            print("Opcion no valida.")

productos = {
1: ("Cafe", 3000, 20),
2: ("Jugo natural", 5000, 15),
3: ("Sandwich", 8000, 10),
4: ("Empanada", 2500, 25),
5: ("Hamburguesa", 12000, 8)
}
pedido = []
menu_principal()
