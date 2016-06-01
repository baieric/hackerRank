# Solution to https://www.hackerrank.com/challenges/chief-hopper

n = int(input())
arr = [int(x) for x in input().split(" ")]
energy = arr[n-1] // 2
if(arr[n-1] % 2 == 1):
    energy += 1
i = n - 2
while i >= 0:
    if (energy + arr[i]) % 2 == 0:
        energy = (energy + arr[i])//2
    else:
        energy = (energy + arr[i])//2 + 1
    i -= 1
print(energy)
