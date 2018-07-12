# def quick_sort(lst):
#     if len(lst) < 2:
#         return lst
#     key = lst.pop(0)
#     less = [i for i in lst if i < key]
#     greater = [i for i in lst if i >= key]
#     return quick_sort(less) + [key] + quick_sort(greater)
#
#
# if __name__ == "__main__":
#     print(quick_sort([21, 1, 323, 323, 3, 323, 32]))


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    print(quick_sort([10, 5, 2, 3]))
