
# 1er intento
#for i in nums:
#    for j in nums:
#        if i + j == objective:
#            if i in result or j in result:
#                continue
#            else:
#                result.append(i)
#                result.append(j)
# print(result)


# Mejorando

nums = [2, 7, 2, 15]
objective = 14


def suma_objetiva1(nums, objective, result=[]):
    for i in nums:
        for j in nums:
            if i == j:
                continue
            elif i + j == objective:
                result.append(i)
    return result


result = suma_objetiva1(nums, objective)
print(result)
