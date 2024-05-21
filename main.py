import RaidFunctions


def get_validated_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)


while True:
    message = input('если вы хотите записать число - введите 1, если прочитать - 2: ')

    if message == '1':
        address_write = get_validated_input(
            'введите адрес, в который вы хотите записать 16-ричное сообщение размером 14 байт (0-63): ',
            lambda x: x.isdigit() and 0 <= int(x) <= 63,
            'Введите корректный адрес (0-63)'
        )

        num = get_validated_input(
            'введите 16-ричное сообщение размером 14 байт: ',
            lambda x: RaidFunctions.validate_hex_message(x),
            'введите корректное 16-ричное сообщение размером ровно 14 байт'
        )

        RaidFunctions.write(address_write, num)

    elif message == '2':
        address_read = get_validated_input(
            'введите адрес, из которого вы хотите прочитать 16-ричное сообщение размером 14 байт (0-63): ',
            lambda x: x.isdigit() and 0 <= int(x) <= 63,
            'Введите корректный адрес (0-63)'
        )

        print(RaidFunctions.read(address_read))

    else:
        print('Введите корректный номер команды')
