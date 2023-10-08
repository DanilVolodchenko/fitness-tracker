from unittest import mock

import pytest

import fitness_tracker


@pytest.mark.parametrize('input_data, expected', [
    (['Swimming', 1, 75, 1, 80],
     'Тип тренировки: Swimming; '
     'Длительность: 1.000 ч.; '
     'Дистанция: 75.000 км; '
     'Ср. скорость: 1.000 км/ч; '
     'Потрачено ккал: 80.000.'
     ),
    (['Running', 4, 20, 4, 20],
     'Тип тренировки: Running; '
     'Длительность: 4.000 ч.; '
     'Дистанция: 20.000 км; '
     'Ср. скорость: 4.000 км/ч; '
     'Потрачено ккал: 20.000.'
     ),
    (['SportsWalking', 12, 6, 12, 6],
     'Тип тренировки: SportsWalking; '
     'Длительность: 12.000 ч.; '
     'Дистанция: 6.000 км; '
     'Ср. скорость: 12.000 км/ч; '
     'Потрачено ккал: 6.000.'
     ),
])
def test_InfoMessage_get_message(input_data, expected):
    """Тест метода 'get_message' класса InfoMessage."""

    info_message = fitness_tracker.InfoMessage(*input_data)

    assert hasattr(info_message, 'get_message'), ('Класс InfoMessage должен обладать'
                                                  ' методом "get_message"')

    result = info_message.get_message()

    assert isinstance(result, str), ('Метод "get_message" класса InfoMessage'
                                     ' должен возвращать тип str')
    assert result == expected, 'Метод "get_message" класса "InfoMessage" вернул неверное значение'


@pytest.mark.parametrize('input_data, expected', [
    ([9000, 1, 75], 5.85),
    ([420, 4, 20], 0.273),
    ([1206, 12, 6], 0.7838999999999999),
])
def test_Training_get_distance(input_data, expected):
    """Тест метода 'get_distance' класса Training."""

    training = fitness_tracker.Training(*input_data)

    assert hasattr(training, 'get_distance'), ('Класс Training должен обладать'
                                               ' методом "get_distance"')

    result = training.get_distance()

    assert isinstance(result, float), ('Метода "get_distance" класса Training'
                                       ' должен возвращать тип float')
    assert result == expected, 'Метод "get_distance" класса "Training" вернул неверное значение'


@pytest.mark.parametrize('input_data, expected', [
    ([9000, 1, 75], 5.85),
    ([420, 4, 20], 0.06825),
    ([1206, 12, 6], 0.065325),
])
def test_Training_get_mean_speed(input_data, expected):
    """Тест метода 'get_mean_speed' класса Training."""

    training = fitness_tracker.Training(*input_data)

    assert hasattr(training, 'get_mean_speed'), ('Класс Training должен обладать'
                                                 ' методом "get_mean_speed"')

    result = training.get_mean_speed()

    assert isinstance(result, float), ('Метода "get_mean_speed" класса Training'
                                       ' должен возвращать тип float')
    assert result == expected, 'Метод "get_mean_speed" класса "Training" вернул неверное значение'


@pytest.mark.parametrize('input_data', [
    ([9000, 1, 75]),
    ([420, 4, 20]),
    ([1206, 12, 6]),
])
def test_Training_get_spent_calories(input_data):
    """Тест метода 'get_spent_calories' класса 'Training'."""

    training = fitness_tracker.Training(*input_data)

    assert hasattr(training, 'get_spent_calories'), ('Класс "Training" должен обладать'
                                                     ' методом "get_spent_calories"')

    with pytest.raises(NotImplementedError):
        training.get_spent_calories()


