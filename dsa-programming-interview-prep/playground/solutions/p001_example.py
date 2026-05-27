def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], index]
        seen[num] = index
    return []

