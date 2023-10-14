# 使用任意位置实参和任意数量的实参
def make_pizza(size, *toppings):
    print(f"making {size} pizza")
    for topping in toppings:
        print(f"-{topping}")


make_pizza(3, 'a', 'b', 3)


# 使用任意数量的关键字实参

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_info = build_profile('z', 's', location='sx', age='3')
print(user_info)
