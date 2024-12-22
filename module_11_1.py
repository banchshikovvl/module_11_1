# pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
from PIL import Image, ImageOps

# 1 Изменение размера изображения
size = (100, 150)
with Image.open("image.jpg") as im:
    ImageOps.contain(im, size).save("imageops_contain.jpg")
    ImageOps.cover(im, size).save("imageops_cover.jpg")
    ImageOps.fit(im, size).save("imageops_fit.jpg")
    ImageOps.pad(im, size, color="#f00").save("imageops_pad.jpg")
    im.thumbnail(size)
    im.save("image_thumbnail.jpg")
im.show()
print(im.format, im.size, im.mode)

# 2 Применить эффект к изображению
with Image.open("image.jpg") as im:
    im = im.convert("L")
im.show()

# 3 Сохранить в другой формат
try:
    with Image.open("image.jpg") as im:
        im.save("image.bmp")
        print('Формат успешно сохранен')
except OSError:
    print("cannot convert", im)

# requests - запросить данные с сайта и вывести их в консоль.
import requests
from pprint import pprint

# 1 Запрос данных с сайта
r = requests.get('https://api.github.com/events')
pprint(r.json())
# Другие типы запросов
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# r = requests.put('https://httpbin.org/put', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')

# 2 Передача параметров В URL-адресах
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
pprint(r.url)

# 3 Получение ответа сервера
r = requests.get('https://api.github.com/events')
pprint(r.text)

# matplotlib
# визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
import matplotlib.pyplot as plt
import numpy as np

# 1 Самый простой способ создать фигуру с осями — использовать функцию "pyplot.subplots"
fig, ax = plt.subplots()  # Создайте фигуру, содержащую одну ось.
ax.plot([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 4, 2, 3, 1], color='yellow', marker='o')  # Параметры фигуры.
plt.show()  # Покажите фигуру.

# 2 Построение графиков с помощью функций pyplot
x = np.linspace(0, 5, 200)  # Sample data.
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Нанесите некоторые данные на (неявные) оси.
plt.plot(x, x ** 2, label='quadratic')  # etc.
plt.plot(x, x ** 3, label='cubic')
plt.xlabel('x label')  # Название оси х
plt.ylabel('y label')  # Название оси y
plt.title("Simple Plot")  # Название фигуры
plt.legend()
plt.show()


# 3 Создание вспомогательных функций с возможностью вручную задавать цвет, толщину и стиль линии
def my_plotter(ax, data1, data2, param_dict):
    fig, ax = plt.subplots(figsize=(5, 2.9))
    x = np.arange(len(data1))
    plt.title("График")
    ax.plot(x, np.cumsum(data1), color='blue', linewidth=5, linestyle='--')
    l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=5)
    l.set_linestyle(':')
    out = ax.plot(data1, data2, **param_dict)
    return out


m = my_plotter(None, [1, 2, 3, 4, 5, 6, 7], [1, 2.5, 2, 4, 2, 3, 1], {'label': 'linear'})
plt.show()
m1 = my_plotter(None, [1, 2, 3, 4], [1, 2.5, 2, 1], {'label': 'linear'})
plt.show()
