def most_common(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_num = max(count, key=count.get)
    return max_num

print(most_common([1,1,1,3,1,0,5,2,1]))
