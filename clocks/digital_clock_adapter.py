from datetime import datetime
from interfaces.base_digital_clock import BaseDigitalClock
from clocks.analog_clock import AnalogClock
from consts.date_consts import DayNightDivision


class DigitalClockAdapter(BaseDigitalClock):
    """
    Адаптер для использования AnalogClock через интерфейс BaseDigitalClock.
    """

    def __init__(self):
        """
        Инициализирует новый экземпляр DigitalClockAdapter и создает экземпляр AnalogClock.
        """
        self.analog_clock = AnalogClock()

    def set_date_time(self, date: datetime) -> None:
        """
        Устанавливает текущее время, преобразуя его из формата datetime в углы для аналоговых часов.

        :param date: дата и время в формате datetime.
        :raises ValueError: если дата не соответствует правильному формату.
        """
        if not isinstance(date, datetime):
            raise ValueError("Входные данные должны быть в формате datetime.")

        hour_angle, minute_angle, second_angle, day_night_division = self._convert_to_angles(date)

        self.analog_clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=hour_angle,
            minute_angle=minute_angle,
            second_angle=second_angle,
            day_night_division=day_night_division
        )

    def get_date_time(self) -> datetime:
        """
        Возвращает текущее время в формате datetime, преобразуя углы из аналоговых часов.

        :return: дата и время в формате datetime.
        """
        year = self.analog_clock.get_year()
        month = self.analog_clock.get_month()
        day = self.analog_clock.get_day()
        hour, minute, second = self._convert_angles_to_time()

        return datetime(year, month, day, hour, minute, second)

    def get_hour_angle(self) -> float:
        """
        Возвращает угол стрелки часов.

        :return: угол стрелки часов в градусах.
        """
        return self.analog_clock.get_hour_angle()

    def get_minute_angle(self) -> float:
        """
        Возвращает угол минутной стрелки.

        :return: угол минутной стрелки в градусах.
        """
        return self.analog_clock.get_minute_angle()

    def get_second_angle(self) -> float:
        """
        Возвращает угол секундной стрелки.

        :return: угол секундной стрелки в градусах.
        """
        return self.analog_clock.get_second_angle()

    def _convert_to_angles(self, date: datetime):
        """
        Преобразует datetime в углы и деление дня/ночи.

        :param date: дата и время в формате datetime.
        :return: углы для часов, минут, секунд и деление дня/ночи.
        """
        hour_angle = (date.hour % 12) * 30  # 360 / 12
        minute_angle = date.minute * 6  # 360 / 60
        second_angle = date.second * 6  # 360 / 60
        day_night_division = DayNightDivision.AM if date.hour < 12 else DayNightDivision.PM
        return hour_angle, minute_angle, second_angle, day_night_division

    def _convert_angles_to_time(self):
        """
        Преобразует углы в часы, минуты и секунды.

        :return: кортеж из часов, минут и секунд.
        """
        hour = int(self.analog_clock.get_hour_angle() / 30) % 12  # 30 degrees per hour
        minute = int(self.analog_clock.get_minute_angle() / 6)  # 6 degrees per minute
        second = int(self.analog_clock.get_second_angle() / 6)  # 6 degrees per second

        # Обработка AM/PM
        if self.analog_clock.day_night_division == DayNightDivision.PM and hour != 12:
            hour += 12
        if self.analog_clock.day_night_division == DayNightDivision.AM and hour == 12:
            hour = 0

        return hour, minute, second
