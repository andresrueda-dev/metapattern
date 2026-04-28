def calcular_aciertos(nums_str, resultado_str):
    if not resultado_str:
        return 0

    nums = set(map(int, nums_str.split(",")))
    res = set(map(int, resultado_str.split(",")))

    return len(nums & res)
