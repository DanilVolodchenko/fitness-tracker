import pytest

import fitness_tracker
import main


@pytest.mark.parametrize('work_type, input_data', [
    ('SWM', [720, 1, 80, 25, 40]),
    ('RUN', [15000, 1, 75]),
    ('WLK', [9000, 1, 75, 180])
])
def test_read_package(work_type, input_data):
    """Тест функции 'read_package'."""

    if work_type == 'SWM':
        swimming = fitness_tracker.Swimming(*input_data)
        result = main.read_package(work_type, input_data)

        assert isinstance(result, fitness_tracker.Swimming), ('Результат функции "read_packege" должен быть объект'
                                                              ' класса "Swimming"')
        assert result == swimming, 'Функция "read_package" вернула неверный результат'

    if work_type == 'RUN':
        running = fitness_tracker.Running(*input_data)
        result = main.read_package(work_type, input_data)

        assert isinstance(result, fitness_tracker.Running), ('Результат функции "read_packege" должен быть объект'
                                                             ' класса "Running"')
        assert result == running, 'Функция "read_package" вернула неверный результат'

    if work_type == 'WLK':
        sport_walking = fitness_tracker.SportsWalking(*input_data)
        result = main.read_package(work_type, input_data)

        assert isinstance(result, fitness_tracker.SportsWalking), ('Результат функции "read_packege" должен быть объект'
                                                                   ' класса "SportWalking"')
        assert result == sport_walking, 'Функция "read_package" вернула неверный результат'
