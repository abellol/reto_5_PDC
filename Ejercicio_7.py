import funciones_matematicas

if __name__ == "__main__":

        lista_numeros=[]
        for i in range(5):
                numeros = float(input("ingrese uno de los numeros:  "))
                lista_numeros.append(numeros)

        print(lista_numeros)

        promedio = funciones_matematicas.hallar_promedio(lista_numeros)
        mediana = funciones_matematicas.hallar_mediana(lista_numeros)
        prom_multi = funciones_matematicas.hallar_promedio_multiplicativo(lista_numeros)
        ascendente= funciones_matematicas.ordenar_ascendente(lista_numeros)
        descendente = funciones_matematicas.ordenar_descendente(lista_numeros)
        potencias = funciones_matematicas.potencia_extremos(lista_numeros)
        raiz = funciones_matematicas.raiz_menor(lista_numeros)

        print("el promedio de los datos ingresados es:", str(promedio))
        print("la mediana de los datos ingresados es:", str(mediana))
        print("el promedio multiplicativo de los datos ingresados es de:", str(prom_multi))
        print("la lista ordenada de lo elementos dados de forma ascendente es:", str(ascendente))
        print("la lista ordenada de los elementos dados de forma descendente:", str(descendente))
        print("el resultado de la potencia con base del numero mayor de lista, elevado al mas pequeño es:", str(potencias))
        print("la raiz cubica del numero mas pequeño de la lista es:", str(raiz))
