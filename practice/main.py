# Импорт библиотек
from PIL import Image, ImageDraw, ImageFont

# Функция для обработки изображения
def photo(name):
    photo1 = Image.open(name)  # Открытие изображения
    resized_photo = photo1.resize((photo1.width // 2, photo1.height // 2))  # Уменьшение размера
    print(photo1.format, photo1.size, photo1.mode)  # Вывод информации
    print(resized_photo.size)  # Вывод нового размера
    return resized_photo  # Возврат изображения

# Обработка изображений
img = photo('image.jpeg')
img2 = Image.open('moon.png')
img2 = img2.resize((img2.width // 4, img2.height // 4))  # Уменьшение второго изображения

# Вставка второго изображения
w, h = img.size
img.paste(img2, (w - 1100, h - 950))

# Добавление текста
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('font.ttf', 150)
draw.text((w - 1100, h - 750), 'Hello', fill='yellow', font=font)

img.show()  # Отображение изображения
