def next_bigger(n):
    if n < 12: return -1
    s = ''.join([d for d in str(n)])
    print(s)
    swap = s[:-2] + s[-1] + s[-2]
    print(swap)
    m = int(swap)
    print(n, m)
    return m if m > n else -1




next_bigger(12)   # returns 21
next_bigger(513)  # returns 531
next_bigger(2017) # returns 2071
# If the digits can't be rearranged to form a bigger number, return -1 
next_bigger(9)   # returns nil
next_bigger(111) # returns nil
next_bigger(531) # returns nil
next_bigger(414) # 441
next_bigger(144) # 414