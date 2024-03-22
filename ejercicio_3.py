c_pollo : float = 1 
c_gallos: float = 7
c_gallina : float = 6
def carne_total(q_pollo: float, q_gallina: float, q_gallos: float) -> float:
    total_carne = ((q_pollo * c_pollo)+(q_gallos * c_gallos)+(q_gallina * c_gallina))
    return total_carne

if __name__ == "__main__":
    q_pollo =float(input("ingrese la cantidad de pollo:   "))
    q_gallina=float(input("ingrese la cantidad de gallina:   "))
    q_gallos=float(input("ingrese la cantidad de gallo:   "))
    t_carne = carne_total(q_pollo, q_gallina, q_gallos)
    print("la cantidad total de carne de pollo es de", str(t_carne), "kg")