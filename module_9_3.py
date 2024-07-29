


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(str_[0]) - len(str_[1]) for str_ in zip(first, second) if len(str_[0]) - len(str_[1]))
second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(len(second)) if i == j)

print(list(first_result))
print(list(second_result))

