import test


def run(arr):
    stop= False
    indexes = list(range(len(arr) - 1))
    iterations = 0
    while not stop:
        for i in indexes:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            iterations += 1
        indexes = indexes[:-1]
        if len(indexes) == 1:
            stop = True
    return arr, iterations


if __name__ == '__main__':
    test.test(run)
