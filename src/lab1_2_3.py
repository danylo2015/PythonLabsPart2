def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    else:
        pivot = arr[length // 2]
        arr.remove(pivot)

    larger = []
    lower = []

    for el in arr:
        if el > pivot:
            larger.append(el)
        else:
            lower.append(el)

    return quick_sort(larger) + [pivot] + quick_sort(lower)


def find_kth_largest_el(arr, k):
    if k > len(arr):
        raise ValueError("Array size must be at least k")
    sorted_arr = quick_sort(arr.copy())
    return (f"The {k} largest element in list is: {sorted_arr[k-1]}, "
            f"the index of the element in the original list is:{arr.index(sorted_arr[k-1])}")


rofl = [15, 7, 22, 9, 36, 2, 42, 18]
print(quick_sort(rofl.copy()))
print(find_kth_largest_el(rofl, 7))
