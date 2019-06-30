"""Longest Common Substring with variable codon length."""


def lcs_string(input_a, input_b, codon_length=1, verbose=False):
    r"""Longest Commong Substring with variable length codon that
    assumes that input_a and input_b are strings. The returned values
    are strings with spaces (' ') where there is no match. If the
    input strings have spaces the algorithm will still run fine but
    the output will be ambiguous.

    >>> print('%r\n%r\n%r' % lcs_string('aaa' * 10, 'aaa' * 10))
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    30
    >>> print('%r\n%r\n%r' % lcs_string('abc' * 10, 'abc' * 10))
    'abcabcabcabcabcabcabcabcabcabc'
    'abcabcabcabcabcabcabcabcabcabc'
    30
    >>> print('%r\n%r\n%r' % lcs_string('abc' * 10, 'cba' * 10))
    '  a b c a b c a b c abcabcabcabcabcabcabc'
    'cbacbacbacbacbacbacba c b a c b a c b a  '
    19
    >>> print('%r\n%r\n%r' % lcs_string('abc' * 10, 'cab' * 10))
    ' abcabcabcabcabcabcabcabcabcabc'
    'cabcabcabcabcabcabcabcabcabcab '
    29
    >>> print('%r\n%r\n%r' % lcs_string('aaa' * 10, 'aaa' * 10, 3))
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    10
    >>> print('%r\n%r\n%r' % lcs_string('abc' * 10, 'abc' * 10, 3))
    'abcabcabcabcabcabcabcabcabcabc'
    'abcabcabcabcabcabcabcabcabcabc'
    10
    >>> print('%r\n%r\n%r' % lcs_string('abc' * 10, 'cba' * 10, 3))
    '                              abcabcabcabcabcabcabcabcabcabc'
    'cbacbacbacbacbacbacbacbacbacba                              '
    0
    >>> print('%r\n%r\n%r' % lcs_string('abc' * 10, 'cab' * 10, 3))
    ' abcabcabcabcabcabcabcabcabc  abc'
    'cabcabcabcabcabcabcabcabcabcab   '
    9
    >>> print('%r\n%r\n%r' % lcs_string('d' + ('abc' * 10), 'e' + ('abc' * 10), 3))
    ' dabcabcabcabcabcabcabcabcabcabc'
    'e abcabcabcabcabcabcabcabcabcabc'
    10
    >>> print('%r\n%r\n%r' % lcs_string(('abc' * 10) + 'd', ('abc' * 10) + 'e', 3))
    'abcabcabcabcabcabcabcabcabcabc d'
    'abcabcabcabcabcabcabcabcabcabce '
    10
    >>> print('%r\n%r\n%r' % lcs_string(('abc' * 10) + 'de', ('abc' * 10) + 'ed', 3))
    'abcabcabcabcabcabcabcabcabcabc  de'
    'abcabcabcabcabcabcabcabcabcabced  '
    10
    >>> print('%r\n%r\n%r' % lcs_string('e' + ('abc' * 10) + 'd', 'd' + ('abc' * 10) + 'e', 3))
    ' eabcabcabcabcabcabcabcabcabcabc d'
    'd abcabcabcabcabcabcabcabcabcabce '
    10
    >>> print('%r\n%r\n%r' % lcs_string('eee' + ('abc' * 10) + 'ddd', 'ddd' + ('abc' * 10) + 'eee', 3))
    '   eeeabcabcabcabcabcabcabcabcabcabc   ddd'
    'ddd   abcabcabcabcabcabcabcabcabcabceee   '
    10
    >>> print('%r\n%r\n%r' % lcs_string('eee' + ('abc' * 10) + 'ddd', 'ddd' + ('abc' * 5) + 'eee', 3))
    '   eeeabcabcabcabcabc   abcabcabcabcabcddd'
    'ddd   abcabcabcabcabceee                  '
    5
    >>> print('%r\n%r\n%r' % lcs_string('eee' + ('abc' * 5) + 'ddd', 'ddd' + ('abc' * 10) + 'eee', 3))
    '   eeeabcabcabcabcabc                  ddd'
    'ddd   abcabcabcabcabcabcabcabcabcabceee   '
    5
    """
    result = lcs(input_a, input_b, codon_length, verbose)
    return (''.join(' ' if c is None else c for c in result[0]),
            ''.join(' ' if c is None else c for c in result[1]),
            result[2])


