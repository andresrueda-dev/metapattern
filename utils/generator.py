import random

def generar_chispazo():
    while True:
        nums = sorted(random.sample(range(1, 57), 5))

        pares = sum(1 for n in nums if n % 2 == 0)
        if not (2 <= pares <= 3):
            continue

        rangos = [
            any(1 <= n <= 10 for n in nums),
            any(11 <= n <= 20 for n in nums),
            any(21 <= n <= 30 for n in nums),
            any(31 <= n <= 40 for n in nums),
            any(41 <= n <= 56 for n in nums),
        ]
        if not all(rangos):
            continue

        if any(nums[i]+1 == nums[i+1] for i in range(4)):
            continue

        return nums


def generar_melate():
    while True:
        nums = sorted(random.sample(range(1, 57), 6))

        pares = sum(1 for n in nums if n % 2 == 0)
        if not (2 <= pares <= 4):
            continue

        if any(nums[i]+1 == nums[i+1] for i in range(5)):
            continue

        return nums
