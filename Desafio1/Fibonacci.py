n = int(input("Insira um número para saber se ele está na sequência de Fibonacci: "))
fiboSequence = [0, 1]

while fiboSequence[-1] < n:
    next_fibo = fiboSequence[-1] + fiboSequence[-2]
    fiboSequence.append(next_fibo)

if n in fiboSequence:
    print(f"O número {n} está na sequência de Fibonacci.")
else:
    print(f"O número {n} não está na sequência de Fibonacci.")