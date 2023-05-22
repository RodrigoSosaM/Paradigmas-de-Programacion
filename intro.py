'''Este es un supercomentario
   De inicio a nuestro resumen
'''
#======================
# Operaciones basicas
#======================
print(2+3) 
print(2*3) 
print(2/3) 
print(2**10) 
print(2**0.5) # raíz cuadrada 
print(10%2) 
print(10%0.1) # exclusivo en python 

#===========================================
# Para saber el tipo de objeto se usa type
#===========================================
t=0
print(type(t)) # entero
t=3.6
print(type(t)) #real (flotante)
t=True

#=========================
#Mensajes a pantalla
#=========================
print("Este es un comando de python" , "Este es otro enunciado" , t) 
print('id: ',1)
print('First Name: ' , 'Steve')
print('Last Name: ' , 'Jobs')
print("vamos a sumar esto" + "con esto otro")

#===============================================
# Continuar una instruccio en varios renglones
#===============================================
if 100 > 99 and \
    200 <= 300 and \
    True != False:
        print('Hello World')

#===========================================
# Comandos diferentes en la misma línea
#===========================================
print("Hola" , print("tu!!"))#SE CONSIDERA MALA PRÁCTICA

#===================================================
# Usando parentesis redondos, cuadrados o llaves
# se puede escribir en varios renglones 
#===================================================
lista= [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4] , [5,6,7,8] , [9,10,11,12] ]
#Las matrices siempre son los corchetes dentro de otros corchetes

print(lista)
print(matriz)

#===================================================================
# Identación estricta para procesos dependientes de : (dos puntos)
#=================================================================== 
if 10>5:
  print("diez es mayor que cinco")
  print("otra identación")
for i in lista:
   print(i)
   print("ok")
if 10>5:
  print("verdadero")
  if 10<20:
    print("verdadero")
elif 5>3: #comienza segunda condicional
    print("esto no se imprimirá")
else:
    print("aquí nunca llega")

#=============
# Funciones
#=============
def say_hello(name):
    print("Hello " , name)
    print("Welcome to Python Tutorials")

say_hello("Julián")

#==================|  
# INTRO PY2
#==================|

#=======================================================
#Input permite obtener datos del usuario en prompter
#=======================================================
nombre = input("Dame tu nombre: ")
print("Hola como estás" , nombre)

#======================================
# Los enteros son de precisión ilimitada
#==========================================
y = 5000000000000000000000000000000000
print(y)

#===============================================================
# Se pueden delimitar números con guíon bajo pero no con coma
#===============================================================
y= 5_000_000
print(y)

#=====================================================
# La función int() canbia strings y floats a enteros
#===================================================== 
numero = int(input("Dame tu edad: "))
type(numero)

#=====================================================
#La notación cientifica de flotantes utiliza e o E
#=====================================================
y = 1.2E-09
print(y)

#==============================================================
# La función flloat() convierte strings y enteros a flotantes
#==============================================================
y = float("14.3")
print(y)

#======================================================
# Los complejos se escriben con la raíz de menos uno 
# j siempre con un número como prefijo
# no acepta la j suelta 
#======================================================
z = 1+1j

# suma +
# resta -
# multiplicación *
# división /
# módulo %
# exponente **
# // función piso
# Funciones para transformar numeros int() float() complex()
# Operaciones abs() round() pow() 
 
print(round(3.15159,4))

#===========================
# Strings de varias lineas
#============================
parrafo = """Mi maestro me dio un beso en la salida
porque hice mis palitos parejitos"""
print(parrafo)

#=================================================
# La función len() obtiene el tamaño del string
#=================================================
n=len(parrafo)
print(n)
  
#===============================================================
#Las letras en un string ocupan lugares como en un arreglo
# (también de atrás para adelante comenzando en -1 el último)
#===============================================================
palabra = "Hola"
print(palabra[0])
print(palabra[-4])



#=======================||
# VIDEO 2 "Operadores"
#=======================||

