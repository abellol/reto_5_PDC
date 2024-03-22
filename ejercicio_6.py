def poblacion(p_inicial:int, n_dia:float)-> float: 
    poblacion_total= p_inicial * (2 ** n_dia)
    return poblacion_total
if __name__ == "__main__":
    p_inicial=int(input("ingresa la poblacion inical de NuncaLandia:  "))
    n_dia=float(input("ingresa el dia en el que quieras saber cuantos contagiados habran:  "))

    contagiados= poblacion(p_inicial, n_dia)
    print(contagiados)
