import random
import logging

# Настройка логирования с кодировкой utf-8
logging.basicConfig(filename='lab6.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')  # Укажите кодировку utf-8


def start_game():
    try:
        # Компьютер загадывает верхнюю границу N
        N = random.randint(1, 100)  # Например, от 1 до 100
        k = int(input("Введите количество попыток (k): "))

        # Логируем загаданное число
        logging.info(f"Компьютер загадал N: {N}, количество попыток k: {k}")

        if k < 1:
            raise ValueError("Количество попыток (k) должно быть натуральным числом.")

        # Игровой цикл
        for attempt in range(1, k + 1):
            try:
                guess = int(input(f"Попытка {attempt}: Введите ваше число от 1 до 100: "))
                logging.info(f"Пользователь ввел: {guess}")

                if guess < 1 or guess > 100:
                    logging.warning("Введено число вне диапазона.")
                    print(f"Пожалуйста, введите число от 1 до 100.")
                    continue

                if guess < N:
                    logging.info("Угаданное число меньше загаданного.")
                    print("Загаданное число больше.")
                elif guess > N:
                    logging.info("Угаданное число больше загаданного.")
                    print("Загаданное число меньше.")
                else:
                    logging.info("Пользователь угадал число.")
                    print("Вы угадали!")
                    return
            except ValueError:
                logging.error("Ошибка ввода: введено нечисловое значение.")
                print("Пожалуйста, введите корректное число.")

        # Если попытки закончились
        logging.info("Попытки закончились.")
        print(f"Попытки закончились. Загаданное число было: {N}")
    except ValueError as e:
        logging.error(f"Ошибка: {e}")
        print(e)


if __name__ == "__main__":
    start_game()
