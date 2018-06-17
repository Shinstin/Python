def expl(idx, compsize, b, st) :
    tmpidx = idx - compsize
    if tmpidx < 0 :
        return idx
    for c in b:
        if c != st[tmpidx] :
            return idx
        else :
            tmpidx = tmpidx + 1
    idx = idx - compsize
    idx = expl(idx, compsize, b, st)
    return idx

if __name__ == "__main__":
    a = str(input())
    b = str(input())
    compsize = len(b)
    st = []
    idx = 0

    for c in a:
        if len(st) > idx :
            st[idx] = c
        else : 
            st.append(c)
        idx = idx + 1
        idx = expl(idx, compsize, b, st)
    
    str = ""
    if idx == 0 :
        str = "FRULA"
    else :
        for c in st :
            str = str + c
            idx = idx - 1
            if (idx <= 0) :
                break
    print(str)