Ip = [int(e) for e in input("Enter number end with (-1) : ").split(' ')]
Ans = []
count = 1
found = False
if -1 not in Ip:
    print("Invalid INPUT !!!")
else:
    for e in Ip:
        if e != -1:
            Ans.append(e)
        else:
            break
    Ans.sort()

    for e in range(0,len(Ans)):
        if e != 0 and Ans[e] == Ans[e-1]:
            count += 1
        else:
            if count > (len(Ans)/2):
                print(Ans[e-1])
                found = True
                break
            else:
                count = 1
    if count > (len(Ans) / 2) and found == False and len(Ans) != 0:
        print(Ans[len(Ans)-1])
        found = True
    if not found:
        print('Not found')
