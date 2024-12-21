# Descrição do Problema

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109

## Pensamento por trás da solução

para não precisar ordernar e virar um O(n log n), podemos criar um set
com o set, ele acha os numeros bem rapido
com isso precisamos verificar se o numero é o primeiro da sequencia
pesquisando se o n-1 existe, caso não, o n é o primeiro elemento
a seguir faz um loop para localizar os numeros sequenciais
salva na variavel de resposta se esse valor é maior do que o existente

## Linguagens desenvolvidas

- [x] Python 
- [ ] C
- [ ] C++
- [ ] C#
- [ ] Java
- [ ] Rust
- [ ] Go
- [ ] TypeScript
- [ ] Scala

## Desempenho
| Linguagem | Runtime | Memory | Complexity
| --- | --- | --- | ---
| Python | 5306 ms | 33.4 MB | Simple

