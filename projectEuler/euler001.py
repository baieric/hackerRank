t = int(input());
for i in range(t):
    n = int(input())
    threes = (n-1) // 3
    fives = (n-1) // 5
    fifteens = (n-1) // 15
    sum = 3*(threes * (threes + 1))//2 + 5*(fives* (fives+1))//2 - 15*(fifteens * (fifteens+1))//2
    print(str(int(sum)))
