import test


def run(arr):
    length = len(arr)
    iterations = 0
    for i in range(0, length):
        curr = arr[i]
        j = i
        while (j > 0 and arr[j - 1] > curr):
            arr[j] = arr[j - 1]
            j = j - 1
            iterations += 1
        arr[j] = curr

    return arr, iterations


if __name__ == '__main__':
    test.test(run)