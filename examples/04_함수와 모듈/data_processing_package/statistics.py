# statistics.py

def sort_data(data):
    return sorted(data)


def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count


def filter_data(data, condition):
    return list(filter(condition, data))
