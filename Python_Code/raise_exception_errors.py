# raise_exception_errors.py

true_values = ['yes', 'y']
false_values = ['no', 'n']

def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')
    
str_to_bool(input("please enter yes or no: "))
