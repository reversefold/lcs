def print_table(arr):
    max_len = max(max(len(str(c)) for c in r) for r in arr)
    row_format = ('{:>' + str(max_len + 1) + '}') * len(arr[0])
    for y in xrange(len(arr)):
        print row_format.format(*arr[y])
