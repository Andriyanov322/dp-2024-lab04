from interfaces import BaseAnalogClock
from consts import DayNightDivision


class AnalogClock(BaseAnalogClock):
    """
    Класс AnalogClock реализует интерфейс BaseAnalogClock и предоставляет функционал для работы с аналоговыми часами.

    Сохраняет текущие значения для года, месяца, дня и углы для часовой, минутной и секундной стрелок.
    """

    def __init__(self):
        """
        Инициализирует новый экземпляр AnalogClock со значениями по умолчанию.
        """
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour_angle = 0.0
        self.minute_angle = 0.0
        self.second_angle = 0.0
        self.day_night_division = DayNightDivision.AM

    def set_date_time(self, year: int, month: int, day: int, hour_angle: float, minute_angle: float,
                      second_angle: float, day_night_division: DayNightDivision):
        """
        Устанавливает текущую дату и углы для часовой, минутной и секундной стрелок.

        :param year: год.
        :param month: месяц.
        :param day: день.
        :param hour_angle: угол часовой стрелки в градусах.
        :param minute_angle: угол минутной стрелки в градусах.
        :param second_angle: угол секундной стрелки в градусах.
        :param day_night_division: текущее время суток (AM или PM).
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour_angle = hour_angle
        self.minute_angle = minute_angle
        self.second_angle = second_angle
        self.day_night_division = day_night_division

    def get_hour_angle(self) -> float:
        """
        Возвращает текущий угол часовой стрелки.

        :return: угол часовой стрелки в градусах.
        """
        return self.hour_angle

    def get_minute_angle(self) -> float:
        """
        Возвращает текущий угол минутной стрелки.

        :return: угол минутной стрелки в градусах.
        """
        return self.minute_angle

    def get_second_angle(self) -> float:
        """
        Возвращает текущий угол секундной стрелки.

        :return: угол секундной стрелки в градусах.
        """
        return self.second_angle

    def get_year(self) -> int:
        """
        Возвращает установленный год.

        :return: год.
        """
        return self.year

    def get_month(self) -> int:
        """
        Возвращает установленный месяц.

        :return: месяц.
        """
        return self.month

    def get_day(self) -> int:
        """
        Возвращает установленный день.

        :return: день.
        """
        return self.day
