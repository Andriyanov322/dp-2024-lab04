from dataclasses import dataclass
from consts.date_consts import DayNightDivision

@dataclass
class ClockAngles:
    """
    DTO для хранения углов часовой, минутной, секундной стрелок и деления дня/ночи.

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
