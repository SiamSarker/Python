for i in range(0, int(input())):
    list = []
    for j in range(0, 3):
        list.append(int(input()))
    for l in range(0, 3):
        flag = 0
        for k in range(1, list[l]-1):
            m = k
            n = (list[l] - 1) - k
            if m == list[l + 1 % 3] and n == list[l + 2 % 3] or n == list[l + 1 % 3] and m == list[l + 2 % 3]:
                flag = 1
            else:
                flag = 0
        if flag == 1:
            print("Yes")
            break
print("No")
