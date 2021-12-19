from random import randint


def my_read(file):
    import re
    work_file = open(file)
    try:
        str_1 = work_file.read()
        num = re.findall(r'\d+', str_1)
    finally:
        work_file.close()
    return num


def my_min(list_one):
    a = min(list_one, key=lambda i: int(i))
    return int(a)


def my_max(list_one):
    b = max(list_one, key=lambda i: int(i))
    return int(b)


def my_sum(list_one):
    sum_all = 0
    for i in range(len(list_one)):
        try:
            a = int(list_one[i])
            sum_all += a
        except OverflowError:
            return None
    return sum_all


def my_multiplication(list_one):
    mult_all = 1
    for i in range(len(list_one)):
        try:
            a = int(list_one[i])
            mult_all = mult_all * a
        except OverflowError:
            return None
    return mult_all


def random_array(length, low, high):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def time_from_time(function):
    import time
    start = time.perf_counter()
    a = function
    finish = time.perf_counter()
    b = finish - start
    return format(b, ".9f")


def add_list(list_new):
    array = sorted(random_array(1_000, 1, 100000000000000000000000000000000))
    array = list(map(str, array))
    list_new = list_new + array
    return list_new


list_1 = my_read("example.txt")
max_1 = my_max(list_1)
min_1 = my_min(list_1)
sum_1 = my_sum(list_1)
mult_1 = my_multiplication(list_1)
print("Максимум:", max_1, "Минимум:", min_1, "Сумма:", sum_1, "Произведение:", mult_1)

