def sum_pairs(ints, s):
    mem = set()
    for i in ints:
        if s - i in mem:
            return [s - i, i]
        mem.add(i)
