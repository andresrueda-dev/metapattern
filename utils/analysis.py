def calcular_aciertos(nums_str, resultado_str):
    if not resultado_str:
        return 0

    nums = set(map(int, nums_str.split(",")))
    res = set(map(int, resultado_str.split(",")))

    return len(nums & res)


# =========================
# SCORE METAPATTERN
# =========================
def score_metapattern(nums):
    score = 100

    populares = {7, 11, 13, 22}
    score -= len(set(nums) & populares) * 10

    for i in range(len(nums)-1):
        if nums[i] + 1 == nums[i+1]:
            score -= 5

    score += sum(1 for n in nums if n > 31) * 2

    return max(score, 0)


# =========================
# FRECUENCIA (HOT / COLD)
# =========================
def frecuencia_numeros(df):
    freq = {}

    for row in df["numeros"]:
        nums = list(map(int, row.split(",")))
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

    return freq


def top_calientes(freq, n=5):
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n]


def top_frios(freq, n=5):
    return sorted(freq.items(), key=lambda x: x[1])[:n]
