"""Longest Common Substring with variable codon length."""

def lcs(input_a, input_b, codon_length=1, verbose=False):
    r"""Longest Common Substring with variable codon length.

    >>> print '%r\n%r\n%r' % lcs('aaa' * 10, 'aaa' * 10)
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    30
    >>> print '%r\n%r\n%r' % lcs('abc' * 10, 'abc' * 10)
    'abcabcabcabcabcabcabcabcabcabc'
    'abcabcabcabcabcabcabcabcabcabc'
    30
    >>> print '%r\n%r\n%r' % lcs('abc' * 10, 'cba' * 10)
    '  a b c a b c a b c abcabcabcabcabcabcabc'
    'cbacbacbacbacbacbacba c b a c b a c b a  '
    19
    >>> print '%r\n%r\n%r' % lcs('abc' * 10, 'cab' * 10)
    ' abcabcabcabcabcabcabcabcabcabc'
    'cabcabcabcabcabcabcabcabcabcab '
    29
    >>> print '%r\n%r\n%r' % lcs('aaa' * 10, 'aaa' * 10, 3)
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    10
    >>> print '%r\n%r\n%r' % lcs('abc' * 10, 'abc' * 10, 3)
    'abcabcabcabcabcabcabcabcabcabc'
    'abcabcabcabcabcabcabcabcabcabc'
    10
    >>> print '%r\n%r\n%r' % lcs('abc' * 10, 'cba' * 10, 3)
    '                              abcabcabcabcabcabcabcabcabcabc'
    'cbacbacbacbacbacbacbacbacbacba                              '
    0
    >>> print '%r\n%r\n%r' % lcs('abc' * 10, 'cab' * 10, 3)
    ' abcabcabcabcabcabcabcabcabc  abc'
    'cabcabcabcabcabcabcabcabcabcab   '
    9
    >>> print '%r\n%r\n%r' % lcs('d' + ('abc' * 10), 'e' + ('abc' * 10), 3)
    ' dabcabcabcabcabcabcabcabcabcabc'
    'e abcabcabcabcabcabcabcabcabcabc'
    10
    >>> print '%r\n%r\n%r' % lcs(('abc' * 10) + 'd', ('abc' * 10) + 'e', 3)
    'abcabcabcabcabcabcabcabcabcabc d'
    'abcabcabcabcabcabcabcabcabcabce '
    10
    >>> print '%r\n%r\n%r' % lcs(('abc' * 10) + 'de', ('abc' * 10) + 'ed', 3)
    'abcabcabcabcabcabcabcabcabcabc  de'
    'abcabcabcabcabcabcabcabcabcabced  '
    10
    >>> print '%r\n%r\n%r' % lcs('e' + ('abc' * 10) + 'd', 'd' + ('abc' * 10) + 'e', 3)
    ' eabcabcabcabcabcabcabcabcabcabc d'
    'd abcabcabcabcabcabcabcabcabcabce '
    10
    >>> print '%r\n%r\n%r' % lcs('eee' + ('abc' * 10) + 'ddd', 'ddd' + ('abc' * 10) + 'eee', 3)
    '   eeeabcabcabcabcabcabcabcabcabcabc   ddd'
    'ddd   abcabcabcabcabcabcabcabcabcabceee   '
    10
    >>> print '%r\n%r\n%r' % lcs('eee' + ('abc' * 10) + 'ddd', 'ddd' + ('abc' * 5) + 'eee', 3)
    '   eeeabcabcabcabcabc   abcabcabcabcabcddd'
    'ddd   abcabcabcabcabceee                  '
    5
    >>> print '%r\n%r\n%r' % lcs('eee' + ('abc' * 5) + 'ddd', 'ddd' + ('abc' * 10) + 'eee', 3)
    '   eeeabcabcabcabcabc                  ddd'
    'ddd   abcabcabcabcabcabcabcabcabcabceee   '
    5
    """

    if verbose:
        from util import print_table
        print input_a
        print input_b
    match_matrix = [[0] * (len(input_b) + 1) for i in xrange(len(input_a) + 1)]
    if verbose:
        matching_points = [[''] * (len(input_b) + 1) for i in xrange(len(input_a) + 1)]
    codon_length_less_1 = codon_length - 1
    for x in xrange(codon_length - 1, len(input_a)):
        for y in xrange(codon_length - 1, len(input_b)):
            match_matrix[x + 1][y + 1] = max(
                ((1 if input_a[x - codon_length_less_1:x + 1] == input_b[y - codon_length_less_1:y + 1]
                  else 0)
                 + match_matrix[x - codon_length_less_1][y - codon_length_less_1]),
                match_matrix[x][y + 1],
                match_matrix[x + 1][y])
            if verbose:
                if match_matrix[x + 1][y + 1] != match_matrix[x][y + 1] and match_matrix[x + 1][y + 1] != match_matrix[x + 1][y]:
                    matching_points[x + 1][y + 1] = 'x'


    if verbose:
        display_matrix = match_matrix[:]
        for i in xrange(len(display_matrix)):
            display_matrix[i] = display_matrix[i][:]
        display_matrix[0] = [''] + list(input_b)
        matching_points[0] = [''] + list(input_b)
        for x in xrange(len(input_a)):
            display_matrix[x + 1][0] = input_a[x]
            matching_points[x + 1][0] = input_a[x]
        print_table(display_matrix)
        print_table(matching_points)

    x = len(input_a)
    y = len(input_b)
    ra = []
    rb = []

    while x > codon_length_less_1 and y > codon_length_less_1:
        if match_matrix[x][y] == match_matrix[x - 1][y]:
            x -= 1
            ra.append(input_a[x])
            rb.append(' ')
        elif match_matrix[x][y] == match_matrix[x][y - 1]:
            y -= 1
            ra.append(' ')
            rb.append(input_b[y])
        else:
            x -= codon_length
            y -= codon_length
            ra.extend(reversed(input_a[x:x + codon_length]))
            rb.extend(reversed(input_b[y:y + codon_length]))
    while x > 0:
        x -= 1
        ra.append(input_a[x])
        rb.append(' ')
    while y > 0:
        y -= 1
        ra.append(' ')
        rb.append(input_b[y])
    ra.reverse()
    rb.reverse()
    ra = ''.join(ra)
    rb = ''.join(rb)
    if verbose:
        print ra
        print rb
    return (ra, rb, match_matrix[len(input_a)][len(input_b)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
