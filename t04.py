Ip = int(input('Enter a positive number : '))
if Ip <= 0 :
    print(f'{Ip} is too low.')
elif Ip >= 16:
    print(f'{Ip} is too high.')
else:
    for i in range(1,Ip+1):
        print("%X " %(i),end='')
    print()
    for i in range(2,Ip+1):
        print("%X" %(i),end='')
        if i != Ip :
            for j in range(3,Ip*2):
                print(' ',end='')
            print("%X" %(i-1), end='')
        else:
            for i in range(1, Ip):
                print(" %X" %(i), end='')
        print()