from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""from utils import read_input
from collections import Counter

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
right_counts = Counter(right)
similarity = sum(num*right_counts.get(num, 0) for num in left)
print(similarity) # solution: 24941624

"""
Complejidad tiempo:
•	Construir Counter(right): O(n), donde n es el tamaño de right.
•	Recorrer left para calcular la similitud: O(m), donde n es el tamaño de left.
•	Total: O(n + m) = o (n).


Complejidad espacio:
1. Espacio para Counter(right):
  •	El diccionario creado por Counter almacena cada número único de right junto con su frecuencia.
  •	Si hay k números únicos en right, el tamaño del diccionario es O(k), donde k \leq m.
 2. Espacio para otras variables:
  •	left y right se crean al desempaquetar el input, ocupando O(n) y O(m), respectivamente.
  •	No se crean estructuras adicionales de tamaño significativo.
Complejidad total en espacio:
 O(k) + O(n) + O(m) = O(n + m) 
"""