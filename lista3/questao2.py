def calc_fatorial(i):
    if i == 0:
        return 1
    else:
        return i * calc_fatorial(i-1)

num = 7
resultado = calc_fatorial(num)
print('O fatorial é', resultado)
