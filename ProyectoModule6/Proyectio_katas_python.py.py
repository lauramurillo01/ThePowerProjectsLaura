# # PROYECTO LÓGICA: Katas de Python
#
# ### Modulo 6 
#

from functools import reduce

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frequencia_letras(string):
    """
    calcula la frecuencia de cada letra en la cadena dada.

    Parametros:
    string (str): el string de entrada a analizar.

    Returns:
    dict: Un diccionario con las letras como claves y sus frecuencias como valores.
    """
    string = string.lower() # convertir a minúscula  
    
    frequencies = {} #inizializar un diccionario vacío para las frecuencias de las letras
    
    for letra in string:
        if letra.isalpha(): #si la letra es una letra, la contamos
            if letra in frequencies:
                frequencies[letra] += 1 #si letra en diccionario, incrementa su valor en 1
            # si la letra no está en el diccionario, agregarla con un conteo de 1
            else:
                frequencies[letra] = 1
                
    return frequencies


frequencia_letras('patata')

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

def doble_lista(lista):
    """
    Duplicar cada elemento en la lista dada.

    Parametros:
    lista (list): la lista de entrada a duplicar.

    Returns:
    list: Una nueva lista con cada elemento duplicado.
    """
    return [elemento * 2 for elemento in lista]


lista = 1,3,6,7,5,4
doble_lista(lista)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def palabras_objetivo(lista_palabras, objetivo):
    """
    Filtra las palabras en la lista que contienen la palabra objetivo.

    Parametros:
    lista_palabras (list): la lista de palabras a filtrar.
    objetivo (str): la palabra objetivo a buscar en cada palabra de la lista.

    Returns:
    list: Una nueva lista con las palabras que contienen la palabra objetivo.
    """
    coincidencias = []
 
    for palabra in lista_palabras:
        if objetivo in palabra:
            coincidencias.append(palabra)
 
    return coincidencias


lista = 'hola', 'caracola', 'patata', 'olas', 'manzana', 'olesa', 'microondas'
palabras_objetivo(lista, 'as')
palabras_objetivo(lista, 'ola')

# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_listas(lista1, lista2):
    """
    Calcula la diferencia entre dos listas de números.

    Parametros:
    lista1 (list): la primera lista de números.
    lista2 (list): la segunda lista de números.

    Returns:
    list: Una nueva lista con la diferencia entre los elementos correspondientes de las dos listas.
    """
    resultado = map(lambda a, b: a - b, lista1, lista2)
    return list(resultado)


l1 = 2,5,7,8,3,10,2,4,6
l2 = 1,6,7,9,0,45,4,3,32
diferencia_listas(l1, l2)

# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def evaluar_notas (lista, nota_aprobado=5):
    """
    Calcula através de una seria de notas en lista si la media es mayor (aprobado) que nota_aprobado o menor (suspenso).

    Parametros:
    lista (int): lista de números.
    nota_aprobado (int): numero para calcular estado.

    Returns:
    media (int): media de los numeros en la lista 
    estado (str): "aprobado" o "suspenso" segun si la media es mayor o menor a la nota_aprobado.
    """
    
    media = sum(lista) / len(lista)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
 
    return (media, estado)


lista = 3,6,9,9,8,7,6,5,1,2,3
evaluar_notas(lista)
evaluar_notas(lista, 4.5)
evaluar_notas(lista, 6)

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    """
    Calcula el factorial de un número n.

    Parametros:
    n (int): el número para calcular su factorial.

    Returns:
    int: El factorial del número dado.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

factorial(4)
factorial(10)

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    """
    Convierte una lista de tuplas a una lista de strings.

    Parametros:
    lista_tuplas (list): lista de tuplas a convertir.

    Returns:
    list: Una nueva lista con las tuplas convertidas a strings.
    """
    return list(map(str, lista_tuplas))


lista_tuplas = [(1, 2), (3, 4), (5, 6), ('a', 'b')]
tuplas_a_strings(lista_tuplas)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():
    """
    Pide al usuario dos números e intenta dividirlos.
    Maneja excepciones para valores no numéricos y división por cero.
    """
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        resultado = num1 / num2
        print(f"La división fue exitosa: {num1} / {num2} = {resultado}")
        
    except ValueError:
        print("Error: Ingresaste un valor no numérico. Por favor, ingresa números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except Exception as e:
        print(f"Error inesperado: {e}")



dividir_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def mascotas_prohibidas(lista):
    """
    Toma una lista de nombres de mascotas y devuelve una nueva lista excluyendo aquellas prohibidas.

    Parametros:
        lista (str): lista de mascotas

    Returns:
        lista (str): lista de mascotas excluyendo mascotas prohibidas
    """
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista))


lista_mascotas = ["Gato", "Perro", "Mapache", "Cocodrilo", "Hámster"]
mascotas_prohibidas(lista_mascotas)

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías"""
    pass

