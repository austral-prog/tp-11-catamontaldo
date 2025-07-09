def read_file_to_dict(filename):
    ventas_por_producto = {}
    with open(filename, "r") as archivo:
        linea = archivo.readline().strip()
        if linea == "":
            return ventas_por_producto

        ventas = linea.split(";")
        for venta in ventas:
            if venta == "":
                continue
            producto, valor = venta.split(":")
            valor = float(valor)
            if producto not in ventas_por_producto:
                ventas_por_producto[producto] = []
            ventas_por_producto[producto].append(valor)

    return ventas_por_producto



def process_dict(data):
    for producto, montos in data.items():
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
