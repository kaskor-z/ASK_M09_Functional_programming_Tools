


def apply_all_func(int_list, *functions):
    reuslts = {}
    for function in functions:
        reuslts.update({function.__name__: function(int_list)})
    return reuslts


print('\n', apply_all_func([6, 20, 15, 9], max, min), end='  ')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
