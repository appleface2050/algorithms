"""
    Binary Search
    -------------
    Recursively partitions the list until the `key` is found.

    Time Complexity:  O(lg n)

    Psuedo Code: http://en.wikipedia.org/wiki/Binary_search

"""
def search(seq, key):
    """
    Takes a list of integers and searches if the `key` is contained within
    the list.

    :param seq: A list of integers
    :param key: The integer to be searched for
    :rtype: The index of where the `key` is located in the list. If `key` is
            not found then False is returned.
    """

    lo = 0
    hi = len(seq) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False

def bin_search_recursively(l, first, last, n):
  '''Binary search n in list l which has been sorted already, returns
  the index if found, else returns None.'''
  if first > last:
    return None

  mid = (first + last) // 2 # Use / 2 if you're using Python 2
  if l[mid] > n:
    return bin_search_recursively(l, first, mid - 1, n)
  elif l[mid] < n:
    return bin_search_recursively(l, mid + 1, last, n)
  else:
    return mid
