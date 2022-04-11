def twosum(nums: list[int] = [1, 2, 3, 4, 5], target: int = 10) -> list[int]:
    res = list[int]
    tmp = 0
    i = 0
    while i != len(nums):
        tmp = nums[i]
        try:
            nums.index(target - tmp)
        except ValueError:
            i += 1
            continue

    return res


print(twosum())
