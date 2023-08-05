def max_free_days(N, D, S):
    counter = 0
    max_counter = 0
    
    for day in range(D):
        if all(S[i][day] == 'o' for i in range(N)):
            counter += 1
            max_counter = max(max_counter, counter)
        else:
            counter = 0
    
    return max_counter

N, D= map(int, input().split())
S = [input() for _ in range(N)]
print(max_free_days(N, D, S))