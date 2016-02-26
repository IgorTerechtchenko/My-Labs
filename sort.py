import radix_sort
import quick_sort
import merge_sort

import random

quick_sort = quick_sort.quicksort
radix_sort = radix_sort.radixsort
merge_sort = merge_sort.merge_sort
def demo(alist, sort):
    """demonstrate work of sort algorythm on alist"""
    random.shuffle(alist)
    print alist
    print sort(alist)
