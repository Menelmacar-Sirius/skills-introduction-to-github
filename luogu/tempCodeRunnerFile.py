n = int(input())
nums = list(map(int, input().split()))
nums.sort()

max_len = 1
current_len = 1

for i in range(1, n):
    if nums[i] == nums[i-1] + 1:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    elif nums[i] != nums[i-1]:
        current_len = 1

print(max_len)