#======================
# Conjunto en Python
#======================
even_nums = {2, 4, 6, 8, 10} # conjunto de números pares
print(even_nums)

#El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} # conjunto de diferentes objetos
print(emp)

nums ={1,2,2,3,4,4,5,5}
print(nums)

#==================================
# Convertir secuencia a conjunto
# No lo genera en orden
#==================================
s = set('Hello')
print(s)
s = set((1,2,3,4,5)) # tupla a conjunto
print(s)

#=================================================
# De diccionario a conjunto: conjunto de llaves
#=================================================
d = {1: 'Onw' , 2: 'Two'}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 # Unión
print(su)

si = s1&s2 # Intersección
print(si)

sr = s1-s2 #Diferencia de conjuntos
print(sr)

sp = s2-s1 
print(sp)

ss = s1^s2 # Diferencia simétrica
print(ss)

#=======================
# Uso de diccionarios
#=======================
capitals = {"USA":"Washington D.C." , "France":"Paris" , "India":"New Delhi"}
print(capitals)

#===============
# Llave:valor
#===============
# diccionario vacío
d = {}

#Llave entera, valoor string
numNames={1:"One" , 2:"Two" , 3:"Three"}

# Llave real, valor string
decNames={1.5:"One and Half" , 2.5: "Two and Half" , 3.5:"Three and Half"}

#LLave tupla, valor string
items={("Parker" , "Reyonolds" , "Camlin"):"pen",("LG","Whirlpool","Samsung"): "Refrigerator"}

#Llave string, valor int
romanNums = {'I':1 , 'II':2 , 'III':3, 'IV':43, 'IV':43, 'IV':4, 'V':5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("india"))

#Reportar llave y valor
for k in capitals:
   print("Key = " + k +", Value = " + capitals[k])
