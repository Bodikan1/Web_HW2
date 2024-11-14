# 1
def check_division_error(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print('check_division_error\nНа нуль ділити не можна!\nСпробуйте ще раз.\n'.upper())

    return wrapper


# 2
def check_index_error(func):
    def wrapper(lst, idx):
        try:
            return func(lst, idx)
        except IndexError:
            print('check_index_error\nІндекс поза діапазоном!\n'.upper())

    return wrapper


# 3
@check_division_error
def divide(a, b):
    return a / b


# 4
@check_index_error
def get_element(lst, idx):
    return lst[idx]


print('check_division_error - 1:', divide(10, 0))
print('check_division_error - 2:', divide(10, 1))
print('------------------------------------------\n')

lst = [1, 2, 3, 4, 5]
print('check_index_error - 1:', get_element(lst,11))
print('check_index_error - 2:', get_element(lst,2))
