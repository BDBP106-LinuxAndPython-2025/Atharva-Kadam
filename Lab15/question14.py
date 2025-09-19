#fibonacci numbers
#Method1
f0, f1 = 0, 1
for _ in range(25):
    print(f0, end=' ')
    f0, f1 = f1, f0 + f1
#Method2
    f0 = 0
    f1 = 1

    for i in range(25):
        print(f0)
        f2 = f0 + f1
        f0 = f1
        f1 = f2