# 860. Lemonade Change

**Enlace al problema:** https://leetcode.com/problems/lemonade-change/

**criterio greedy:** Estrategia del Elemento Mayor Primero

## Enunciado 

En un puesto de limonadas, cada limonada cuesta $5. Los clientes están haciendo fila para comprarte y piden una a la vez (en el orden especificado por los billetes). Cada cliente solo comprará una limonada y pagará con un billete de $5, $10 o $20. Debes darle el cambio correcto a cada cliente para que la transacción neta sea que el cliente pague $5.

Ten en cuenta que al principio no tienes nada de cambio.

Dada una matriz de enteros bills (billetes) donde bills[i] es el billete con el que paga el $i$-ésimo cliente, devuelve true si puedes darle a cada cliente el cambio correcto, o false en caso contrario.

Restricciones:

1 <= bills.length <= 10ʌ5
bills[i] es 5, 10, or 20.

## Rendimiento

- **Complejidad de tiempo:** O(N), donde N es la longitud del arreglo bills. Se realiza una sola pasada lineal procesando cada cliente en O(1).

- **Complejidad de espacio:** O(1), ya que solo se emplean dos variables enteras (five y ten) para el estado de la caja.

## Evidencias

**Runtime**
![Runtime — Lemonade Change](evidencias/LemonadeChangeRuntime.png)

**Memory**
![Memory — Lemonade Change](evidencias/LemonadeChangeMemory.png)