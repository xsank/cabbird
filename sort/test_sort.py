#these are stable sorting
from bubble_sort import bubble_sort
from insert_sort import insert_sort
from merge_sort import merge_sort

#these are non comparative sorting
from bucket_sort import bucket_sort
from count_sort import count_sort
from radix_sort import radix_sort

#these are unstable sorting
from select_sort import select_sort
from quick_sort import quick_sort
from heap_sort import heap_sort

cases=[
    [],
    [1],
    [1,3,1,4,21],
    [3,1,2,4]
]

answers=[
    [],
    [1],
    [1,1,3,4,21],
    [1,2,3,4]
]

def test_sort(func):
    '''
    the test cases only contain natural numbers.
    just because the bucket sort,count sort,radix sort.

    '''
    tmp_cases=[i[:] for i in cases]
    for index,case in enumerate(tmp_cases):
        try:
            assert func(case)==answers[index]
        except Exception:
            print '%d test case,%s get wrong anwser' % (index+1,func.__name__)


if __name__=="__main__":
    test_sort(bubble_sort)
    test_sort(insert_sort)
    test_sort(bucket_sort)
    test_sort(count_sort)
    test_sort(merge_sort)
    test_sort(radix_sort)
    test_sort(select_sort)
    test_sort(quick_sort)
    test_sort(heap_sort)
