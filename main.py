def count_even_numbers_in_range(arr, queries):
    def count_even_in_subarray(sub_arr):
        return sum(1 for num in sub_arr if num % 2 == 0)
    result = []
    for query in queries:
        start_idx, end_idx = query[0], query[1]
        sub_array = arr[start_idx:end_idx + 1]
        even_count = count_even_in_subarray(sub_array)
        result.append(even_count)
    return result
arr = [1, 2, 3, 4, 5]
queries = [[0, 2], [2, 4], [1, 4]]
result = count_even_numbers_in_range(arr, queries)
print("Counts of even numbers in each query:", result)
arr = [2, 1, 8, 3, 9, 6]
queries = [[0, 3], [3, 5], [1, 3], [2, 4]]
result = count_even_numbers_in_range(arr, queries)
print("Counts of even numbers in each query:", result)
