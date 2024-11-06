from dataclasses import dataclass


@dataclass
class ClockTime:
    """
    DTO для хранения времени в часах, минутах и секундах.

    Attributes:
        hour (int): Часы.
        minute (int): Минуты.
        second (int): Секунды.
    """
    hour: int
    minute: int
    second: int
