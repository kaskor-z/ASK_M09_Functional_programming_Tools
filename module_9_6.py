from itertools import combinations


def all_variants(text):
    for i_ in range(len(text)):
        for i_1 in combinations(text, i_+1):
            yield i_1

a = all_variants("abc")
print()
for i in a:
    print(*i)
