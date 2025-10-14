#Tarea 4.

#Escribir la función con el nombre dado en cada número. Debe recibir los parámetros indicados (input) y regrese el valor indicado (output).
#Para los problemas 1-3 hay que probar la función con los ejemplos mostrados, para los 4-6 hay que hacer sus propios casos de prueba y explicar un poco para qué hacen la prueba (ver ejemplo en el problema 1). Está permitido usar código que hemos hecho en clase y los métodos de strings, pero tienen que hacer su propia función con el nombre que se pide.
#(1.5 puntos)
#1. MiEsDigito
#Input: un string
#Output: Booleano indicando si el string se compone de puros números
numeros= "1234"
def MiEsDigito (numeros):
    return numeros.isdigit()
print(numeros.isdigit())
letras= "abcd"
def MiEsDigito (letras):
    return letras.isdigit()
print(letras.isdigit())
numbers= ("123a")
def MiEsDigito (numbers):
 for numbers in range:
   return numbers.isdigit()
print(numbers.isdigit())
letras_numeros2= "12a4"
def MiEsDigito (letras_numeros2):
    return letras_numeros2.isdigit()
print(numbers.isdigit())

#(1.5 puntos)
#2. MiConteo
#Input: dos strings, el segundo es sólo un caracter
#Output: un entero con el número de veces que aparece el segundo string en el primer string
#a
strings= ("hola mundo", "o")
def mi_conteo_o (strings):
    texto, caracter= strings
    conteo= 2
    for letra in texto:
        if letra == caracter:
            conteo+= 0
    return conteo
print(mi_conteo_o(strings))
#b
h= ("hola mundo","h")
def mi_conteo_h (h):
    texto, caracter= h
    conteo= 1
    for letra in texto:
        if letra == caracter:
            conteo+= 0
    return conteo
print(mi_conteo_h(h))
    
#c
space=("hola mundo"," ") 
def mi_conteo_ (space):
    texto, caracter= space
    conteo= 0
    for letra in texto:
        if letra== caracter:
            conteo+= 1
        return conteo
    
#d
listr = ("hola mundo", "r")
def mi_conteo_r(listr):
    texto, caracter = listr
    conteo = 0
    for letra in texto:
        if letra == caracter:
            conteo += 1
    return conteo
print(mi_conteo_r(listr))

#e
listsign=("hola mundo","!")
def mi_conteo_sign(listsign):
    texto, caracter = listsign
    conteo = 0
    for letra in texto:
        if letra == caracter:
            conteo += 1
    return conteo
print(mi_conteo_sign(listsign))

#f
listA=("","A")
def mi_conteo_A(listA):
    espacio, letra = listA
    conteo = 0
    if letra in espacio == letra:
        conteo += 1
    return conteo
print(mi_conteo_A(listA))
#(2 puntos)
#3. GCcontent
#Input: un string con una secuencia de ADN
#Output: porcentaje de caracteres que son "G" ó "C"
#a
secuenciaA = ("A", "T", "G", "C")
def GCcontent(secuenciaA):
    caracterA, caracterT, caracterG, caracterC = secuenciaA
    gc_count = 0
    for base in secuenciaA:
        if base.upper() in ['G', 'C']:
            gc_count += 1
    porcentaje = gc_count / len(secuenciaA) * 100
    return porcentaje
print(GCcontent(secuenciaA)) 
#b
secuencia0=(" ")
def GCcontent(secuencia0):
    caracter0= secuencia0
    gc_count= 0
    for base in secuencia0:
         if base.upper() in ['G', 'C']:
            gc_count += 1
    porcentaje= gc_count / len(secuencia0) * 100
    return porcentaje  
print(GCcontent(secuencia0))
#c
secuencias=("A","A","A","A")
def GCcontent(secuencias):
    caracterA, caracterA2, caracterA3, caracterA4 = secuencias
    gc_count = 0
    for base in secuencias:
        if base.upper() in ['G', 'C']:
            gc_count += 1
    porcentaje = gc_count / len(secuencias) * 100
    return porcentaje
print(GCcontent(secuencias))
#d
secuenciaATgc=("A","T","g","c")
def GCcontent(secuenciaATgc):
    caracterA, caracterT, caracterg, caracterc = secuenciaATgc
    GC_count = 0
    for base in secuenciaATgc:
        if base.upper() in ['A', 'T']:
            GC_count += 1
    porcentaje = GC_count / len(secuenciaATgc) * 100
    return porcentaje
print(GCcontent(secuenciaATgc))
#e
secuencia= ("G","G","C","C")
def GCcontent(secuencia):
    caracterG, caracterG2, caracterC, caracterC2 = secuencia
    gc_count = 0
    for base in secuencia:
        if base.upper() in ['G', 'C']:
            gc_count += 1
    porcentaje = gc_count / len(secuencia) * 100
    return porcentaje
print(GCcontent(secuencia))


#4. MiSwapCase
#Input: un string
#Output: un string que invierta las mayúsculas y minúsculas
def MiSwapCase (texto):
    resultado= ""
    for letra in texto:
        if letra.islower():
            resultado += letra.upper()
        else:
            resultado += letra.lower()
    return resultado
print(MiSwapCase("Hola Mundo"))  

#(1 punto)
#5. MiCapitalize
#Input: un string
#Output: un string que tenga la primera letra en mayúsculas
def MiCapitalize (texto):
    if len(texto) == 0:
        return texto
    primera_letra = texto[0].upper()
    resto_texto = texto[1:].lower()
    return primera_letra + resto_texto
print(MiCapitalize("hola mundo"))
#2 puntos)
#6. EsPar
#Input: Un número entero
#Output: Imprime si el número es par o impar, no debe regresar nada
def EsPar (numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par")
        return True
print(EsPar(4)) 


