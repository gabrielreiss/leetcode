# Descrição do Problema
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


## Pensamento por trás da solução
Em Python, usar Counter().

No geral:
1.  Usar hashmaps, como dicionários. A ideia é criar algo com chave e valor, a chave é o número e o valor é a quantidade de vezes que ele aparece. 
2. Percorre o array, e vai adicionando a quantidade de vezes.
3. Para achar o que tem mais valor e não utilizar qualquer algoritmo de ordenação, salva em uma lista de listas, para caso tenha números com quantidades repetidas.
4. Salva os valores do dicionário na lista conforme a quantidade de vezes que ele aparece.
5. Percorre a lista de trás para frente e retorna o primeiro valor não nulo.

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
| Python | 11 ms | 24.2 MB | 

