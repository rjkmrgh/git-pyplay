def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    for i in range(1, n1+1):
        L.append(A[p + i - 1])
    for j in range(1, n2+1):
        R.append(A[q + j])
    L.append(float('inf'))
    R.append(float('inf'))

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:

        q = int((p + r)/2)

        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
    return arr


def sort_it():
    unsorted = [5, 3, 7, 2, 8, 1, 0, 4]
    ln = len(unsorted)
    print(unsorted)
    sorted = merge_sort(A, 0, ln-1)
    print(sorted)


if __name__ == '__main__':
    sort_it()