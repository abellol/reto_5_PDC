import math
pi:float = math.pi

def area_rectangulo(b:float, a:float)->float:
    ar_rectangulo= a * b
    return ar_rectangulo
def perimetro_rectangulo(b:float, a:float) ->float:
    per_rectangulo=2 * a + 2 * b
    return per_rectangulo
def area_circulo(r:float)->float:
    ar_circulo=(r**2)*pi
    return ar_circulo
def perimetro_circulo(r:float)->float:
    per_circulo=2 * pi * r
    return per_circulo

if __name__ == "__main__":
    a=float(input("inserte la altura del rectangulo en cm:   "))
    b=float(input("inserte la base del rectangulo en cm:   "))
    r=float(input("inserte el radio del circulo en cm:   "))

    a_rec=area_rectangulo(a, b)
    a_cir=area_circulo(r)

    p_rec=perimetro_rectangulo(a, b)
    p_cir=perimetro_circulo(r)

    print("El area total de la figura es de",a_rec + 2* a_cir, "cm, aproximadamente")
    print("el perimetro total de la figura es de", p_rec + 2*p_cir, "cm, aproximadamente")