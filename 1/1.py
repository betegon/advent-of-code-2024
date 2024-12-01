from utils import read_input

input = read_input()
left = [int(n[0]) for n in input]
right = [int(n[1]) for n in input]
distance = sum([abs(x - y) for x, y in zip(sorted(left), sorted(right))])
print(distance) # solution: 2086478 

"""
Complejidad en tiempo:
1.	read_input():
	•	Dependiendo de cómo esté implementado, asume que lee n líneas del archivo y devuelve una lista de listas o tuplas.
	•	Complejidad de lectura: O(n), donde n es el número de líneas en el archivo.
2.	Construcción de left y right:
	•	Cada comprensión de lista (left y right) recorre las n líneas de input y accede a los índices 0 y 1 respectivamente.
	•	Complejidad de ambas comprensiones: O(n).
3.	Ordenar las listas (sorted(left) y sorted(right)):
	•	La función sorted utiliza un algoritmo de ordenación eficiente como Timsort, con complejidad O(k \log k), donde k es el tamaño de la lista.
	•	Ambas listas tienen tamaño n, por lo que la complejidad de ordenar es O(n \log n) para cada lista.
	•	Complejidad total para ordenar: O(n \log n) + O(n \log n) = O(n \log n).
4.	Calcular la distancia:
	•	El bucle que itera sobre zip(sorted(left), sorted(right)) tiene una complejidad lineal O(n), ya que itera una sola vez sobre los n elementos de ambas listas combinadas.

Complejidad total en tiempo:
 O(n) + O(n) + O(n \log n) + O(n) = O(n \log n) 


Complejidad en espacio:
1.	read_input():
	•	Supone que devuelve una lista de n elementos. Cada elemento contiene dos valores (una lista o tupla).
	•	Complejidad espacial: O(n).
2.	left y right:
	•	Cada comprensión de lista crea una nueva lista de tamaño n.
	•	Complejidad espacial combinada: O(n) + O(n) = O(n).
3.	Ordenar las listas (sorted(left) y sorted(right)):
	•	sorted devuelve nuevas listas ordenadas, por lo que crea copias de tamaño n.
	•	Complejidad espacial combinada para ordenar: O(n) + O(n) = O(n).
4.	Cálculo de la distancia:
	•	zip crea un objeto iterable sin ocupar memoria adicional.
	•	El cálculo de la suma no requiere espacio adicional significativo.

Complejidad total en espacio:
 O(n) + O(n) + O(n) = O(n) 
"""