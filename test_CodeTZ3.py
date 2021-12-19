from CodeTZ3 import my_min, my_max, my_sum, my_multiplication, random_array, my_read, time_from_time, add_list
from functools import reduce
from operator import mul
import os


def test_my_min():
    assert my_min(["1", "436"]) == 1
    assert my_min(["4", "78", "123"]) == 4
    assert my_min(["7", "12", "164", "766632", "3", "2"]) == 2
    array = sorted(random_array(1_000, -100, 100))
    assert my_min(array) == min(array)


def test_my_max():
    assert my_max(["1", "436"]) == 436
    assert my_max(["4", "78", "123"]) == 123
    assert my_max(["7", "12", "164", "7666", "3", "2"]) == 7666
    array = sorted(random_array(1_000, -100, 100))
    assert my_max(array) == max(array)


def test_my_sum():
    assert my_sum(["1", "436"]) == 437
    assert my_sum(["4", "78", "123"]) == 205
    assert my_sum(["7", "12", "164", "7666", "3", "2"]) == 7854
    array = sorted(random_array(1_000, -100, 100))
    assert my_sum(array) == sum(array)


def test_my_multiplication():
    assert my_multiplication(["1", "436"]) == 436
    assert my_multiplication(["4", "78", "123"]) == 38376
    assert my_multiplication(["7", "12", "164", "7666", "3", "2"]) == 633640896
    array = sorted(random_array(1_000, -100, 100))
    assert my_multiplication(array) == reduce(mul, array)


def test_work_with_new():
    my_file = open("NewFile.txt", "w+")
    my_file.write("000000012341 01003 0011100 343727 222222")
    my_file.close()
    assert my_read("NewFile.txt") == ['000000012341', '01003', '0011100', '343727', '222222']
    os.remove("NewFile.txt")


def test_time_of_work():
    my_file = open("NewFile.txt", "w+")
    my_file.write("000000012341 01003 0011100 343727 222222 4553 2345453 4433453453 25253453 534536546 3543534543")
    my_file.close()
    list_12 = my_read("NewFile.txt")
    list_123 = add_list(list_12)
    os.remove("NewFile.txt")
    assert time_from_time(my_multiplication(list_123)) >= time_from_time(my_multiplication(list_12))
    print(time_from_time(my_multiplication(list_123)), time_from_time(my_multiplication(list_12)))
