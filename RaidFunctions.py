import os

def check_and_create_file(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.writelines('\n' * 65)



def replace_line_in_file(filename, line_num, text):
    with open(filename, 'r') as file:
        lines = file.readlines()

    if 0 <= line_num < len(lines):
        lines[line_num] = text + '\n'

    with open(filename, 'w') as file:
        file.writelines(lines)


def read_specific_line(filename, line_num):
    with open(filename, 'r') as file:
        for current_line_num, line in enumerate(file):
            if current_line_num == line_num:
                return line.rstrip('\n')

def xor_hex_numbers(hex1, hex2):
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    xor_result = num1 ^ num2

    return hex(xor_result)[2:].upper()


def split_hex_number(hex_number, chunk_size=7):
    if hex_number.startswith("0x"):
        hex_number = hex_number[2:]

    padded_hex_number = hex_number.zfill((len(hex_number) + chunk_size - 1) // chunk_size * chunk_size)

    chunks = [padded_hex_number[max(i - chunk_size, 0):i] for i in range(len(padded_hex_number), 0, -chunk_size)]

    chunks.reverse()

    return chunks

def is_line_empty(filename, line_num):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if 0 <= line_num < len(lines):
            return lines[line_num].strip() == ''


def write(address, num):
    filename_0 = 'disk0.txt'
    check_and_create_file(filename_0)
    filename_0 = 'disk1.txt'
    check_and_create_file(filename_0)
    filename_0 = 'disk2.txt'
    check_and_create_file(filename_0)
    splitted_num = split_hex_number(num)
    first_part = splitted_num[0]
    second_part = splitted_num[1]
    first_with_second = xor_hex_numbers(first_part, second_part)
    if address.startswith('0') and len(address) == 2:
        address = int(address[1])
    else:
        address = int(address)
    modular_division = address % 3
    if (modular_division == 0):
        replace_line_in_file('disk0.txt', address, str(first_part))
        replace_line_in_file('disk1.txt', address, str(second_part))
        replace_line_in_file('disk2.txt', address, str(first_with_second))
    elif (modular_division == 1):
        replace_line_in_file('disk0.txt', address, str(first_part))
        replace_line_in_file('disk1.txt', address, str(first_with_second))
        replace_line_in_file('disk2.txt', address, str(second_part))
    else:
        replace_line_in_file('disk0.txt', address, str(first_with_second))
        replace_line_in_file('disk1.txt', address, str(first_part))
        replace_line_in_file('disk2.txt', address, str(second_part))

def read(address):
    filename_0 = 'disk0.txt'
    check_and_create_file(filename_0)
    filename_0 = 'disk1.txt'
    check_and_create_file(filename_0)
    filename_0 = 'disk2.txt'
    check_and_create_file(filename_0)
    if address.startswith('0') and len(address) == 2:
        address = int(address[1])
    else:
        address = int(address)
    modular_division = address % 3
    if (modular_division == 0):
        if (is_line_empty('disk0.txt', address)):
            ans_first_part = read_specific_line('disk1.txt', address)
            ans_second_part = read_specific_line('disk2.txt', address)
            prev_ans = xor_hex_numbers(ans_first_part, ans_second_part)
            ans = prev_ans + ans_first_part
            return ans
        elif (is_line_empty('disk1.txt', address)):
            ans_first_part = read_specific_line('disk0.txt', address)
            ans_second_part = read_specific_line('disk2.txt', address)
            prev_ans = xor_hex_numbers(ans_first_part, ans_second_part)
            ans = ans_first_part + prev_ans
            return ans
        else:
            ans_first_part = read_specific_line('disk0.txt', address)
            ans_second_part = read_specific_line('disk1.txt', address)
            ans = ans_first_part + ans_second_part
            return ans
    elif (modular_division == 1):
        if (is_line_empty('disk0.txt', address)):
            ans_first_part = read_specific_line('disk1.txt', address)
            ans_second_part = read_specific_line('disk2.txt', address)
            prev_ans = xor_hex_numbers(ans_first_part, ans_second_part)
            ans = prev_ans + ans_first_part
            return ans
        elif (is_line_empty('disk2.txt', address)):
            ans_first_part = read_specific_line('disk0.txt', address)
            ans_second_part = read_specific_line('disk1.txt', address)
            prev_ans = xor_hex_numbers(ans_first_part, ans_second_part)
            ans = ans_first_part + prev_ans
            return ans
        else:
            ans_first_part = read_specific_line('disk0.txt', address)
            ans_second_part = read_specific_line('disk2.txt', address)
            ans = ans_first_part + ans_second_part
            return ans
    else:
        if (is_line_empty('disk1.txt', address)):
            ans_first_part = read_specific_line('disk0.txt', address)
            ans_second_part = read_specific_line('disk2.txt', address)
            prev_ans = xor_hex_numbers(ans_first_part, ans_second_part)
            ans = prev_ans + ans_first_part
            return ans
        elif (is_line_empty('disk2.txt', address)):
            ans_first_part = read_specific_line('disk0.txt', address)
            ans_second_part = read_specific_line('disk1.txt', address)
            prev_ans = xor_hex_numbers(ans_first_part, ans_second_part)
            ans = ans_second_part + prev_ans
            return ans
        else:
            ans_first_part = read_specific_line('disk1.txt', address)
            ans_second_part = read_specific_line('disk2.txt', address)
            ans = ans_first_part + ans_second_part
            return ans
