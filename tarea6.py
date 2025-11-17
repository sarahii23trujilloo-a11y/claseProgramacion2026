#(3 puntos)
#1. Construye una lista que funcione como un conjunto (set). 
# Esto es, construye una función a la que le pasas una lista y un elemento que agregar 
lista = [{'1':'uno','2':'dos','3':'tres'}] #lista inicial
def agregar_a_conjunto(valor, llave):#se define función
    if valor not in lista: #si el valor no está en la lista
        lista.append({llave:valor}) #se agrega el valor con su llave mediante append
    return lista #regresa la lista actualizada
print(agregar_a_conjunto('cuatro','4')) #se imprime el resultado de la función
#sobreescribir el valor de una llave si esta ya existe:
def agregar_o_sobreescribir(valor, llave): #se define función
    for elemento in lista: #se recorre la lista
        if llave in elemento: #si la llave ya existe en el elemento
            elemento[llave] = valor #se sobreescribe el valor
            return lista #regresa la lista actualizada
    lista.append({llave:valor}) #si la llave no existe, se agrega el nuevo par llave-valor
    return lista #regresa la lista actualizada
print(agregar_o_sobreescribir('cinco','2')) #se imprime el resultado de la función indicando que se sobreescribió el valor de la llave '2'
# pero sólo lo agregue si no existe dentro de la lista,
# también hay que hacer una función que agregue valores
# (si la llave no existe hay que agregarla y si ya existe hay que sobre-escribir su valor).
#(4 puntos)
#2. Construye dos listas que funcionen juntas como un diccionario. Por ejemplo, simular el diccionario
d=['uno', 'dos', 'tercero'] #lista de llaves
d2=['1', '2', '3'] #lista de valores
def obtener_valor(llave): #se define función
    if llave in d: #si la llave está en la lista de llaves
        indice = d.index(llave) #se obtiene el índice de la llave
        return f'la llave {llave}, tiene valor {d2[indice]}' #regresa el valor correspondiente
    else:
        return 'La llave no existe' #si la llave no existe, regresa un mensaje indicando eso
#imprime el valor y llave de todos:
print(obtener_valor('dos')) #se imprime el resultado de la función
print(obtener_valor('tercero')) 
#d = {'uno':1, 'dos':2, 'tercero':3}
#Utilizando las listas debe poder responder
#"la llave uno, tiene valor 1"
#Sugerencia, usar el método index de las listas para buscar la llave y luego el índice para buscar el valor correspondiente.

#(3 puntos)
#3. Hacer una función que convierta un string con nucleótidos en la proteína correspondiente.
# Sugerencia, crea un diccionario del código genético. 
# Nota: los codones de paro comunmente se sustituyen por un asterisco (*). 
# Tener cuidado con qué pasa si la secuencia no tiene una longitud múltiplo de 3.

oxitocina = {'AUG':'Met','UGU':'Cys', 'UAC':'Tyr', 'AUC':'Ile', 'CAG':'Gln', 'AAU':'Asn', 'UGC':'Cys', 'CCU':'Pro', 'CUU':'Leu', 'GGU':'Gly','UGA':'*'}
def convertir_a_oxitocina(secuencia): #se define función
    resultado = [] #lista para almacenar la proteína resultante
    if len(secuencia) % 3 != 0: #si la longitud de la secuencia no es múltiplo de 3
        return 'La secuencia no tiene una longitud múltiplo de 3' #regresa un mensaje indicando eso
    for i in range(0, len(secuencia), 3): #recorre la secuencia en pasos de 3
        codon = secuencia[i:i+3] #obtiene el codón actual
        if codon in oxitocina: #si el codón está en el diccionario
            resultado.append(oxitocina[codon]) #agrega la proteína correspondiente a la lista resultado
        else:
            resultado.append('X') #si el codón no está en el diccionario, agrega 'X' para indicar un codón desconocido
    return '-'.join(resultado) #regresa la proteína resultante como una cadena separada por guiones
print(convertir_a_oxitocina('AUGUGUUACAUCCAGAAUUGCCCUCUUGGUUGA')) 