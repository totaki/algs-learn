import test_data


def run(arr):
    stop= False
    indexes = list(range(len(arr) - 1))
    while not stop:
        for i in indexes:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        indexes = indexes[:-1]
        if len(indexes) == 1:
            stop = True
    return arr


if __name__ == '__main__':
    print('To sorting:')
    print(' ', test_data.TO_SORT)
    print('Expected:')
    print(' ', test_data.EXPECTED)
    print('Result:')
    result = run(test_data.TO_SORT) 
    print(' ', result)
    print('Success:')
    print(' ', result == test_data.EXPECTED)
