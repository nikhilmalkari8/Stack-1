def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n  # Initialize the result array with -1
    stack = []  # Stack to store indices

    # Iterate through the array twice for circular behavior
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            index = stack.pop()
            result[index] = nums[i % n]
        if i < n:  # Only push indices during the first pass
            stack.append(i % n)
    
    return result
