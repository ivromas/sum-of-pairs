
def sum_pairs(num, s):
    mem = set()
    for i in lst:
        if s - i in mem:
            return [s - i, i]
        mem.add(i)
