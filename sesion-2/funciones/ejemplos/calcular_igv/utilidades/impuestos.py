def calcular_precio_final(precio_del_producto):
    igv = .18
    impuesto = precio_del_producto * igv
    total = precio_del_producto + impuesto

    return total