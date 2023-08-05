N = int(input())
S = [input() for _ in range(N)]

sticks = set()
for s in S:
    sticks.add(min(s, s[::-1]))

print(len(sticks))
N = int(input())
S = [input() for _ in range(N)]

sticks = set()
for s in S:
    sticks.add(min(s, s[::-1]))

print(len(sticks))
