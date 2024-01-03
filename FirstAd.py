with open("test.txt", 'r') as rf:
    read = rf.readlines()   
    num = []
    for rad in range(0,len(read)):
        rad_num = []
        for  x in read[rad]:          
            if str(x).isdigit():
                rad_num.append(x)
        num.append(rad_num)
    num_sorted = []
    for rad in num:
        if len(rad) == 1:
            new_num = rad[0]+rad[0]
            num_sorted.append(int(new_num))
        else:
            new_num = rad[0]+rad[-1]
            num_sorted.append(int(new_num))


print(sum(num_sorted))


Text_num = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

