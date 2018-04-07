def swap(items, a, b):
    t = items[a]
    items[a] = items[b]
    items[b] = t


def partition(items, p, r):

    x = items[r]
    i = p - 1
    for j in range(p, r):
        if items[j] <= x:
            i = i+1
            swap(items, i, j)
    swap(items, i+1, r)
    return i+1


def quick_sort(items, p, r):
    if p < r:
        q = partition(items, p, r)
        quick_sort(items, p, q-1)
        quick_sort(items, q+1, r)


def sort_it():
    items = [56, 23, 34, 12, 2, 65, 45, 76, 13]
    print('Actual Items: {}'.format(items))
    quick_sort(items, 0, len(items)-1)
    print('Sorted Items: {}'.format(items))


if __name__ == '__main__':
    sort_it()