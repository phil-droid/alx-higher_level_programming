def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    start, end = 0, len(list_of_integers) - 1

    while start <= end:
        mid = (start + end) // 2

        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid - 1
        else:
            start = mid + 1
