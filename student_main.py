import re

def interpolate_missing(numbers):
    interpolated = []
    for i, num in enumerate(numbers):
        if num is None:
            left_neighbor = next((x for x in reversed(numbers[:i]) if x is not None), None)
            right_neighbor = next((x for x in numbers[i + 1:] if x is not None), None)
            if left_neighbor is not None and right_neighbor is not None:
                interpolated.append((left_neighbor + right_neighbor) / 2)
            elif left_neighbor is not None:
                interpolated.append(left_neighbor)
            elif right_neighbor is not None:
                interpolated.append(right_neighbor)
        else:
            interpolated.append(num)
    return interpolated

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def process_batches(numbers, batch_size):
    return [max(numbers[i:i+batch_size]) for i in range(0, len(numbers), batch_size)]

def encode_string(s):
    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded

def decode_string(encoded):
    decoded = ''
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        decoded += encoded[i + 1] * count
        i += 2
    return decoded

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def regex_search(strings, pattern):
    return [s for s in strings if re.match(pattern, s)]

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

from collections import defaultdict

def group_by_key(data, key):
    grouped = defaultdict(list)
    for d in data:
        grouped[d[key]].append(d['value'])
    return dict(grouped)

def remove_outliers(numbers):
    mean = sum(numbers) / len(numbers)
    std_dev = (sum((x - mean) ** 2 for x in numbers) / len(numbers)) ** 0.5
    return [x for x in numbers if abs(x - mean) <= 2 * std_dev]
