if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a=max(arr)
    arr = [x for x in arr if x != a]  
    b=max(arr)
    print(b)
