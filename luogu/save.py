# budgets = []
# for i in range(12):
#     x = int(input())
#     budgets.append(x)

budgets = [int(input()) for _ in range(12)]

nums= list(map(int, input().split()))
result=nums[:-1][::-1]
print(result)

nums = list(map(int, input().split()))
nums.pop()      # 删除并返回最后一个元素（0）
nums.reverse()  # 将列表原地反转
print(nums)
# 输出: [6, 5, 4, 3, 2, 1]

nums = list(map(int, input().split()))
# 先切片去掉最后一个，再用 reversed 反转
result = list(reversed(nums[:-1]))
print(result)
# 输出: [6, 5, 4, 3, 2, 1]