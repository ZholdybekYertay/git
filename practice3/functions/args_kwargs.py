# 1
def sum_all(*args):
    print(sum(args))

sum_all(1, 2, 3, 4)


# 2
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Tom", age=25)


# 3
def mix(a, b, *args):
    print(a, b, args)

mix(1, 2, 3, 4, 5)


# 4
def show_data(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_data(1, 2, name="Alice", age=22)
