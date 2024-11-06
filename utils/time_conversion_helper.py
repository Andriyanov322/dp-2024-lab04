from datetime import datetime
from consts.date_consts import DayNightDivision
from consts.clock_consts import ClockConstants  # Импорт констант
from clocks.dto.clock_angles_dto import ClockAngles  # Импорт DTO

class TimeConversionHelper:
    """
    Статический класс для преобразования времени и дат в углы и обратно.
    """

    @staticmethod
    def convert_to_angles(date: datetime) -> ClockAngles:
        """
        Преобразует datetime в углы и деление дня/ночи.

        :param date: дата и время в формате datetime.
        :return: объект ClockAngles с углами для часов, минут, секунд и делением дня/ночи.
        """
        hour_angle = (date.hour % ClockConstants.HOURS_IN_HALF_DAY) * ClockConstants.HOURS_TO_DEGREES
        minute_angle = date.minute * ClockConstants.MINUTES_TO_DEGREES
        second_angle = date.second * ClockConstants.SECONDS_TO_DEGREES
        day_night_division = DayNightDivision.AM if date.hour < ClockConstants.HOURS_IN_HALF_DAY else DayNightDivision.PM
        return ClockAngles(hour_angle, minute_angle, second_angle, day_night_division)

    @staticmethod
    def convert_angles_to_time(hour_angle: float, minute_angle: float, second_angle: float, day_night_division: DayNightDivision) -> (int, int, int):
        """
        Преобразует углы в часы, минуты и секунды.

        :param hour_angle: угол часовой стрелки в градусах.
        :param minute_angle: угол минутной стрелки в градусах.
        :param second_angle: угол секундной стрелки в градусах.
        :param day_night_division: деление дня/ночи (AM или PM).
        :return: кортеж из часов, минут и секунд.
        """
        hour = int(hour_angle / ClockConstants.HOURS_TO_DEGREES) % ClockConstants.HOURS_IN_HALF_DAY
        minute = int(minute_angle / ClockConstants.MINUTES_TO_DEGREES)
        second = int(second_angle / ClockConstants.SECONDS_TO_DEGREES)

        # Обработка AM/PM
        if day_night_division == DayNightDivision.PM and hour != ClockConstants.HOURS_IN_HALF_DAY:
            hour += ClockConstants.HOURS_IN_HALF_DAY
        if day_night_division == DayNightDivision.AM and hour == ClockConstants.HOURS_IN_HALF_DAY:
            hour = ClockConstants.MIDNIGHT_HOUR

        return hour, minute, second
