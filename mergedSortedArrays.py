def merge_two_sorted_lists(nums1,m,nums2,n):

    if n < 1:
        pass

    elif m < 1:
        nums1[0] = nums2

    else:
        for x in range(0, m):
            nums1[m+x] = nums2[x]
        nums1.sort()
    print(nums1)

(merge_two_sorted_lists([1,2,3,0,0,0],3, [2,5,6],3))
(merge_two_sorted_lists([1],1, [],0))
(merge_two_sorted_lists([0],0, [1],1))

