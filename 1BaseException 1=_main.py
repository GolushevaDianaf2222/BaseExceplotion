class InvalidArgumentException(BaseException):
    pass
def calculate_square_area(side_length):
    if side_length <= 0:
        raise InvalidArgumentException('Side length must be a positive number')
    return side_length**2

try:
    print(calculate_square_area(-5))
except InvalidArgumentException as e:
    print(f'Error: {e}')
    

 

