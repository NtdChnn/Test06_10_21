Ip = int(input("Input : "))
if Ip <= 0:
    print("!!!Please enter number greater than zero!!!")
else:
    for i in range(0,Ip+1):
        for j in range(0,i):
            print('*',end='')
        for j in range(i,Ip):
            print('  ',end='')
        for j in range(0, i):
            print('*', end='')
        print()
    for i in range(0,Ip):
        for j in range(i,Ip-1):
            print('*',end='')
        for j in range(0,i+1):
            print('  ',end='')
        for j in range(i, Ip - 1):
            print('*', end='')
        print()