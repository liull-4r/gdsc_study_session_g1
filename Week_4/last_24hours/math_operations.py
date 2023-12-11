basic_operations_dict ={}
def basic_operations(a, b):
 try:
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    basic_operations_dict.update({
        "sum": sum,
        "difference": difference,
        "product": product,
        "quotient": quotient
    })
    return basic_operations_dict
 except ZeroDivisionError:
   return "the denominator must be differe from zero"
 except TypeError:
   return "please enter a valid number"
print(basic_operations(10, 1))

def power_operation(base, exponent, **kwargs):
 try:
    result = base ** exponent  
    modulo = kwargs.get('modulo') 
    if modulo is not None:
        result %= modulo  
    return result
 except TypeError:
    return "please enter a valid number"
print(power_operation(3, 4, modulo=8))


def apply_operations(operation_list):
    results = list(map(lambda x: x[0](*x[1]), operation_list))
    return results


operations = [
    (lambda x, y: x + y, (4, 5)),
    (lambda x, y: x * y, (7, 8)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)



# Updated at 2023-12-11 21:49:51