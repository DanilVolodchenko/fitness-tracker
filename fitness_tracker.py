from typing import ClassVar
from dataclasses import asdict, dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float

    calories: float

    MASSAGE = (
        'Тип тренировки: {training_type}; '
        'Длительность: {duration:.3f} ч.; '
        'Дистанция: {distance:.3f} км; '
        'Ср. скорость: {speed:.3f} км/ч; '
        'Потрачено ккал: {calories:.3f}.'
    )

    def get_message(self) -> str:
        """Вывод сообщения."""

        return self.MASSAGE.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""

    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000
    MIN_IN_H: ClassVar[float] = 60

    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        raise NotImplementedError(
            'В родительском классе эта функция ничего не возвращает'
        )

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        return InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


@dataclass
class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: ClassVar[int] = 18
    CALORIES_MEAN_SPEED_SHIFT: ClassVar[float] = 1.79

    def get_spent_calories(self) -> float:
        """Подсчет затраченных калорий при беге."""

        return (
                (
                        self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                        + self.CALORIES_MEAN_SPEED_SHIFT
                )
                * self.weight
                / self.M_IN_KM
                * self.duration
                * self.MIN_IN_H
        )


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WEIGHT_MULTIPLIER: ClassVar[float] = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER: ClassVar[float] = 0.029
    KMH_IN_MSEC: ClassVar[float] = 0.278
    CM_IN_M: ClassVar[int] = 100

    height: int

    def get_spent_calories(self) -> float:
        """Подсчет затраченных калорий при ходьбе."""

        return (
                (
                        self.CALORIES_WEIGHT_MULTIPLIER * self.weight
                        + (
                                (self.get_mean_speed() * self.KMH_IN_MSEC) ** 2
                                / (self.height / self.CM_IN_M)
                        )
                        * self.CALORIES_SPEED_HEIGHT_MULTIPLIER
                        * self.weight
                )
                * self.duration
                * self.MIN_IN_H
        )


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: ClassVar[float] = 1.38
    CALORIES_MEAN_SWIM_MULTIPLIER: ClassVar[float] = 1.1
    CALORIES_MEAN_SWIM_SHIFT: ClassVar[int] = 2

    length_pool: int
    count_pool: int

    def get_mean_speed(self) -> float:
        """Подсчет средней скорости для плавания."""

        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Подсчет затраченных калорий при плавании."""

        return (
                (self.get_mean_speed() + self.CALORIES_MEAN_SWIM_MULTIPLIER)
                * self.CALORIES_MEAN_SWIM_SHIFT
                * self.weight
                * self.duration
        )
