def kadane(arr):
    max_current = max_global = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            s = i
        else :
            max_current += arr[i]

        if max_current > max_global:
            max_global = max_current
            start = s
            end = i
    return max_global , start , end  