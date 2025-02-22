n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif 2<=n<= 5:
    print("Not Weird")
elif 6<=n<=20: # If n is even and in the range 6 to 20
    print("Weird") 
elif n>20: # If n is even and greater than 20 
    print("Not Weird")
