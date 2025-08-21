def trap(height):
    n = len(height)
    if n < 3:  # less than 3 bars, no water can be trapped
        return 0
    
    left, right = 0, n - 1
    leftMax, rightMax = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1
    
    return water


# ✅ Test Cases
tests = [
    [0,1,0,2,1,0,1,3,2,1,2,1],  # Expected 6
    [4,2,0,3,2,5],              # Expected 9
    [1,1,1],                    # Expected 0
    [5],                        # Expected 0
    [2,0,2],                    # Expected 2
    [0,0,0],                    # Expected 0
    [1,2,3,4,5],                # Expected 0
    [5,4,3,2,1]                 # Expected 0
]

for arr in tests:
    print(f"Input: {arr} -> Trapped Water = {trap(arr)}")
