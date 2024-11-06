from datetime import datetime
from interfaces.base_digital_clock import BaseDigitalClock
from interfaces.base_analog_clock import BaseAnalogClock
from utils.time_conversion_helper import TimeConversionHelper  # Импорт нового хелпера

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

        angles = TimeConversionHelper.convert_to_angles(date)

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

        # Используем TimeConversionHelper для получения времени
        hour, minute, second = TimeConversionHelper.convert_angles_to_time(
            self.analog_clock.get_hour_angle(),
            self.analog_clock.get_minute_angle(),
            self.analog_clock.get_second_angle(),
            self.analog_clock.day_night_division
        )

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
