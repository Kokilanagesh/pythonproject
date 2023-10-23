def multiplication_table(factor, n):
    for i in range(1, n + 1):
        product = factor * i
        print(f"{factor} * {i} = {product}")
factor = 2
n = 10
multiplication_table(factor, n)



