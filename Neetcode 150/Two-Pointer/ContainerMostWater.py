def maxArea(height):
    #int array height n, n vertical
    j = 0
    k = len(height) - 1
    left = 0
    right = 0
    area=0
    # for i in height:
    while k!=0 or j>=len(height):
        if height[j] >= height[k]:
            lowest_side = height[k]
        else:
            lowest_side = height[j]
        if area < lowest_side * (k-j):
            area = lowest_side * (k-j)
        if j > k:
            k+=1
        else:
            j+=1
    return area

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)