from datetime import datetime
from clocks.digital_clock_adapter import DigitalClockAdapter


def main():
    """
    Главная функция, запускающая приложение для работы с цифровыми часами.
    Запрашивает у пользователя время и отображает его.
    """
    digital_clock = DigitalClockAdapter()

    while True:
        user_input = input("Введите время в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ")
        try:
            date_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
            digital_clock.set_date_time(date_time)
            break  # Выход из цикла, если ввод корректный
        except ValueError as e:
            print("Ошибка:", e)

    # Вывод текущего времени
    current_time = digital_clock.get_date_time()
    print("Текущее время:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

    # Вывод углов
    print(f"Угол стрелки часов: {digital_clock.get_hour_angle()}°")
    print(f"Угол минутной стрелки: {digital_clock.get_minute_angle()}°")
    print(f"Угол секундной стрелки: {digital_clock.get_second_angle()}°")


if __name__ == "__main__":
    main()
