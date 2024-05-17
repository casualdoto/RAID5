import RaidFunctions
address_write = input('введите адрес, в который вы хотите записать 16-ричное сообщение размером 14 байт (0-63): ')
num = input('введите 16-ричное сообщение размером 14 байт: ')
RaidFunctions.write(address_write, num)
address_read = input('введите адрес, из которого вы хотите прочитать 16-ричное сообщение размером 14 байт: ')
print(RaidFunctions.read(address_read))