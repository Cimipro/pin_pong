from pygame import *

game = True
#Создание игрового окна
#Сделать пременные отвечающие за написание на экране надписей
#Основной класс
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y,size_x,size_y,player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

#Класс платформы (Игрока)
class Platphorm(GameSprite):
    #Функция обновления обьекта
    def update_wasd():
        self.y - self.player_speed
        pass

    def update_arrow():
        pass
#Класс мяча 
class ball(GameSprite):
    #Функция обновления обьекта
    def update():
        pass



#Экземпляры классов

#Игровой цикл
while game:
    #Сделать завешение игры по нажатию крестика
    #Сделать проверку нажатия кнопок управления
    pass
    #Реализовать отрисовку спрайтов мяча и платформ

    #Проверка взаимодействия обьектов
    