print("Введите версию 1")
ver1 = input()
print("Введите версию 2")
ver2 = input()

def version_cmpr(ver1,ver2):
    ver1_new = list(map(int, ver1.split('.')))
    ver2_new = list(map(int, ver2.split('.')))

    for i, j in zip(ver1_new, ver2_new):
        if i > j:
            return 1
        elif i < j:
            return -1
    return 0

print(version_cmpr(ver1, ver2))