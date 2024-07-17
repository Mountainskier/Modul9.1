def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results


def min_numbers(args):
    return min(args)


def max_numbers(args):
    return max(args)


def len_numbers(args):
    return len(args)


def sum_numbers(args):
    return sum(args)


def sorted_numbers(args):
    return sorted(args)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
