print("Введите массив чисел")
lst = input()

def sorting_squared(lst):
    lst_n = list(map(int, lst.split(' ')))
    l = 0
    r = len(lst_n) - 1  
    res = []
    while l <= r:
        if lst_n[l]**2 > lst_n[r]**2:
            res.append(lst_n[l]**2)
            l += 1
        else:
            res.append(lst_n[r]**2)
            r -= 1
    res.reverse()
    return res

sorting_squared(lst)
print(sorting_squared(lst))