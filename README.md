# Solución reto 6
### Soy Alejandro Bello y pertenezco al grupo de "Fenomenoides", adjunto nuestro logo: 

<details><summary>Preparense para ver el grandioso logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "somos programadores, no diseñadores" </b></figcaption></figure>
</div>
</p></details><br>

### Todas las soluciones están en el archivo reto_5.ipynb adjunto, sin embargo, acá algunas aclaraciones:
```python
# acá están todas las funciones usadas en el literal 7

def hallar_promedio(numeros:list):
  promedio_reales = 0
  for numero in numeros:
    promedio_reales += numero
  promedio_reales /= len(numeros)
  return promedio_reales


def hallar_mediana(numeros:list):
    ordenar_ascendente(numeros)
    if len(numeros) % 2 == 1:
        mediana = numeros[len(numeros) // 2]
    else:
        mediana = (numeros[len(numeros) // 2] + numeros[len(numeros) // 2 - 1]) / 2

    return mediana

def hallar_promedio_multiplicativo(numeros:list):
    producto = 1
    for numero in numeros:
        producto *= numero

    return producto ** 0.5

def ordenar_ascendente(numeros: list):
  
  for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
      if numeros[i] > numeros[j]:
        numeros[i], numeros[j] = numeros[j], numeros[i]
  return numeros

def ordenar_descendente(numeros: list):
  for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
      if numeros[i] < numeros[j]:
        numeros[i], numeros[j] = numeros[j], numeros[i]
  return numeros

def raiz_menor(numeros: list):
  raiz_menor = False
  for numero in numeros:
    raiz_actual = numero ** (1/3)
    if raiz_menor == False or raiz_actual < raiz_menor:
      raiz_menor = raiz_actual
  return raiz_menor
```
