values_list = [45, 'dynamo', False]
values_list_2 = [54.32, 'Строка']
values_dict = {'a': 37, 'b': 'shakhtar', 'c': True}
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, c = 42)

