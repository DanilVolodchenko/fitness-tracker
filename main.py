from fitness_tracker import Training, Swimming, Running, SportsWalking


def _common_data_for_training():
    input_data = [int(input('Количество движений: ')),
                  float(input('Продолжительность, ч: ')),
                  float(input('Ваш вес, кг: '))]
    return input_data


def data_for_running():
    """Ввод данных для бега."""

    return _common_data_for_training()


def data_for_sport_walking():
    """Ввод данных для спортивной ходьбы."""

    common_data = _common_data_for_training()

    input_data = [float(input('Высота подъема, км: '))]

    return common_data + input_data


def data_for_swimming():
    """Ввод данных для плавания."""

    common_data = _common_data_for_training()

    input_data = [float(input('Длина бассейна, м: ')),
                  float(input('Кол-во проплытых бассейнов: '))]

    return common_data + input_data


def select_training():
    """Выбор тренировки."""

    data = {
        '1': 'RUN',
        '2': 'WLK',
        '3': 'SWM'
    }
    type_training = input('Выберите тип тренировки:\n'
                          '1 Бег;\n'
                          '2 Спортивная ходьба;\n'
                          '3 Плавание.\n')
    return data[type_training]


def training_data(type_of_training):
    """Взависимости от типа тренировки вызывается та или иная функция."""

    if type_of_training == 'RUN':
        return data_for_running()

    elif type_of_training == 'WLK':
        return data_for_sport_walking()

    else:
        return data_for_swimming()


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
    status = True
    while status:
        try:
            type_of_training = select_training()
            data_of_training = training_data(type_of_training)

        except KeyError:
            print('Нужно ввести цифру от 1 до 3!\n')

        except ValueError:
            print('Данные некорректны!\n')
        else:
            training = read_package(type_of_training, data_of_training)
            main(training)

            status = False
