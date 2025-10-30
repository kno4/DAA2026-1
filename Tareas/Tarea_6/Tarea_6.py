def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arreglo = [25, 255, 16, 17, 256, 14, 2, 87, 35, 23]
merge_sort(arreglo)
print(arreglo)

def mochila_dp(values, weights, w_max):
    n = len(values)
    dp = [[0 for _ in range(w_max + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        actual_w = weights[i - 1]
        actual_v = values[i - 1]
        for w in range(w_max + 1):
            value_no_item = dp[i - 1][w]
            if actual_w <= w:
                value_item = actual_v + dp[i - 1][w - actual_w]
                dp[i][w] = max(value_no_item, value_item)
            else:
                dp[i][w] = value_no_item
    return dp[n][w_max]

valores = [15, 10 , 25]
pesos = [10, 20, 30]
peso_max = 50
max_val = mochila_dp(valores, pesos, peso_max)
print(max_val)
