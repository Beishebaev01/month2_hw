from random import randint
from settings import Settings


class GuessNumber:
    def __init__(self):
        self.settings = Settings()
        self.capital = self.settings.INITIAL_CAPITAL
        self.attempts = self.settings.ATTEMPTS
        self.random_num = self.generate_random_num()

    def generate_random_num(self):
        return randint(self.settings.MIN_NUMBER, self.settings.MAX_NUMBER)

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("Введите ваше число: "))
                if self.settings.MIN_NUMBER <= guess <= self.settings.MAX_NUMBER:
                    return guess
                else:
                    print(f"Число должно быть в диапазоне от {self.settings.MIN_NUMBER} до {self.settings.MAX_NUMBER}.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

    def get_user_bet(self):
        while True:
            try:
                bet = int(input("Сделайте ставку: "))
                if bet > 0:
                    return bet
                else:
                    print("Ставка должна быть положительным числом.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

    def play(self):
        print(f'Угадайте число от {self.settings.MIN_NUMBER} до {self.settings.MAX_NUMBER}.')
        print(f'У вас {self.attempts} попыток. Начальная капитал: {self.capital}.')

        while self.attempts > 0:
            print(f"\nПопытка {self.settings.ATTEMPTS - self.attempts + 1}.")
            print(f"Ваш текущий капитал: {self.capital}")

            guess = self.get_user_guess()
            bet = self.get_user_bet()

            if bet > self.capital:
                print("Ставка превышает ваш капитал. Попробуйте снова.")
                continue

            if guess == self.random_num:
                self.capital += bet
                print(f"Поздравляем! Вы угадали число. Ваш капитал теперь: {self.capital}")
                break
            else:
                self.capital -= bet
                print(f"Неверно. Ваш капитал теперь: {self.capital}")

            self.attempts -= 1

        if self.attempts == 0:
            print(f"\nИгра окончена. Загаданное число было: {self.random_num}")
