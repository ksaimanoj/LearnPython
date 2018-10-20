def seq(start, end):
    l = []
    for i in range(start, end):
        if i % 7 == 0 and i %35 != 0:
            l.append(str(i));
    return ",".join(l)