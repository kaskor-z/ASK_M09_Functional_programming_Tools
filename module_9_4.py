from random import choice

#       Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda s_1, s_2: s_1 == s_2, first, second)))

#       Замыкание:

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'w')
        list(map(lambda x: file.write(str(x) + '\n'), data_set))
        file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#    Метод __call__:

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное', 'приблизительно', 'так точно',
                        'теоритически', 'практически')
print(first_ball())
print(first_ball())
print(first_ball())
