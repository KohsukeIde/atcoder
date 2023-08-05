def minimum_length(N, S):
    left = 0
    right = 0
    char_count = {char: 0 for char in "ABC"}
    
    for i in range(3):
        char_count[S[i]] += 1
        right = i
    
    while 0 in char_count.values():
        right += 1
        char_count[S[right]] += 1
    
    while all(val > 1 for val in char_count.values()):
        char_count[S[left]] -= 1
        left += 1
    return right - left + 1
 
N = map(int, input())
S = input()
 
print(minimum_length(N, S))