#!/usr/bin/python3

from utils.file import get_input
from functools import reduce
import re

PROD = get_input("input.prod")
TEST = get_input("input.test")


def one():
    test_result = sum_valid(TEST.splitlines())
    prod_result = sum_valid(PROD.splitlines())
    return f"P1-TEST: {test_result}\n" + f"P1-PROD: {prod_result}"


def sum_valid(games, id=0, result=0):
    game = games.pop(0).split(":")[1]
    id += 1
    if is_valid(game.split(";")):
        result += id
    if games:
        result = sum_valid(games, id=id, result=result)
    return result


def is_valid(sets, valid=True):
    pull = sets.pop(0).split(",")
    valid = possible(pull)
    if sets and valid:
        valid = is_valid(sets)
    return valid


def possible(dice, valid=True):
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    die = dice.pop(0)
    num = int(re.search(r"\d+", die).group(0))
    color = re.search(r"[a-z]+", die).group(0)
    bag[color] -= num
    if bag[color] < 0:
        valid = False
    if dice and valid:
        valid = possible(dice)
    return valid


def two():
    test_result = sum_power(TEST.splitlines())
    prod_result = sum_power(PROD.splitlines())
    return f"P2-TEST: {test_result}\n" + f"P2-PROD: {prod_result}"


def sum_power(games, result=0):
    game = games.pop(0).split(":")[1]
    bag = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    fewest = get_fewest(game.split(";"), bag)
    result += reduce((lambda x, y: x*y), fewest.values())
    if games:
        result = sum_power(games, result)
    return result


def get_fewest(sets, bag):
    pull = sets.pop(0).split(",")
    bag = count_bag(pull, bag)
    if sets:
        bag = get_fewest(sets, bag)
    return bag


def count_bag(dice, bag):
    die = dice.pop(0)
    num = int(re.search(r"\d+", die).group(0))
    color = re.search(r"[a-z]+", die).group(0)
    if bag[color] < num:
        bag[color] = num
    if dice:
        bag = count_bag(dice, bag)
    return bag