# Nuevo dato para el diccionario
capitals["México"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["México"]
print(capitals)

#Borrar todo el diccionario
del capitals

#Reportar llaves
print(romanNums.keys())

#Reportar valores
print(romanNums.values())

# Juicio de llave (está o no está la llave en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)

#=======================|
# PARTE 2 "Listas"
#=======================|

#================================================
# Listas
# las listas pueden ser de objetos diferentes
#================================================
miPrimeraLista= [] #Lista vacía
print(miPrimeraLista)

#====================
# Llenado de lista
#====================
miPrimeraLista =[1 , "Javier" , 1.34 , "Bosco" , "Angel" , "Abiigail" , True]
print(miPrimeraLista)

#==========================================
# list: hacer una lista
# range(i,j) : secuencia de i hasta j-1
#==========================================
nums = list(range(1,61))

for i in nums:
   print(i)

#========================================
# Incluir nuevos elementos en la lista
#========================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)

#================================
# Quitar elementos de la lista
#================================
nums.remove(61)
print(nums)

#================================
# Quitar elemento con índice i
#================================
i = 61
del nums[i]
print(nums)

#===================
# Borrar la lista
#===================
del nums

#================
# Sumar listas
#================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#==================
# Llenado a mano
#==================
potencial = []
for i in range(0,10000):
   potencial.append(float(i))
print(potencial[100])

#==============================
# Generar tupla con la lista
#==============================
potencial = tuple(potencial)
print(potencial[100])

#===========||
# VIDEO 3
#===========||

#=================
# Condicionales
#=================
precio = 50
#-------------
# Si esto...
#-------------
if precio < 50:
    print("El precio es menor que 50")
#----------------------------
# Si no... si esto otro...
#----------------------------
elif precio >50:
    print("EL precio es mayor a 50")
#--------------------------
#Si nada de lo aterior...
#--------------------------
else:
    print("EL precio es 50")

precio = 50 
cantidad = 5
total = precio*cantidad
#========================
# Concionales anidados
#========================
if total > 100:
    if total > 500:
        print("TOtal es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 pero mayor que 400")
        elif total < 500 and total > 300:
            print("Total entre 300 y 500")
        else:
            print("Total entre 100 y 300")
#---------------------------------
# Condiconal de igualdad son ==
#---------------------------------
elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

#==================================================
# Contador mientras la condicional sea verdadera
#==================================================
num =0
while num < 5:
    num = num + 1
    print('num = ' , num)

num = 0
while num <5:
    num += 1                    # num +=1 es lo mismo que num = num +1
    print('num= ' , num)
    if num == 3:                # condición ates de salir del bucle
        break

num = 0
while num <5:
    num += 1
    if num > 3:
        continue          #evitar lo que sigue, continuar con las iteaciones
    print('num= ' , num)

#=====================
# Bucle sobre lista
#=====================
nums = {10, 20, 30, 40, 50}
for i in nums:
    print(i)

#==========================
# BLucle sobre un string
#==========================
for char in 'Hello':
    print (char)

#===============================
# Bucles soobre un diccioario
# items = elementos
#===============================
numNames = {1:'One' , 2:'Two' , 3:'Trhee'}
for pair in numNames.items():
    print(pair)

#==============================
# Bucle sobre un diccionario
# key = llave
# value = valor
#==============================
for k, v in numNames.items():
    print("key = " , k , ", value =" , v)

#===============================
# Parte 2 Video 3 "Funciones"
#===============================

#===================
# Primera función
#===================
def saludo():
    #=====================================
    # Documentación rápida de la función
    #=====================================
    """Esta función saluda"""
    print('¡Que pasion!, ¿cómo estás?')

#=========================
# Llamado de la función
#=========================
saludo()

#================================
# Se ejecuta pero no se asigna
#================================
salida = saludo()

#====================
# Esto no funciona
#====================
print(salida)

#=========================
# Mostrar documentación
#=========================
#help(saludo)

#=========================
# Función con argumento
#=========================
def  salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("¡Qué onda ese",nombre,"!")
salu2("Julián")
salu2("Ángel")

#===========================================
# Ahorrar trabajo del intérprete
# nombre:str la variable nombre es un str
#===========================================
def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("¡Qué onda ese" , nombre , "!")
saludos("Julián")
a = 123
print(type(a))
saludos(a)

#=================================
# Función con muchos argumentos
#=================================
def saludos_multiples(nombre1 , nombre2 , nombre3):
    """Esta función saluda a 3 personas al mismo tiempo"""
    print("Hola " , nombre1 , "," , nombre2 , "y" , nombre3)
saludos_multiples("Hugo" , "Paco" , "Luis")

#==============================================
# Función con cualquier número de argumentos
#==============================================
def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #====================================
    # end = es para ponerlo de corrido
    #====================================
    print("Hola " , end = "")
    while len(nombres) > i:
        # Último nombre
        if (i == len(nombres)-1):
            print(nombres[i])
        else:
            # Cualquier otro nombre
            print(nombres[i] , end = ", ")
        i+=1

muchos_saludos("Bosco" , "Angel" , "David" , "Tamara" , "Mili" , "Edwin" , "Lev" , "Luis" , "Abigail")

def greet(firstname , lastname):
    print('Hello' , firstname , lastname)

#==================================================
# Llamar a la función con argumentos de desorden
#==================================================
greet(lastname = 'Jobs' , firstname = 'Steve') #Se pueden especificar las variables en desorden

#========================================
# Función con argumentos escondidos **
#========================================
def greet(**person):
    #=====================================================
    # person tiene características firstname y lastname
    #=====================================================
    print('Hello ' , person['firstname'] , person['lastname'])

greet(firstname = 'Steve' , lastname = 'Jobs')
greet(lastname = 'Jobs' , firstname = 'Steve')
greet(firstname = 'Dill' , lastname = 'Gates' , age = 55) # Se pueden pasar más parametros de los necesarios

#===================================
# Función con valores por defecto
#===================================
def greet(name = 'Guest'):
    print('Hello', name)
    
greet() # Utiliza el valor dado de antemano
greet('Steve')

#=========================
# Función con resultado
#=========================
def suma(a , b):
    return a + b

#====================================
# Programación funcional
# Se pueden funciones en funciones
#====================================
total = suma(5 , suma(10 , 20))
print(total)

#===================================================
# Cálculo LAMBDA
# nombre de la funció = lambda variable : función
#===================================================
x_al_cuadrado = lambda x : x * x
a1 = x_al_cuadrado(5)
print(a1)

#==============================
# Lambda de varias variables
#==============================
suma = lambda x1 , x2 , x3 : x1 + x2 + x3
print(suma(99 , 98 , 97))

sumas = lambda *x : x[0] + x[1] + x[2] + x[3]

print(sumas(100 , 200 , 300 , 400))

#===========================================
# Uso de una función anónima
# El argumento va afuera entre párentesis
#===========================================
print((lambda x : x * x)(6)) # Función anónima


#===============================
# Función con variable global
# ¡¡¡ EVITE EL EXCESO ;)!!!
#===============================
name = 'Steve'
def greet():
    global name   # Para utilizar una variable global (que viene fuera del bloque)
    name = 'Bill'
    print('Hello ' , name)

greet()


#================================
# Parte 3 Video 3 "Calcular e"
#================================

#==============================
# Algoritmo 1
#==============================
# Serie exponencial
# Factorización de x
# Negativos con función inversa
#==============================
n = 200
x = -100.0
flag = False
if x<0:
    flag = True
    x = -x
s = 1.0
for i in range(n , 0 , -1):
    s *= x/float(i)
    s += 1.0 
if flag == True:
    s = 1/s
print(s)

#===========||
# VIDEO 4
#===========||

#====================================
# PROGRAMACIÓN ORIENTADA A OBJETOS
#====================================

#==================================
# Una clase para un objeto vacío
# No está tan vacío, necesita
# la palabra pass = pasar
#==================================

class ObjetoVacio:
    pass

#==========================
# nada es un ObjetoVacio
#==========================

nada = ObjetoVacio()
print(type(nada))

#===================
# La clase llanta
#===================

class Llanta:

    #=======================================
    # Variable cuenta es de toda la clase
    #=======================================
    
    cuenta = 0

    #=====================================
    # Función constructora de identidad
    # __init__ es una función reservada
    # comienza con uno mismo: self
    # pero puede ser otro nombre (mi)
    # parámetros de entrada = default
    #=====================================
    def __init__(mi, radio = 50 , ancho = 30 , presión = 1.5):
        # variable de la estructura completa Llanta
        Llanta.cuenta += 1
        # variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presión = presión

#==========================
# Objetos (instanciados)
#==========================

llanta1 = Llanta(50 , 30 , 1.5)
llanta2 = Llanta(presión = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40 , 30 , 1.6)

#=====================================
# Objeto que contiene otras objetos
#=====================================

class Coche:
    def __init__(mi , ll1 , ll2 , ll3 , ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(llanta1 , llanta2 , llanta3 , llanta4)

print("Total de llantas: " , Llanta.cuenta)  # Variable global de la clase
print("Presión de la llanta 4 = " , llanta4.presión)  # Presión de la ll4
print("Radio de la llanta 4 = " , llanta4.radio)
print("Presión de la llanta 1 de mi coche = " , micoche.llanta1.presión)

#===================
# Encapsulamiento
#===================

#=======================================================================
# Uso de la función de python property para poner y obtener atributos
#=======================================================================

class Estudiante:
    def __init__(mi):
        mi.__nombre = ''
    def ponerme_nombre(mi , nombre):
        print('se llamó a ponerme_nombre')
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print('se llamó a obtener_nombre')
        return mi.__nombre
    nombre = property(obtener_nombre , ponerme_nombre)

#======================================
# Crear objeto estudiante sin nombre
#======================================

estudiante = Estudiante()

#======================================================================
# Ponerle nombre usando la propiedad nombre y el método poner_nombre
# (sin tener que llamar explícitamente la función)
#======================================================================

estudiante.nombre = "Diego"

#========================================================================
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
# (sin tener que llamar explicitamente la función
#========================================================================

print(estudiante.nombre)

# Esto no funciona:
# print(estudiante.__nombre)

#======================
# Herencia de clases
#======================

class Cuadrilatero:
    def __init__(mi , a , b , c , d):
        mi.lado1 = a
        mi.lado2 = b
        mi.lado3 = c
        mi.lado4 = d

    def perimetro(mi):
        p = mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("perimetro= " , p)
        return p

#======================================
# Su hijo rectángulo
# Rectángulo es hojo de Cuadrilátero
# Rectángulo (Cuadrilatero)
#======================================

class Rectangulo(Cuadrilatero):
    def __init__(self , a , b):
        #===========================
        # Constructor de su madre
        #===========================

        super().__init__(a , b , a , b)

#======================
# Su nieto Cuadrado
# Hijo de Rectángulo
#======================

class Cuadrado(Rectangulo):
    def __init__(self , a):
        super().__init__(a , a)

    def area(self):
        area = self.lado1**2
        return area

    # def perimetro(self):
    # p = 4.0*self.lado1
    # print("perimetro =" , p)
    # return p

#=====================
# Crear un cuadrado
#=====================

cuadrado1 = Cuadrado(5)

#========================================================
# Llamar al método perímetro de su abuelo cuadrilatero
#========================================================

perimetro1 = cuadrado1.perimetro()

#==================================
# Llamar a su propio método área
#==================================

area1 = cuadrado1.area()

print("Perímetro = " , perimetro1)
print("Área = " , area1)

#===============================================================
# Sobre-escribir un método de su madre o abuela o tatarabuela
# Es volver a definir una función ya existente
#===============================================================


#================================
# VIDEO 4 PARTE 2 "Asociación"
#================================

#========================================
# La clase A tiene tres números reales
#========================================

class A:
    __a: float = 0.0
    __b: float = 0.0
    __c: float = 0.0
    
    def __init__(self , a: float , b: float , c: float):
        self.a = a
        self.b = b
        self.c = c

#=======================================
# La clase B tiene dos números reales
#=======================================

class B:
    __d: float = 0.0
    __e: float = 0.0

    def __init__(self , d: float , e: float):
        self.d = d
        self.e = e

    #===========================================
    # Método sumar todo (internos + externos)
    #===========================================

    def sumar_todo(self , aa: float , bb: float):
        x: float = self.d + self.e + aa + bb
        return x

#==============
# ASOCIACIÓN
#==============

#Usando objetos independientes
objetoA = A(1.0 , 2.0 , 3.0)
objetoB = B(4.0 , 5.0)
print(objetoB.sumar_todo(objetoA.a , objetoA.b))

#==============================================
# El objeto C tiene dos reales y un objeto A
# El objeto AA se instancia dentro de C
#==============================================

class C:
    __d: float = 0.0
    __e: float = 0.0
    __Aa: A = None

    def __init__(self, d: float , e: float):
        self.d = d
        self.e = e
        # A está instanciado adentro
        self.Aa = A(1.0 , 2.0 , 3.0)

    def sumar_todo(self):
        x: float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#===============================
# COMPOSICIÓN
# Contiene otro objeto dentro
#===============================

objetoC = C(4.0,5.0)
print(objetoC.sumar_todo())

#===========================================
# Objeto D tiene dos reales y un objeto A
# definido por fuera
#===========================================

class D:
    __d: float = 0.0
    __e: float = 0.0
    __Aa: A = None

    def __init__(self , d: float , e: float , Aa:A):
        self.d = d
        self.e = e
        self.Aa = Aa

    def sumar_todo(self):
        x: float = self.d + self.e + self.Aa.a + self.Aa.b
        return x

#==========================================
# AGREGACIÓN
# Construye el objeto agregado por fuera
#==========================================

objetoD = D(4.0 , 5.0 , objetoA)
print(objetoD.sumar_todo())


#===========||
# VIDEO 5
#===========||


