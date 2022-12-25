def swap_min_max(a):
    max_index =a.index(max(a))
    min_index =a.index(min(a))
    ma=max(a)
    mi=min(a)
    a[max_index]=mi
    a[min_index]=ma
    a=[ ]
    print(a)
    return swap_min_max(a)