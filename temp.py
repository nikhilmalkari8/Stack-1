def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n  # Initialize the result list with zeros
    stack = []  # Stack to store indices
    
    for i, temp in enumerate(temperatures):
        # Process elements in the stack
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)  # Push the current index onto the stack
    
    return result
