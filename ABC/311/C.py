def find_cycle(N, A):
    adj = [0] + A
 
    slow = fast = 1
 
 
    while True:
        slow = adj[slow]
        fast = adj[adj[fast]]
        if slow == fast:
            break
 
    fast = 1
    while slow != fast:
        slow = adj[slow]
        fast = adj[fast]
 
    cycle = [slow]
    while True:
        slow = adj[slow]
        if slow == cycle[0]:
            break
        cycle.append(slow)
 
 
    start = cycle[0]
    cycle = [start]
    while adj[start] != cycle[0]:
        cycle.append(adj[start])
        start = adj[start]
 
    return cycle
 
N = int(input())
A = list(map(int, input().split()))
 
res = find_cycle(N, A)
print(len(res))
print(*res)