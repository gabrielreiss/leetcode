class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #para não precisar ordernar e virar um O(n log n), podemos criar um set
        #com o set, ele acha os numeros bem rapido
        #com isso precisamos verificar se o numero é o primeiro da sequencia
        #pesquisando se o n-1 existe, caso não, o n é o primeiro elemento
        #a seguir faz um loop para localizar os numeros sequenciais
        #salva na variavel de resposta se esse valor é maior do que o existente
        
        set_nums = set(nums)
        longest_s = 0
        
        for num in nums:
            if num -1 not in set_nums:
                current_num = num
                current_s = 1
                
                while current_num + 1 in set_nums:
                    current_num += 1
                    current_s += 1
                longest_s = max(longest_s, current_s)

        return longest_s
