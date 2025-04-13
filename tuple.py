if __name__ == '__main__':
    n = int(input())
    integer = map(int, input().split())
    t=tuple(map(int,integer))
    print(hash(t))