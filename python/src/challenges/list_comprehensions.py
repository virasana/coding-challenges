def get_cuboid_permuations(x, y, z, n):
    # result = []
    # for i in range(x + 1):
    #     for j in range(y +1):
    #         for k in range(z + 1):
    #             if i + j + k != n:
    #                 result.append([i, j, k])
    
    result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]    
    print(result)
    return result

if __name__ == '__main__':
    x, y, z, n = 1, 1, 1, 2
    get_cuboid_permuations(x, y, z, n)
    
    


