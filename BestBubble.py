def merge_and_count(arr, temp_arr, left, right):
    if left == right:
        return 0

    mid = (left + right) // 2
    swap_count = 0

    swap_count += merge_and_count(arr, temp_arr, left, mid)
    swap_count += merge_and_count(arr, temp_arr, mid + 1, right)

    swap_count += merge(arr, temp_arr, left, mid, right)

    return swap_count

def merge(arr, temp_arr, left, mid, right):
    left_index = left
    right_index = mid + 1
    temp_index = left
    swap_count = 0

    while left_index <= mid and right_index <= right:
        if arr[left_index] <= arr[right_index]:
            temp_arr[temp_index] = arr[left_index]
            left_index += 1
        else:
            temp_arr[temp_index] = arr[right_index]
            swap_count += (mid - left_index + 1) 
            right_index += 1
        temp_index += 1

    while left_index <= mid:
        temp_arr[temp_index] = arr[left_index]
        left_index += 1
        temp_index += 1

    while right_index <= right:
        temp_arr[temp_index] = arr[right_index]
        right_index += 1
        temp_index += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return swap_count

def count_swaps(arr, ascending=True):
    n = len(arr)
    temp_arr = [0] * n

    if ascending:
        return merge_and_count(arr, temp_arr, 0, n - 1)
    else:
        arr.reverse()
        return merge_and_count(arr, temp_arr, 0, n - 1)

n = int(input())
arr = list(map(int, input().split()))

ascending_swaps = count_swaps(arr.copy(), ascending=True)
descending_swaps = count_swaps(arr.copy(), ascending=False)

print(min(ascending_swaps, descending_swaps), end="")