def calculo_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Parametros:
    numeros (list): lista de números.
    
    Returns:
    float: El promedio de los números en la lista.
    
    Raises:
    ListaVaciaError: Si la lista está vacía.
    """
    try:
        if len(numeros) == 0:
            raise ListaVaciaError("Error: La lista no puede estar vacía.")
        promedio = sum(numeros) / len(numeros)
        return promedio
    except ListaVaciaError as e:
        print(f"Excepción capturada: {e}")
        return None


calculo_promedio([10, 20, 30, 40])
calculo_promedio([])

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    """Pide al usuario introducir su edad y maneja las excepciones.
    """
    try:
        edad = int(input("Introduce to edad: "))
        if edad < 0 or edad > 120:
            print("Error: la edad debe estar entre 0 y 120")
        else: 
            print("Tu edad es:", edad)
    except ValueError:
        print("Error: debes introducir un número entero")


pedir_edad()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabras(frase):
    """
    Recibe una frase y devuelve una lista con la longitud de cada palabra.

    Args:
        frase (str): la frase de entrada a analizar.

    Returns:
        list: una lista de enteros con la longitud de cada palabra de la frase.
    """
    palabras = frase.split()
    lista = map(len, palabras)
    return list(lista)


frase = "Hola me gustan las galletas y la fruta"
longitud_palabras(frase)

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def letras_mayus_minusculas(caracteres):
    """
    Convierte un conjunto de caracteres en una lista de tuplas
    con cada letra en mayúsculas y minúsculas, sin repetir letras.

    Parametros:
    caracteres (str): cadena de caracteres a procesar.

    Returns:
    list: lista de tuplas (mayuscula, minuscula) por cada letra única.
    """
    letras_unicas = list(dict.fromkeys(c.lower() for c in caracteres if c.isalpha()))
    
    return list(map(lambda c: (c.upper(), c.lower()), letras_unicas))


letras_mayus_minusculas("Hola Mundo")

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def palabras_comienzan_con(lista_palabras, letra):
    """
    Devuelve las palabras de la lista que comienzan con la letra especificada.

    Args:
        lista_palabras (list): lista de palabras a filtrar.
        letra (str): letra por la que deben empezar las palabras.

    Returns:
        list: lista con las palabras que comienzan por la letra indicada.

    Raises:
        ValueError: si 'letra' no es una cadena no vacía.
    """
    if not isinstance(letra, str) or len(letra) == 0:
        raise ValueError("la 'letra' debe ser una cadena no vacía")
    letra = letra.lower()
    return list(filter(lambda p: isinstance(p, str) and p.lower().startswith(letra), lista_palabras))


frase = "Hola me gustan las galletas y la fruta"
palabras = frase.split()
palabras_comienzan_con(palabras, 'g')

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: [numero + 3 for numero in lista]  

lista = 3,6,7,7,5,51,3,9
sumar_tres(lista)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_mas_largas_que_n(texto, n):
    """
    Devuelve las palabras de un texto cuya longitud es mayor que n.

    Args:
        texto (str): texto del que se extraen las palabras.
        n (int): longitud mínima (exclusiva) que debe superar cada palabra.

    Returns:
        list: lista de palabras con longitud mayor que n.
    """
    palabras = texto.split()
    resultado = filter(lambda palabra: len(palabra) > n, palabras)
    return list(resultado) 

# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572). Usa la función reduce()

def digitos_a_numero(lista_digitos):
    """
    Convierte una lista de dígitos en el número entero que representan.

    Args:
        lista_digitos (list): lista de dígitos (int), en el orden en que forman el número.

    Returns:
        int: el número resultante de unir los dígitos de la lista.
    """
    resultado = reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)
    return resultado

lista = [5,7,2]
digitos_a_numero(lista)

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

def calificacion_alta(estudiante):
    """
    Comprueba si un estudiante tiene una calificación igual o superior a 90.

    Args:
        estudiante (dict): diccionario con al menos la clave "calificacion".

    Returns:
        bool: True si la calificación es mayor o igual a 90, False en caso contrario.
    """
    return estudiante["calificacion"] >= 90
 
 
def estudiantes_destacados(lista_estudiantes):
    """
    Filtra los estudiantes con calificación igual o superior a 90.

    Args:
        lista_estudiantes (list): lista de diccionarios con datos de estudiantes.

    Returns:
        list: lista de diccionarios de los estudiantes destacados.
    """
    resultado = filter(calificacion_alta, lista_estudiantes)
    return list(resultado)


lista_estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 80},
        {"nombre": "Marta", "edad": 19, "calificacion": 92},
    ]
print(estudiantes_destacados(lista_estudiantes))

# 19. Crea una función lambda que filtre los números impares de una lista dada.

filtro_impares = lambda lista: [numero for numero in lista if numero % 2 != 0]

lista = 3,4,6,7,8,9,1,10,13,19
filtro_impares(lista)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def filtrar_enteros(elementos):
    """
    Devuelve una lista solo con los valores enteros de la lista dada.
    """
    return list(filter(lambda x: isinstance(x, int), elementos))


lista_mixta = [1, "dos", 3, "cuatro", 5, "6", 7, 8.7]
filtrar_enteros(lista_mixta)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda numero: numero**3

cubo(3)

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .

def producto_total(lista_numeros):
    """
    Calcula el producto de todos los valores de una lista de números.

    Args:
        lista_numeros (list): lista de números.

    Returns:
        int | float: el producto total de todos los elementos de la lista.
    """
    return reduce(lambda x, y: x * y, lista_numeros)

lista = 3,6,7,8,4,1,3,2
producto_total(lista)

# 23. Concatena una lista de palabras.Usa la función reduce() .

def concatenar_palabras(lista_palabras):
    """
    Concatena todas las palabras de una lista en una única cadena, separadas por espacios.

    Args:
        lista_palabras (list): lista de palabras (str) a concatenar.

    Returns:
        str: cadena resultante de unir todas las palabras.
    """
    return reduce(lambda x, y: x + " " + y, lista_palabras)

lista = "arbol", "hola", "caracola", "camiseta"
concatenar_palabras(lista)

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() .

def diferencia_total(lista_numeros):
    """
    Calcula la diferencia acumulada entre los valores de una lista,
    restando cada elemento al resultado anterior de izquierda a derecha.

    Args:
        lista_numeros (list): lista de números.

    Returns:
        int | float: resultado de restar sucesivamente todos los elementos de la lista.
    """
    return reduce(lambda x, y: x - y, lista_numeros)

lista = 2,9,3,8,5,7
diferencia_total(lista)

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    """
    Cuenta el número de caracteres de una cadena de texto.

    Args:
        cadena (str): cadena de texto a analizar.

    Returns:
        int: número total de caracteres de la cadena.
    """
    return len(cadena)


cadena = "Hola que tal me llamo Laura"
contar_caracteres(cadena)

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

resto_division = lambda a, b: a % b

resto_division(3, 2)

# 27. Crea una función que calcule el promedio de una lista de números.

def promedio(lista_numeros):
    """
    Calcula el promedio (media) de una lista de números.

    Args:
        lista_numeros (list): lista de números.

    Returns:
        float: el promedio de los números de la lista.
    """
    return sum(lista_numeros) / len(lista_numeros)

lista = 2,5,6,7,10,8,9,8,5,4,3,2,2,1
promedio(lista)

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    """
    Busca y devuelve el primer elemento que aparece repetido en una lista.

    Args:
        lista (list): lista de elementos a analizar.

    Returns:
        El primer elemento duplicado encontrado, o None si no hay ninguno.
    """
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento 
        else:
            vistos.add(elemento)
    return None

lista = 2,5,6,7,5,4,3,2,2,1
primer_duplicado(lista)

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarar(valor):
    """
    Convierte un valor en cadena de texto y enmascara todos sus caracteres
    con '#', dejando visibles solo los últimos cuatro.

    Args:
        valor: valor de cualquier tipo que se pueda convertir a cadena.

    Returns:
        str: cadena enmascarada, o el propio texto si tiene 4 caracteres o menos.
    """
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    parte_enmascarada = "#" * (len(texto) - 4)
    ultimos_cuatro = texto[-4:]
    return parte_enmascarada + ultimos_cuatro

enmascarar("HolaComoEstas")
enmascarar(7394020346)

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """
    Comprueba si dos palabras son anagramas entre sí.

    Args:
        palabra1 (str): primera palabra a comparar.
        palabra2 (str): segunda palabra a comparar.

    Returns:
        bool: True si ambas palabras están formadas por las mismas letras, False en caso contrario.
    """
    letras1 = sorted(palabra1.replace(" ", "").lower())
    letras2 = sorted(palabra2.replace(" ", "").lower())
    return letras1 == letras2

p1 = "manzana"
p2 = "zamanan"
son_anagramas(p1, p2)

# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    """
    Pide al usuario una lista de nombres separados por comas y, después,
    un nombre a buscar dentro de esa lista. Informa si el nombre se encuentra.

    Raises:
        Exception: si el nombre buscado no está en la lista introducida.
    """
    entrada = input("Introduce una lista de nombres separados por comas: ")
    lista_nombres = entrada.split(",")
 
    # quitamos los espacios en blanco que pueda tener cada nombre
    nombres_limpios = []
    for nombre in lista_nombres:
        nombres_limpios.append(nombre.strip())
 
    nombre_buscado = input("¿Qué nombre quieres buscar? ")
 
    if nombre_buscado in nombres_limpios:
        print(f"El nombre '{nombre_buscado}' ha sido encontrado.")
    else:
        raise Exception(f"El nombre '{nombre_buscado}' no está en la lista.")
    
buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    """
    Busca el puesto de un empleado a partir de su nombre completo.

    Args:
        nombre_completo (str): nombre completo del empleado a buscar.
        lista_empleados (list): lista de diccionarios con las claves "nombre" y "puesto".

    Returns:
        str: el puesto del empleado si se encuentra, o un mensaje indicando que no trabaja aquí.
    """
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return "Esta persona no trabaja aquí."


lista_empleados = [{"nombre": "Ana García", "puesto": "Desarrolladora"},
                   {"nombre": "Luis Pérez", "puesto": "Diseñador"}]

print(buscar_puesto("Ana García", lista_empleados))
print(buscar_puesto("Carlos Ruiz", lista_empleados))

# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: [a + b for a, b in zip(lista1, lista2)]

l1 = 2,6,8,9,65,5,6
l2 = 1,3,3,5,6,7,10
sumar_listas(l1, l2)

# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
# Código a seguir:
#     1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#     2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#     3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#     4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#     5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#     6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
#
# Caso de uso:
#
#     1. Crear un árbol.
#     2. Hacer crecer el tronco del árbol una unidad.
#     3. Añadir una nueva rama al árbol.
#     4. Hacer crecer todas las ramas del árbol una unidad.
#     5. Añadir dos nuevas ramas al árbol.
#     6. Retirar la rama situada en la posición 2.
#     7. Obtener información sobre el árbol.

class Arbol:
    """Representa un árbol genérico con un tronco y una lista de ramas."""

    def __init__(self):
        """Inicializa el árbol con un tronco de tamaño 1 y sin ramas."""
        self.tronco = 1
        self.ramas = []
 
    def crecer_tronco(self):
        """Aumenta en 1 el tamaño del tronco."""
        self.tronco += 1
 
    def nueva_rama(self):
        """Añade una nueva rama al árbol, con tamaño inicial 1."""
        self.ramas.append(1)
 
    def crecer_ramas(self):
        """Aumenta en 1 el tamaño de todas las ramas existentes."""
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
 
    def quitar_rama(self, posicion):
        """
        Elimina la rama situada en la posición indicada.

        Args:
            posicion (int): índice de la rama a eliminar.
        """
        self.ramas.pop(posicion)
 
    def info_arbol(self):
        """
        Devuelve el estado actual del árbol.

        Returns:
            dict: diccionario con el tamaño del tronco, el número de ramas
                y la lista con el tamaño de cada rama.
        """
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "ramas": self.ramas,
        }

# Comprobación de que todos los metodos funcionan correctamente
arbol = Arbol()

print("Estado inicial:", arbol.info_arbol())

arbol.crecer_tronco()
print("Después de crecer_tronco:", arbol.info_arbol())

arbol.nueva_rama()
print("Después de nueva_rama:", arbol.info_arbol())

arbol.crecer_ramas()
print("Después de crecer_ramas:", arbol.info_arbol())

arbol.nueva_rama()
arbol.nueva_rama()
print("Después de añadir dos nuevas ramas:", arbol.info_arbol())

arbol.quitar_rama(2)
print("Después de quitar la rama en posición 2:", arbol.info_arbol())

# Comprobaciones
assert arbol.tronco == 2
assert arbol.ramas == [2, 1]
assert arbol.info_arbol() == {"tronco": 2, "numero_ramas": 2, "ramas": [2, 1]}

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
#     1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#     2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#     3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
#     4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#
# Caso de uso:
#
#     1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#     PROYECTO LÓGICA: Katas de Python 3
#     2. Agregar 20 unidades de saldo de "Bob".
#     3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#     4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    """Representa a un usuario de un banco, con su nombre, saldo y tipo de cuenta."""

    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Inicializa un usuario del banco.

        Args:
            nombre (str): nombre del usuario.
            saldo (float): saldo inicial de la cuenta.
            cuenta_corriente (bool): indica si el usuario tiene cuenta corriente.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
 
    def retirar_dinero(self, cantidad):
        """
        Retira una cantidad de dinero del saldo del usuario.

        Args:
            cantidad (float): cantidad a retirar.

        Raises:
            Exception: si la cantidad a retirar es mayor que el saldo disponible.
        """
        if cantidad > self.saldo:
            raise Exception("No hay saldo suficiente para retirar esa cantidad.")
        self.saldo -= cantidad
 
    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Transfiere dinero desde otro usuario hacia este usuario.

        Args:
            otro_usuario (UsuarioBanco): usuario del que sale el dinero.
            cantidad (float): cantidad a transferir.

        Raises:
            Exception: si el otro usuario no tiene saldo suficiente.
        """
        if cantidad > otro_usuario.saldo:
            raise Exception("El usuario que transfiere no tiene saldo suficiente.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
 
    def agregar_dinero(self, cantidad):
        """
        Añade una cantidad de dinero al saldo del usuario.

        Args:
            cantidad (float): cantidad a añadir.
        """
        self.saldo += cantidad

# CASO DE USO 

Alicia = UsuarioBanco("Alicia", 100, True)
Bob = UsuarioBanco("Bob", 50, True)

try:
    Bob.agregar_dinero(40)
    print("Saldo de Bob después de agregar 20:", Bob.saldo)

    Alicia.transferir_dinero(Bob, 80)
    print("Saldo de Alicia después de recibir 80 de Bob:", Alicia.saldo)
    print("Saldo de Bob después de transferir 80:", Bob.saldo)

    Alicia.retirar_dinero(50)
    print("Saldo de Alicia después de retirar 50:", Alicia.saldo)
except Exception as e:
    print("Error en el caso de uso:", e)

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# Código a seguir:
#     1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
#     2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
#     3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
#     4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
#
# Caso de uso:
#
#     Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en un texto.

    Args:
        texto (str): texto a analizar.

    Returns:
        dict: diccionario con cada palabra como clave y su número de apariciones como valor.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo
 
 
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza todas las apariciones de una palabra por otra en un texto.

    Args:
        texto (str): texto original.
        palabra_original (str): palabra que se quiere sustituir.
        palabra_nueva (str): palabra por la que se sustituye.

    Returns:
        str: el texto con las palabras reemplazadas.
    """
    return texto.replace(palabra_original, palabra_nueva)
 
 
def eliminar_palabra(texto, palabra):
    """
    Elimina todas las apariciones de una palabra concreta de un texto.

    Args:
        texto (str): texto original.
        palabra (str): palabra que se quiere eliminar.

    Returns:
        str: el texto resultante sin esa palabra.
    """
    palabras = texto.split()
    palabras_filtradas = []
    for p in palabras:
        if p != palabra:
            palabras_filtradas.append(p)
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto llamando a la función correspondiente según la opción indicada.

    Args:
        texto (str): texto a procesar.
        opcion (str): operación a realizar ("contar", "reemplazar" o "eliminar").
        *args: argumentos adicionales necesarios según la opción elegida
            (por ejemplo, palabra_original y palabra_nueva para "reemplazar").

    Returns:
        El resultado de la operación elegida (dict o str), o un mensaje
        indicando que la opción no es válida.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        return "Opción no válida"

texto_prueba = "el perro corre y el gato duerme y el perro ladra"

print(procesar_texto(texto_prueba, "contar"))
print(procesar_texto(texto_prueba, "reemplazar", "perro", "lobo"))
print(procesar_texto(texto_prueba, "eliminar", "el"))

# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def periodo_del_dia(hora):
    """
    Determina si, según la hora dada, es de día, de tarde o de noche.

    Args:
        hora (int): hora del día en formato 24 horas (0-23).

    Returns:
        str: "día", "tarde" o "noche" según corresponda.
    """
    if hora >= 6 and hora < 12:
        return "día"
    elif hora >= 12 and hora < 20:
        return "tarde"
    else:
        return "noche"
    

periodo_del_dia(11)

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
#

def calificacion_en_texto(nota):
    """
    Convierte una calificación numérica en su equivalente en texto.

    Args:
        nota (int | float): calificación numérica del alumno (0-100).

    Returns:
        str: "excelente", "muy bien", "bien" o "insuficiente" según la nota.
    """
    if nota >= 90:
        return "excelente"
    elif nota >= 80:
        return "muy bien"
    elif nota >= 70:
        return "bien"
    else:
        return "insuficiente"
    

calificacion_en_texto(90)
calificacion_en_texto(4)

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
#

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica según su tipo y sus medidas.

    Args:
        figura (str): tipo de figura ("rectangulo", "circulo" o "triangulo").
        datos (tuple): medidas necesarias para el cálculo (base y altura para
            rectángulo o triángulo; radio para círculo).

    Returns:
        float: el área calculada, o un mensaje indicando que la figura no es reconocida.
    """
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        radio = datos[0]
        return 3.1416 * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no reconocida"
    
calcular_area("triangulo", (2,3))

# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
#
#     1. Solicita al usuario que ingrese el precio original de un artículo.
#     2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#     3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#     4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.
#     5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#     6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def calcular_compra():
    """
    Calcula el precio final de una compra, aplicando un descuento si el
    usuario indica que tiene un cupón. Pide todos los datos necesarios
    al usuario por teclado.
    """
    precio = float(input("Introduce el precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ")
 
    if tiene_cupon.lower() == "si":
        descuento = float(input("Introduce el valor del cupón de descuento: "))
        if descuento > 0:
            precio_final = precio - descuento
            print(f"El descuento es de: {descuento}")

        else:
            precio_final = precio
    else:
        precio_final = precio
    
    print(f"El precio del producto es: {precio}")
    print(f"El precio final de la compra es: {precio_final}")

calcular_compra()
