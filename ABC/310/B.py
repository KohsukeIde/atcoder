def is_strictly_superior_product(N, M, products):
    for i in range(N):
        for j in range(N):
            if i != j:
                Pi, Ci, Fi = products[i]
                Pj, Cj, Fj = products[j]
                if Pi >= Pj and set(Fi).issubset(set(Fj)) and (Pi > Pj or len(Fi) < len(Fj)):
                    return "Yes"
    return "No"
 
N, M = map(int, input().split())
products = []
for _ in range(N):
    product = list(map(int, input().split()))
    Pi = product[0]
    Ci = product[1]
    Fi = product[2:]
    products.append((Pi, Ci, Fi))
 
print(is_strictly_superior_product(N, M, products))