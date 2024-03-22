import math
pi:float=math.pi

def volumen_cono(r1:float, h:float)->float:
    v_cono=((r1 ** 2)* h * pi)/3
    return v_cono
def volumen_esfera(r2:float)-> float:
    v_esfera=(4*((r2 ** 3) * pi))/3
    return v_esfera
def area_cono(r1:float, h:float)->float:
    a_cono = ((math.sqrt(h**2 + r1**2))* pi * r1)+(pi*(r1**2))
    return a_cono
def area_esfera(r2:float)->float:
    a_esfera = 4*((r2**2)*pi)
    return a_esfera

if __name__ == "__main__":
    r1=float(input("ingrese el radio del cono en cm:  "))
    h=float(input("ingrese la altura del cono en cm:  "))
    r2= float(input("ingrese el radio de la esfera en cm:  "))
    
    vol_cono=volumen_cono(r1, h)
    vol_esfera= volumen_esfera(r2)

    ar_esfera=area_esfera(r2)
    ar_cono=area_cono(r1, h)

    
    print("el area superficial de la figura completa es de", ar_cono + ar_esfera, "cm, aproximadamente")
    print("El volumen de la figura completa es de", vol_esfera + vol_cono, "cm, aproximadamente")