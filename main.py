from fitness_tracker import Training, Swimming, Running, SportsWalking


def read_package(training_type: str, input_data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    list_of_training: dict = {'SWM': Swimming,
                              'RUN': Running,
                              'WLK': SportsWalking}
    if training_type in list_of_training:
        return list_of_training[training_type](*input_data)
    else:
        raise KeyError('Такого ключа не существует!')


def main(training: Training) -> None:
    """Главная функция вызова."""

    info = training.show_training_info()

    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
