def solution(triangle):
    sum_triangle = [triangle[0]]
    for i in range(1,len(triangle)):
        leaf_level = []
        for j in range(i+1):
            if (j == 0):
                leaf_level.append(triangle[i][j] + sum_triangle[i-1][0])
            elif (j == i):
                leaf_level.append(triangle[i][j] + sum_triangle[i-1][j-1])
            elif (sum_triangle[i-1][j-1] > sum_triangle[i-1][j]):
                leaf_level.append(triangle[i][j] + sum_triangle[i-1][j-1])
            else:
                leaf_level.append(triangle[i][j] + sum_triangle[i-1][j])
        sum_triangle.append(leaf_level)            

    return max(sum_triangle[-1])