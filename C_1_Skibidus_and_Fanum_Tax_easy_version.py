dev bs( l, t):
    l,r = 0, len(l)
    while l < r:
        m = (l+r)//2
        if l[m] == t:
            return m
        if l[m] < t:
            l = m+1
        else:
            r = m