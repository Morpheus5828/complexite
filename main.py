def iterative_fibo(n):
    n += 1
    fibo = [0] * n
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, n):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n - 1]


def recursive_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibo(n - 1) + recursive_fibo(n - 2)


def prod_mat(A, B):
    height = len(A)
    width = len(B[0])
    P = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            for k in range(height):
                P[i][j] += A[i][k] * B[k][j]
    return P


def exp_mat(A, n):
    bitmap = []
    i = 0
    while n > 1:
        bitmap.append(n % 2 == 0)
        i += 1
        n //= 2
    RES = A
    for j in range(i - 1, -1, -1):
        if bitmap[j]:
            RES = prod_mat(RES, RES)
        else:
            RES = prod_mat(prod_mat(RES, RES), A)
    return RES


def expo_fibo(n):
    if n == 0:
        return 0
    n -= 1
    mat = [[0, 1], [1, 1]]
    vec = [[0], [1]]
    return prod_mat(exp_mat(mat, n), vec)[1][0]


print(iterative_fibo(25))

print(recursive_fibo(25))

print(expo_fibo(25))