def minimum_payment(N, P, Q, D):
    min_cost_dish = min(D)
    cost_with_coupon = Q + min_cost_dish
    return min(cost_with_coupon, P)

N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
print(minimum_payment(N, P, Q, D))