def lcs(input_a, input_b, codon_length=1, verbose=False):
    r"""Longest Common Substring with variable codon length.

    >>> print('%r\n%r\n%r' % lcs((0, 1, 2) * 3, (2, 0, 1) * 3))
    [None, 0, 1, 2, 0, 1, 2, 0, 1, 2]
    [2, 0, 1, 2, 0, 1, 2, 0, 1, None]
    8
    >>> print('%r\n%r\n%r' % lcs((0, 1, 2) * 3, (2, 0, 1) * 3, 3))
    [None, 0, 1, 2, 0, 1, 2, None, None, 0, 1, 2]
    [2, 0, 1, 2, 0, 1, 2, 0, 1, None, None, None]
    2
    >>> print('%r\n%r\n%r' % lcs((0, 1, 2) * 3, (0, 1, 2) * 3, 3))
    [0, 1, 2, 0, 1, 2, 0, 1, 2]
    [0, 1, 2, 0, 1, 2, 0, 1, 2]
    3
    >>> print('%r\n%r\n%r' % lcs((0, 1, 2) * 3, (0, 1, 2) * 3))
    [0, 1, 2, 0, 1, 2, 0, 1, 2]
    [0, 1, 2, 0, 1, 2, 0, 1, 2]
    9
    >>> print('%r\n%r\n%r' % lcs((0, 1, 2) * 3, (2, 1, 0) * 3))
    [None, None, 0, None, 1, None, 2, 0, 1, 2, 0, 1, 2]
    [2, 1, 0, 2, 1, 0, 2, None, 1, None, 0, None, None]
    5
    """

    if verbose:
        from util import print_table
        print(input_a)
        print(input_b)
    match_matrix = [[0] * (len(input_b) + 1) for i in range(len(input_a) + 1)]
    if verbose:
        matching_points = [[''] * (len(input_b) + 1) for i in range(len(input_a) + 1)]
    codon_length_less_1 = codon_length - 1
    for x in range(codon_length - 1, len(input_a)):
        for y in range(codon_length - 1, len(input_b)):
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
        for i in range(len(display_matrix)):
            display_matrix[i] = display_matrix[i][:]
        display_matrix[0] = [''] + list(input_b)
        matching_points[0] = [''] + list(input_b)
        for x in range(len(input_a)):
            display_matrix[x + 1][0] = input_a[x]
            matching_points[x + 1][0] = input_a[x]
        print_table(display_matrix)
        print_table(matching_points)

    x = len(input_a)
    y = len(input_b)
    result_a = []
    result_b = []

    while x > codon_length_less_1 and y > codon_length_less_1:
        if match_matrix[x][y] == match_matrix[x - 1][y]:
            x -= 1
            result_a.append(input_a[x])
            result_b.append(None)
        elif match_matrix[x][y] == match_matrix[x][y - 1]:
            y -= 1
            result_a.append(None)
            result_b.append(input_b[y])
        else:
            x -= codon_length
            y -= codon_length
            result_a.extend(reversed(input_a[x:x + codon_length]))
            result_b.extend(reversed(input_b[y:y + codon_length]))
    while x > 0:
        x -= 1
        result_a.append(input_a[x])
        result_b.append(None)
    while y > 0:
        y -= 1
        result_a.append(None)
        result_b.append(input_b[y])
    result_a.reverse()
    result_b.reverse()
    if verbose:
        if isinstance(input_a, str):
            print(''.join(' ' if c is None else c for c in result_a))
        else:
            print(result_a)
        if isinstance(input_b, str):
            print(''.join(' ' if c is None else c for c in result_b))
        else:
            print(result_b)
    return (result_a, result_b, match_matrix[len(input_a)][len(input_b)])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
