def findMedianSortedArrays(nums1, nums2):
    arr1=nums1
    arr2=nums2
    arr1.extend(arr2)
    arr1.sort()
    half=(len(arr1)//2)
    if len(arr1)%2==0:
        frst=arr1[half-1]
        scnd=arr1[half]
        median = (frst + scnd) / 2
        return median/1.0
    else:
        median = arr1[half]
        return median
print(findMedianSortedArrays([1,2],[3,4]))