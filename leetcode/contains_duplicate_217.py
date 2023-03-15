def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    dct = set()
    for i in nums:
        if i in dct:
            return True
        dct.add(i)
    return False

if __name__ == "__main__":
    from doctest import testmod
    testmod()