def test_Training_show_training_info():
    """Тест метода 'show_training_info' класса 'Training'."""

    training = fitness_tracker.Training(*[9000, 1, 75])

    assert hasattr(training, 'show_training_info'), ('Класс "Training" должен обладать'
                                                     ' методом "show_training_info"')

    training.get_spent_calories = mock.Mock()  # Использую Mock(), чтоб метод get_spent_calories
    training.get_spent_calories.return_value = 50  # возращал результат равный 50
    result = training.show_training_info()

    assert isinstance(result, fitness_tracker.InfoMessage), ('Метод "show_training_info" класса "Training" '
                                                             'должен вернуть объект класса InfoMessage')
    assert result == fitness_tracker.InfoMessage(training_type='Training', duration=1, distance=5.85, speed=5.85,
                                                 calories=50), (
        'Метод "show_training_info" класса "Training" вернул неверный результат'
    )


@pytest.mark.parametrize('input_data, expected', [
    ([9000, 1, 75], 481.905),
    ([420, 4, 20], 14.489),
    ([1206, 12, 6], 12.812),
])
def test_Running_get_spent_calories(input_data, expected):
    """Тест метода 'get_spent_calories' класса 'Running'."""

    running = fitness_tracker.Running(*input_data)

    assert hasattr(running, 'get_spent_calories'), ('Класс "Running" должен обладать'
                                                    ' методом "get_spent_caloties"')

    result = running.get_spent_calories()

    assert isinstance(result, float), ('Метода "get_spent_calories" класса "Running"'
                                       ' должен возвращать тип float')
    assert round(result, 3) == expected, 'Метод "get_spent_calories" класса "Training" вернул неверное значение'


@pytest.mark.parametrize('input_data, expected', [
    ([9000, 1, 75, 180], 349.252),
    ([420, 4, 20, 42], 168.119),
    ([1206, 12, 6, 12], 151.544),
])
def test_SportsWalking_get_spent_calories(input_data, expected):
    """Тест метода 'get_spent_calories' класса 'SportWalking'."""

    sport_walking = fitness_tracker.SportsWalking(*input_data)

    assert hasattr(sport_walking, 'get_spent_calories'), ('Класс "SportWalking" должен обладать'
                                                          ' методом "get_spent_caloties"')

    result = sport_walking.get_spent_calories()

    assert isinstance(result, float), ('Метод "get_spent_calories" класса "SportWalking"'
                                       ' должен возвращать тип float')
    assert round(result, 3) == expected, 'Метод "get_spent_calories" класса "SportWalking" вернул неверное значение'


@pytest.mark.parametrize('input_data, expected', [
    ([720, 1, 80, 25, 40], 1.0),
    ([420, 4, 20, 42, 4], 0.042),
    ([1206, 12, 6, 12, 6], 0.005999999999999999),
])
def test_Swimming_get_mean_speed(input_data, expected):
    """Тест метода 'get_mean_speed' класса 'Swimming'."""

    swimming = fitness_tracker.Swimming(*input_data)

    assert hasattr(swimming, 'get_mean_speed'), ('Класс "Swimming" должен обладать'
                                                 ' методом "get_mean_speed"')

    result = swimming.get_mean_speed()

    assert isinstance(result, float), ('Метод "get_mean_speed" класса "Swimming"'
                                       ' должен возвращать тип float')
    assert result == expected, 'Метод "get_mean_speed" класса "Swimming" вернул неверное значение'


@pytest.mark.parametrize('input_data, expected', [
    ([720, 1, 80, 25, 40], 336.0),
    ([420, 4, 20, 42, 4], 182.72),
    ([1206, 12, 6, 12, 6], 159.264),
])
def test_Swimming_get_spent_calories(input_data, expected):
    """Тест метода 'get_spent_calories' класса 'Swimming'."""

    swimming = fitness_tracker.Swimming(*input_data)

    assert hasattr(swimming, 'get_spent_calories'), ('Класс "Swimming" должен обладать'
                                                     ' методом "get_spent_caloties"')

    result = swimming.get_spent_calories()

    assert isinstance(result, float), ('Метод "get_spent_calories" класса "Swimming"'
                                       ' должен возвращать тип float')
    assert round(result, 3) == expected, 'Метод "get_spent_calories" класса "Swimming" вернул неверное значение'
