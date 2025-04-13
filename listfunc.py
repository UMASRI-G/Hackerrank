if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        pos=input().split()
        cmd=pos[0]
        if cmd=="insert":
            list.insert(int(pos[1]),int(pos[2]))
        elif cmd=="print":
            print(list)
        elif cmd=="remove":
            list.remove(int(pos[1]))
        elif cmd=="append":
            list.append(int(pos[1]))
        elif cmd=="sort":
            list.sort()
        elif cmd=="pop":
            list.pop()
        elif cmd=="reverse":
            list.reverse()
    
