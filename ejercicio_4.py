P_PAN : float = 300
P_LECHE : float = 3300
P_HUEVO: float = 350
def precio_total(q_huevo:float, q_leche: float, q_pan: float) -> float:
    total_price = ((q_huevo * P_HUEVO)+(q_leche * P_LECHE)+(q_pan * P_PAN))
    return total_price

if __name__ == "__main__":
    q_huevo= float(input("Ingrese la cantidad de huevo comprado:  "))
    q_leche = float(input("ingrese la cantidad de leche comprada:  "))
    q_pan = float(input("Ingrese la cantidad de pan comprado:  "))
    billete = float(input("ingrese el valor del billete dado por su madre:  "))
    total = precio_total (q_huevo, q_leche, q_pan)
    if total > billete:
        print("el dinero no le alcanza")
    else:
        print("su cambio debe ser de:", str((billete - total)))