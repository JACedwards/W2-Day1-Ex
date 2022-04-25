number = range(1001)

for n in number:
    n = n**3
    if n < 1000:
        print(n)
    else:
        break