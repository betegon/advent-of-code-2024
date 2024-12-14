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
"""

"""
TypeScript equivalent:

interface InputLine {
  left: number;
  right: number;
}

function readInput(): InputLine[] {
  // Implementation would depend on input source
  return [];
}

function calculateSimilarity(input: InputLine[]): number {
  const left = input.map(line => line.left);
  const right = input.map(line => line.right);
  
  // Create frequency counter for right array
  const rightCounts = new Map<number, number>();
  right.forEach(num => {
    rightCounts.set(num, (rightCounts.get(num) || 0) + 1);
  });

  // Calculate similarity
  return left.reduce((sum, num) => 
    sum + num * (rightCounts.get(num) || 0), 0);
}

// Usage:
const input = readInput();
const similarity = calculateSimilarity(input);
console.log(similarity); // 24941624

/*
Time Complexity:
• Building Map for right array: O(n)
• Iterating left array for similarity: O(m) 
• Total: O(n + m) = O(n)

Space Complexity:
1. Space for Map:
  • Map stores unique numbers from right with frequencies
  • If k unique numbers in right, Map size is O(k), where k ≤ m
2. Space for other variables:
  • left and right arrays from input take O(n) and O(m)
  • No additional significant data structures created
Total space complexity: O(k + n + m) = O(n + m)
*/
"""
