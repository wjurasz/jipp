def analyze_data(data):
    numeric_values = list(filter(lambda x: isinstance(x, (int, float)), data))
    string_values = list(filter(lambda x: isinstance(x, str), data))
    tuple_values = list(filter(lambda x: isinstance(x, tuple), data))

    max_number = max(numeric_values) if numeric_values else None
    longest_string = max(string_values, key=len) if string_values else None
    largest_tuple = max(tuple_values, key=len) if tuple_values else None

    return max_number, longest_string, largest_tuple

data = [42, "hello", (1, 2, 3), 3.14, "world!", (4, 5), {"key": "value"}, [1, 2, 3, 4], "Zdanie", (7, 8, 9, 10)]

max_number, longest_string, largest_tuple = analyze_data(data)

print("Największa liczba:", max_number)
print("Najdłuższy napis:", longest_string)
print("Krotka z największą liczbą elementów:", largest_tuple)
