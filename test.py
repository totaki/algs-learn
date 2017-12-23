TO_SORT = [10, 28, 34, 34, 1, 456, 2, 4, 5, 3, 75, 2, 85, 63, 5, 73, 21]

EXPECTED = [1, 2, 2, 3, 4, 5, 5, 10, 21, 28, 34, 34, 63, 73, 75, 85, 456]


def test(func):
    print('\nTo sorting %s length' % len(TO_SORT))
    print(' ', TO_SORT)
    print('Expected:')
    print(' ', EXPECTED)
    result, iterations = func(TO_SORT) 
    print('Result:')
    print(' ', result)
    print('Iterations:')
    print(' ', iterations)
    print('Success:')
    print(' ', result == EXPECTED, '\n')