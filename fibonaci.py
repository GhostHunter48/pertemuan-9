def fibonacci(n):
    if n < 1:
        return "Masukkan bilangan positif"
    elif n == 1:
        return [0]
    else:
        hasil = [0, 1]
        for i in range(2, n):
            hasil.append(hasil[i-1] + hasil[i-2])
        return hasil

n = 10
print(fibonacci(n))
