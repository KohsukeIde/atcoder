def final_string(N, M, S, C):
  color_positions = [[] for _ in range(M)]
  
  for i, color in enumerate(C):
      color_positions[color - 1].append(i)

  result = [None] * N
  for color, positions in enumerate(color_positions, start=1):
      k = 1 % len(positions) 
      for i, pos in enumerate(positions):
          result[pos] = S[positions[(i - k) % len(positions)]]

  return ''.join(result)


N, M = map(int, input().strip().split())
S = input().strip()
C = list(map(int, input().strip().split()))

print(final_string(N, M, S, C))