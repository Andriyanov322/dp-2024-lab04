from datetime import datetime
from dataclasses import dataclass
from interfaces.base_digital_clock import BaseDigitalClock
from interfaces.base_analog_clock import BaseAnalogClock
from consts.date_consts import DayNightDivision

# Константы для преобразования времени в углы
HOURS_TO_DEGREES = 30  # 360 / 12 часов
MINUTES_TO_DEGREES = 6  # 360 / 60 минут
SECONDS_TO_DEGREES = 6  # 360 / 60 секунд

# Константы для работы с временем
HOURS_IN_HALF_DAY = 12
MIDNIGHT_HOUR = 0


@dataclass
class ClockAngles:
    """
    Датакласс для хранения углов часовой, минутной, секундной стрелок и деления дня/ночи.

    Attributes:
        hour_angle (float): Угол часовой стрелки в градусах.
        minute_angle (float): Угол минутной стрелки в градусах.
        second_angle (float): Угол секундной стрелки в градусах.
        day_night_division (DayNightDivision): Деление дня/ночи (AM или PM).
    """
    hour_angle: float
    minute_angle: float
    second_angle: float
    day_night_division: DayNightDivision


class DigitalClockAdapter(BaseDigitalClock):
    """
    Адаптер для использования AnalogClock через интерфейс BaseDigitalClock.
    """

    def __init__(self, analog_clock: BaseAnalogClock):
        """
        Инициализирует новый экземпляр DigitalClockAdapter с экземпляром BaseAnalogClock.

        :param analog_clock: экземпляр, реализующий интерфейс BaseAnalogClock.
        """
        self.analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Устанавливает текущее время, преобразуя его из формата datetime в углы для аналоговых часов.

        :param date: дата и время в формате datetime.
        :raises ValueError: если дата не соответствует правильному формату.
        """
        if not isinstance(date, datetime):
            raise ValueError("Входные данные должны быть в формате datetime.")

        angles = self._convert_to_angles(date)

        self.analog_clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=angles.hour_angle,
            minute_angle=angles.minute_angle,
            second_angle=angles.second_angle,
            day_night_division=angles.day_night_division
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

    def _convert_to_angles(self, date: datetime) -> ClockAngles:
        """
        Преобразует datetime в углы и деление дня/ночи.

        :param date: дата и время в формате datetime.
        :return: объект ClockAngles с углами для часов, минут, секунд и делением дня/ночи.
        """
        hour_angle = (date.hour % HOURS_IN_HALF_DAY) * HOURS_TO_DEGREES
        minute_angle = date.minute * MINUTES_TO_DEGREES
        second_angle = date.second * SECONDS_TO_DEGREES
        day_night_division = DayNightDivision.AM if date.hour < HOURS_IN_HALF_DAY else DayNightDivision.PM
        return ClockAngles(hour_angle, minute_angle, second_angle, day_night_division)

    def _convert_angles_to_time(self):
        """
        Преобразует углы в часы, минуты и секунды.

        :return: кортеж из часов, минут и секунд.
        """
        hour = int(self.analog_clock.get_hour_angle() / HOURS_TO_DEGREES) % HOURS_IN_HALF_DAY
        minute = int(self.analog_clock.get_minute_angle() / MINUTES_TO_DEGREES)
        second = int(self.analog_clock.get_second_angle() / SECONDS_TO_DEGREES)

        # Обработка AM/PM
        if self.analog_clock.day_night_division == DayNightDivision.PM and hour != HOURS_IN_HALF_DAY:
            hour += HOURS_IN_HALF_DAY
        if self.analog_clock.day_night_division == DayNightDivision.AM and hour == HOURS_IN_HALF_DAY:
            hour = MIDNIGHT_HOUR

        return hour, minute, second
