def radixsort(array):
    maxLength = False
    tmp = -1 
    placement = 1
 
    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(10)]
 
    # split array between lists
        for i in array:
            tmp = i / placement
            buckets[tmp % 10].append(i)
            if maxLength and tmp > 0:
                maxLength = False
 
    # empty lists into array array
        a = 0
        for b in range( 10 ):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1
 
    # move to next digit
        placement *= 10
    return array
