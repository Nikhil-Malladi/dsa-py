

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dct = {}
    for n,i in enumerate(nums):
        if target - i in dct:
            return [n,dct[target-i]]
        dct[i]=n
    return []


if __name__ == "__main__":
    from doctest import testmod
    testmod()