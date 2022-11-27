for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = input().split()
    index = n - (k%n)
    print(*arr[index:n] + arr[:index])