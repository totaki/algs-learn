import test


def run(arr):
    sorted_arr = [[i] for i in arr]
    length = len(arr)
    iterations = 0
    while len(sorted_arr[0]) != length:
        f = sorted_arr.pop(0)
        s = sorted_arr.pop(0)
        result = []
        while s or f:
            if f and s:
                if f[0] < s[0]:
                    result.append(f.pop(0))
                else:
                    result.append(s.pop(0))
            elif s:
                result.extend(s)
                s = None
            elif f:
                result.extend(f)
                f = None
            iterations += 1
        sorted_arr.append(result)

    return sorted_arr[0], iterations


if __name__ == '__main__':
    test.test(run)