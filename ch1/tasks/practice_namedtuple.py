from collections import namedtuple


User = namedtuple('User', ['name', 'sex', 'age'])

user = User(name='dingxiangyang', sex='male', age=24)

print(user._fields)

user1 = User._make(['tinghsiangyang', 'male', 16])

print(user1)
print(user1.name)
print(user1.sex)
print(user1.age)

user1 = user1._replace(age=24)

print(user1.age)
