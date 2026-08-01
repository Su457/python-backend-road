# 函数的定义

def greet_user():
    """显示简单的问候语""" # 文档字符串 用来描述函数的作用
    print("Hello!")

greet_user()

# 向函数传递参数

def greet_name(username): # username 形参(parameter)
    """显示简单的问候语"""
    print(f"Hello,{username.title()}!")
    # bytes.title() 其中每个单词以一个大写 ASCII 字符为开头，其余字母转为小写。

greet_name("jesse")       # "jesse" 实参(argument)

# 位置实参
def describe_pet(animal_type, pet_name):
    """
    显示宠物信息
    :param animal_type:宠物类型
    :param pet_name: 宠物名称
    """
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog','di') # 认函数调用中实参的顺序与函数定义中形参的顺序需一致

# 关键字实参
def describe_pet(animal_type, pet_name):
    """
    显示宠物的信息
    :param animal_type:宠物类型
    :param pet_name: 宠物名称
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 关键词参数的顺序无关紧要
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """
    显示宠物信息
    :param pet_name:宠物名称
    :param animal_type: 宠物类型（默认dog）
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# 一条名为 Willie 的小狗
describe_pet('willie')
# describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet(pet_name='harry', animal_type='hamster')

# 函数返回值 (让实参变成可选的)
def get_formatted_name(first_name, last_name, middle_name=''):
    """生成标准格式的姓名，每个单词首字母大写。

    如果提供中间名，则拼接为「名 中间名 姓」；
    否则拼接为「名 姓」。

    Args:
        first_name: 名
        last_name: 姓
        middle_name: 中间名，可选，默认为空字符串

    Returns:
        格式化后的完整姓名字符串
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name, age=None):
    """创建并返回一个包含个人信息的字典

    必选传入姓名信息，年龄为可选参数
    当传入age时，会将其加入字典中

    Args:
        first_name: 名字
        last_name:姓
        age:年龄， 默认为None，表示不提供年龄信

    Returns:
         包含 first、last 键的字典，若提供 age 则额外包含 age 键
    """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 传递列表
def greet_users(names):
    """
    向列表中每个用户发送简单的问候
    :param names: 用户名列表
    :return:
    """
    for name in names:
        print(f"Hello, {name.title()}!")

user_names = ['xiaodi', 'su']
greet_users(user_names)

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表 completed_models 中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models 中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop() # .pop 移除并返回列表中的最后一个条目
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    显示打印好的所有模型
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 禁止函数修改列表
# print_models(unprinted_designs[:], completed_models) #  [:] 表示创建列表的副本

# 传递任意数量实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 形参名 *toppings 中的星号让 Python 创建一个名为 toppings的元组 (*args)为通用参数名

# 任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建并返回一个包含用户所有信息的字典。

    将姓、名与其他任意关键字参数整合到一个字典中。

    Args:
        first: 用户的名字
        last: 用户的姓氏
        **user_info: 任意数量的关键字参数，用于存储用户其他信息

    Returns:
        包含用户完整信息的字典
    """
    # 把名字和姓氏添加到 user_info 字典中
    user_info['first_name'] = first
    user_info['last_name'] = last
    # 返回最终的用户信息字典
    return user_info


# 调用函数，传入名字、姓氏，以及 location、field 两个额外信息
user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')

# 打印完整的用户信息字典
print(user_profile)

# **user_info 中的两个星号让Python 创建一个名为 user_info 的字典，该字典包含函数收到的其他所有名值对
# **kwargs 通用参数名

def make_car(manufacturer, model, **kwargs):
    """创建并返回包含汽车信息的字典

    Args:
        manufacturer:汽车制造商
        model:汽车型号
        **kwargs:任意关键词参数，如颜色，选装包等

    Returns:
        包含汽车完整信息的字典
    """
    info = {
        '制造商' : manufacturer,
        '型号' : model,
        **kwargs
    }
    return info
car = make_car('subaru',
               'outback',
               color='blue',
               tow_package=True)
print(car)