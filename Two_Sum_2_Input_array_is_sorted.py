
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, r = 0, len(numbers)-1
    while l<r:
      total = numbers[l]+numbers[r]
      if total > target: r-=1
      elif total < target: l+=1
      else: return [l+1,r+1]


print(twoSum([2,7,11,15],9))
