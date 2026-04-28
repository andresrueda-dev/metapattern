import random

def generar_chispazo():
    while True:
        nums = sorted(random.sample(range(1, 57), 5))

        pares = sum(1 for n in nums if n % 2 == 0)
        if not (2 <= pares <= 3):
            continue

        if any(nums[i]+1 == nums[i+1] for i in range(4)):
            continue

        return nums
