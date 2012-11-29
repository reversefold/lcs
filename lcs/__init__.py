from util import print_table


def lcs(a, b, cl, verbose=False):
    if verbose:
        print a
        print b
    arr = [[0] * (len(b) + 1) for i in xrange(len(a) + 1)]
    arr2 = [[''] * (len(b) + 1) for i in xrange(len(a) + 1)]
#    maxcoord = (0, (0, 0))
    for x in xrange(cl - 1, len(a)):
        for y in xrange(cl - 1, len(b)):
            arr[x + 1][y + 1] = max(
                (1 if a[x - (cl - 1):x + 1] == b[y - (cl - 1):y + 1] else 0) + arr[x - (cl - 1)][y - (cl - 1)],
                arr[x][y + 1], #arr[x - (cl - 1)][y + 1],
                arr[x + 1][y]) #arr[x + 1][y - (cl - 1)])
#            if arr[x + 1][y + 1] > maxcoord[0]:
#                maxcoord = (arr[x + 1][y + 1], (x + 1, y + 1))
#            if arr[x + 1][y + 1] != arr[x - (cl - 1)][y + 1] and arr[x + 1][y + 1] != arr[x + 1][y - (cl - 1)]:
            if arr[x + 1][y + 1] != arr[x][y + 1] and arr[x + 1][y + 1] != arr[x + 1][y]:
                arr2[x + 1][y + 1] = 'x'
#            print x, y, a[x], b[y], arr[x][y], arr[x + 1][y + 1]
    parr = arr[:]
    parr[0] = [''] + list(b)
    arr2[0] = [''] + list(b)
    for x in xrange(len(a)):
        arr[x + 1][0] = a[x]
        arr2[x + 1][0] = a[x]
    if verbose:
        print_table(parr)
        print_table(arr2)

    x = len(a)
    y = len(b)
    ra = []
    rb = []
#    while x > maxcoord[1][0]:
#        x -= 1
#        ra.append(a[x])
#        rb.append(' ')
#    while y > maxcoord[1][1]:
#        y -= 1
#        ra.append(' ')
#        rb.append(b[y])

    while x > (cl - 1) and y > (cl - 1):
        if arr[x][y] == arr[x - 1][y]:
            x -= 1
            ra.append(a[x])
            rb.append(' ')
        elif arr[x][y] == arr[x][y - 1]:
            y -= 1
            ra.append(' ')
            rb.append(b[y])
        else:
            x -= cl
            y -= cl
            ra.extend(reversed(a[x:x + cl]))
            rb.extend(reversed(b[y:y + cl]))
    while x > 0:
        x -= 1
        ra.append(a[x])
        rb.append(' ')
    while y > 0:
        y -= 1
        ra.append(' ')
        rb.append(b[y])
    ra.reverse()
    rb.reverse()
    ra = ''.join(ra)
    rb = ''.join(rb)
    if verbose:
        print ra
        print rb
    return (ra, rb, arr[len(a)][len(b)])
