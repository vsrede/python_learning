from random import *
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно',
'Попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
'Сконцентрируйся и спроси опять','Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Введите имя ')
print('Привет', name)
def question_answer ():
    question = input('Введите ваш вопрос ')
    print(choice(answers))
question_answer()
while True:
    a = input('Хотите ли еще задать вопрос? Введите y если да, n если нет ')
    if a == 'y':
        question_answer()
    elif a == 'n':
        print('Возвращайся если возникнут вопросы!')
        break
    else:
        print('Введите y или n')
