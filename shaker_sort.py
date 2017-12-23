import test


def run(arr):
    left = 0
    right = len(arr) - 1
    iterations = 0
    while True:
        if left == right:
            break

        curr = left
        while curr < right:
            if arr[curr] > arr[curr + 1]:
                arr[curr], arr[curr + 1] = arr[curr + 1], arr[curr]
            iterations += 1
            curr += 1
        right -= 1

        curr = right
        while curr > left:
            if arr[curr] < arr[curr - 1]:
                arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
            iterations += 1
            curr -= 1
        left += 1

    return arr, iterations


if __name__ == '__main__':
    test.test(run)
