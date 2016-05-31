wow = 0


def merge_sort(arr):
    def merge(arr1, arr2):
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
                if i < len(arr1):
                    result += arr1[i:]
                elif j < len(arr2):
                    result += arr2[j:]

        return result

    if len(arr) > 1:
        arr1 = merge_sort(arr[:len(arr) // 2])
        arr2 = merge_sort(arr[len(arr) // 2:])
        return merge(arr1, arr2)
    return arr


def main():
    a = int(raw_input())
    combination = map(int, raw_input().strip().split(" "))
    combination = merge_sort(combination)
    print wow


if __name__ == "__main__":
    main()
