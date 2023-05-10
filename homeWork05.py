# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

'''
a = int(input('A = '))
b = int(input('B = '))
def cub_a(a, b):
    if b == 1:
        return a
    return a ** b
print(cub_a(a, b))
'''
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию
# RLE,
# которая на выходе даст:
# A4B3C2XYZD4E3F3A6B28

a = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'

def rle(a):
    count = 0
    b = ()
    final = ()
    for i in range(0, len(a)):
        if a[i] == a[i - 1]:
            count += 1
        else:
            final = (a[i], count)
            b += final
            
    print(*b)
rle(a) 

    