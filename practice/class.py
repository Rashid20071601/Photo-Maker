# Импорт библиотек
from PIL import Image, ImageDraw, ImageFont


# Класс для создания постов с изображениями и текстом
class PostMaker:
    def __init__(self, name_photo):
        # Инициализация объекта с загрузкой и уменьшением изображения
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        # Метод для вставки другого изображения в основное
        paste_image = Image.open(name_photo)
        w, h = paste_image.size
        paste_image = paste_image.resize((w // 4, h // 4))
        self.image.paste(paste_image, (self.w - 1100, self.h - 950))

    def upgrade(self, text, color):
        # Метод для добавления текста на изображение
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('font.ttf', 150)
        draw.text((self.w - 1100, self.h - 750), text=text, fill=color, font=font)

    def show(self):
        # Метод для отображения итогового изображения
        self.image.show()


# Создание объекта и выполнение операций
img = PostMaker('image.jpeg')
img.paste('moon.png')
img.upgrade('Hello', 'yellow')
img.show()
