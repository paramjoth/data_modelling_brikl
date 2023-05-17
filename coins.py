from itertools import combinations

def coin_sum(coins,input):
    for i in range(1,len(coins)):
        coin_combinations = list(combinations(coins,i))
        #print(coin_combinations)
        for j in coin_combinations:
            if sum(list(j)) == input:
                coin_len = len(list(j))
                return coin_len,j
    return -1


Coins1 = [1, 5, 7, 9, 11]
Input1 = 25
Coins2 = [1, 5, 7, 9, 11]
Input2 = 14
Coins3 = [7, 9]
Input3 = 20
print(coin_sum(Coins1,Input1))
print(coin_sum(Coins2,Input2))
print(coin_sum(Coins3,Input3))
