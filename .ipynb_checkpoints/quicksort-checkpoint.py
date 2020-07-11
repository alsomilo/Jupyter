import numpy as np
def quicksort_np(a):
    if len(a) < 2:
        return a

    mid = a[0]
    a = a[1:]
    return np.concatenate((quicksort_np(a[a[:] <= mid]), [mid] , quicksort_np(a[a[:] > mid])))

def quicksort(a):
    if len(a) < 2:
        return a

    return quicksort([x for x in a[1:] if x <= a[0]]) + [a[0]] + quicksort([x for x in a[1:] if x > a[0]])

b = [10,5,2,3, -1, 0, 9, 2, 1]
a = np.array([10,5,2,3, -1, 0, 9, 2, 1])
sort_np = quicksort_np(a)
sort_legacy = quicksort(b)
print(f'NP    : {sort_np}, type: {type(sort_np)}')
print(f'Legacy: {sort_legacy}, type: {type(sort_legacy)}')