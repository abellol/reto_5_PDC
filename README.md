# Solución reto 6
### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### 1. Volumen y area superficial 
[![image.png](https://i.postimg.cc/63S6j3rt/image.png)](https://postimg.cc/XGf0Xn1z)

```python
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
```

### 2. Area y perimetro
[![image.png](https://i.postimg.cc/TwZ8H44y/image.png)](https://postimg.cc/sQ90Mwyy)
```python
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
```
### 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
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
```
### 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```python
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
```
### 5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.
```python
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
```
### 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
def poblacion(p_inicial:int, n_dia:float)-> float: 
    poblacion_total= p_inicial * (2 ** n_dia)
    return poblacion_total
if __name__ == "__main__":
    p_inicial=int(input("ingresa la poblacion inical de NuncaLandia:  "))
    n_dia=float(input("ingresa el dia en el que quieras saber cuantos contagiados habran:  "))

    contagiados= poblacion(p_inicial, n_dia)
    print(contagiados)
```
### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número
```python
import funciones_matematicas  #Se adjunta el archivo funciones_matematicas.py para visualizar las funciones usadas

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
```
### 9. ¿Qué es y cómo funciona PIP en python?
##### El PIP (package intaller for Python), es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Estos paquetes pueden ser conjuntos de módulos y bibliotecas que pueden ser usados en diferentes proyectos. PIP utiliza un archivo llamado ***requirements.txt*** para especificar los paquetes que se requieren en el proyecto,. Este archivo contiene la lista de los nombres de los paquetes y, opcionalmente sus versiones.
### 10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.
#### Algunos de los paquetes mas utilizados son:
  - NumPY
  - Pandas
  - Matplotlib
  - Keras
  - Django
  - Pytest
  - etc...

Para instalar el módulo (usaremos como ejemplo Matplotlib) debemos antes que nada tener dscargado python en una versión reciente (requisito básico del curso), luego debemos ejecutar este código en la terminal:
```python
pip install matplotlib
```
y luego de un rato aparecerá que ya lo hemos descargado, podremos importar la libreria en nuestro código y empezar a utilizarlo.







