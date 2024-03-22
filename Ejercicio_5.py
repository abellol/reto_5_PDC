T_AÑO : float = 12
C : float=100
I : float = 1
def años(num_meses:float) -> float:
    total_tiempo = (num_meses / T_AÑO)
    return total_tiempo
def interes(inversion_inicial: float, tasa_interes:float) -> float:
    total_intereses = ((inversion_inicial*(I + (tasa_interes/C))))
    return total_intereses

if __name__ == "__main__":
    inversion_inicial=float(input("ingrese el valor del prestamo:   "))
    tiempo = float(input("ingrese el periodo de tiempo en meses:  "))
    tasa_interes= float(input("ingrese la tasa de interes en porcentaje sin el (%):   "))

    valor_prestamo=interes(inversion_inicial, tasa_interes)
    tiempo_prestamo=años (tiempo)
    
    p_total= valor_prestamo ** tiempo_prestamo

    print("su prestamo tendrá un valor aproximado de",str(p_total), "en un tiempo de", str(tiempo), "meses")
