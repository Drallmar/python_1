import random


def pass_gen(len_pass):
    password = ''
    for i in range(len_pass):
        password += chr(random.randint(33, 126))
    return password


print('Привет! Я генератор паролей!')
print('Введите, сколько символов должно быть в пароле')
pas = int(input())
print('Ваша пароль:', pass_gen(pas))
