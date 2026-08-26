# task one
def calculate_price(item_name: str, price: float, tax_rate: float = 0.14, discount: float = 0.0):
    final_price = (price - discount) * (1 + tax_rate)
    return final_price

print(f"{calculate_price('Mouse', 100.0):.2f}")
print(f"{calculate_price('Keyboard', 200.0, discount=20.0):.2f}")


# task two
def summarize_event(event_name: str, *attendees: str, **metadata):
    print("Event:-", event_name, " | ", "Attendees:- ", len(attendees))
    print("Attendees:- ", end="")
    for a in attendees:
        print(a, " ", end="", )
    print()
    print("Details:- ", end="")
    for key, value in metadata.items():
        print(key, " : ", value, " | ", end="")

summarize_event('Python Lab', 'Ali', 'Sara', 'Omar', room='Lab 3', date='Today')

# task three
get_cube = lambda x: x ** 3
full_name = lambda first , last: f"{first} {last}"
is_adult = lambda age: True if age >= 18 else False

print(get_cube(3)) # --> 27
print(full_name('Ahmed', 'Hassan')) # --> 'Ahmed Hassan'
print(is_adult(20)) # --> True

# task four
def sum_range(n: int) -> int:
    if n == 1 : return 1
    else:
        return n + sum_range(n - 1)

print(sum_range(5)) #--> 15
print(sum_range(10)) #--> 55

# task five
def transform_list(numbers: list, operation) -> list:
    newList = []
    for number in numbers:
        newList.append(operation(number))
    return newList

def square(x):
    return x ** 2

print(transform_list([1, 2, 3, 4], square))
print(transform_list([1, 2, 3, 4], lambda x: x * 10))

# task six
def make_formatter(prefix: str):
    def format_message(message: str) -> str:
        return f'[{prefix}] {message}'
    return format_message

info_log = make_formatter('INFO')
error_log = make_formatter('ERROR')

print(info_log('Server started successfully'))
print(error_log('Connection failed'))