import time
from threading import Thread

# Константа: общее количество врагов
TOTAL_ENEMIES = 100

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name  # Имя рыцаря
        self.power = power  # Сила рыцаря
        self.days = 0  # Количество дней, которое рыцарь сражается
        self.remaining_enemies = TOTAL_ENEMIES  # Количество врагов

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.remaining_enemies > 0:
            self.days += 1  # Увеличиваем количество дней
            self.remaining_enemies -= self.power  # Уменьшаем количество врагов
            if self.remaining_enemies < 0:
                self.remaining_enemies = 0
            time.sleep(1)  # Пауза 1 секунда = 1 день
            print(
                f"{self.name} сражается {self.days} день(дня)..., осталось {self.remaining_enemies} воинов."
            )
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание и запуск потоков
if __name__ == "__main__":
    # Создаём двух рыцарей
    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 20)

    # Запускаем потоки
    first_knight.start()
    second_knight.start()

    # Ждём завершения обоих потоков
    first_knight.join()
    second_knight.join()

    # Вывод финального сообщения
    print("Все битвы закончились!")