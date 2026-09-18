
#1. Cómo podemos concatenar un número a un string? (.5 punto)
#wusamos string para cambiar cualquier numero a una string 
a="3"
print(a)
#2. De qué tipo son las variables justifica la respuesta (1.5 puntos)
#a = "1" es una string porque está entre comillas
#b = 1.0 es un float porque tienen un punto decimal
#c = 1.5 + True 
#d = 1.5 + 2.5
#b,c,d  todos son float porque tienen punto decimal
#e = 1 + True
#f = False + True
#g = True * 0
#e,g son int porque no tienen punto decimal f es un boolean
#3. Manipulando la variable palabra (concatenando y con los métodos de strings), convertirla (2 puntos)
#a. cambiar algunas letras por números
#palabra "hola" en "Ho14"
pala= "Ho"
bra= "14"
print(pala+bra)
#or we can use the method replace to change some letter for numbers:
palabra= "hola"
palabra= palabra.replace("la","14") 
print(palabra)
#b remover espacios
#palabra = "  hola"
#	en "hola" in this case we can use the method strip(): rstrip or lstrip to right and left ends
#it consist in removing the spaces at the beginning of the string, we can use the method strip() to remove the spaces at the beginning and at the end of the string, also we can use the method lstrip() to remove the spaces at the beginning of the string and rstrip() to remove the spaces at the end of the string
palabra= " hola "
print(palabra)
print(palabra.strip())
#c. cambiar mayúsculas y minúsculas
#for to change the uppercase letters to lowercase we can use the method lower() and for to change the lowercase letters to upercase we can use the method upper()
palabra = "HoLa"
#if we want to change only some letters to uppercase or lowercase we can use the method replace() to change some letter for other letter, for example if we want to change the letter "o" for "O" we can do it like this:
print(palabra.replace("H","h",1).replace("o","O",1).replace("L","l",1).replace("a","A",1))
#how can to make it more short? we can use the method swapcase() to change all the uppercase letters to lowercase and all the lowercase letters to uppercase, for example:
print(palabra.swapcase()) 
#this will change all the uppercase in lowercase and all the lowercase in uppercase this is the shorter way to change the uppercase to lowercase and lowercase to uppercase

#d. poner la primera en mayúscula
#palabra = "hola"
#	en "Hola" for this we can use the method capitalize 
#we write the value of the variable
word = "hOLA"
#then we use the method capitalize to change the first letter to uppercase and the rest to lowercase
print(word.capitalize())
#4. Explica qué hacen los métodos y da un ejemplo: (2 puntos)
# a. count()
gen= "AAAAAAA" #cuenta cuantas veces aparece una letra en una palabra o un elemento en una lista 
print(gen.count("A"))
# b. find() #regresa el numero del lugar que ocupa un caracter o el numero de indice donde inicia una palabra
parraf0= "hola mnundo"
print(parraf0.find("n"))
# c. isdigit() #me dice si una variable está compuesta de numeros del 0-9
abecedario= "1234556"
print(abecedario.isdigit())
# d. replace()this method help us to change some letter for other letter even for a number, such as:
michis= "gatos"
print(michis.replace("a","4"))
#we can also do this by this:
print("g" +"4"+"tos") 
#but this is different because we don´t have the value of the variable michis at the start, we only concatenate several strings to get the result 

#5. Qué problema tiene declarar estas variables? (1.5 puntos)
oraciónlarga = 'hola mundo'
palabr = 'hola' 'mundo' 
print(oraciónlarga)
print(palabr)
#si queremos que se imprima la string con un espacio, lo debemos poner entre comillas " "
palabras= "hola"" ""mundo"
print(palabras)
#6. Investigar "fstring": qué son, cómo se usan y un ejemplo. (2.5 puntos)
#fstring es una cadena con formato que se escribe con f y entre comillas el texto y entre llaves las variables u operaciones deseadas
name = "John"
age = 30
name2= "Micha"
age2="16"
print(f"My name is {name} and I am {age} years old.")
print(f"My name is {name2} and I am {age2} years old.")
