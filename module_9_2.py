first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string_) for string_ in first_strings if len(string_) >= 5]
second_result = [(string_1, string_2) for string_1 in first_strings for string_2 in second_strings if
                 len(string_1) == len(string_2)]
third_result = [{string_: str(len(string_))} for string_ in (first_strings + second_strings) if not len(string_) % 2]

print('')
print(first_result)
print(second_result)
print(third_result)
