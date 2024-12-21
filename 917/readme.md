# Descrição do Problema

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
- 1 <= s.length <= 100
- s consists of characters with ASCII values in the range [33, 122].
- s does not contain '\"' or '\\'.

## Pensamento por trás da solução
1. Inverter só as letras, portanto precisa verificar se é uma letra.
2. Usando dois ponteiros, o primeiro deles vai começar no inicio da string e o segundo vai começar no final da string, ambos percorrendo a string até se encontrarem.
3. O primeiro ponteiro percorre até encontrar uma letra, deixa ele parado lá.
4. O segundo ponteiro percorre a string pela ordem inversa até encontrar uma letra.
5. Quando ambos encontrarem a proxima letra, faz a troca.
6. Para fazer a troca, talvez precise de uma variável auxiliar. 
7. Segue o fluxo até ambos os ponteiros estiverem na mesma casa.


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
| Python | 0 ms | 17.7 MB | 

