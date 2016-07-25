__author__ = 'shaked'

# -------------------------- #
# This is a test suite for HW5 of CS101
# If you want to run it, just change the import to call your answers file:
# Where: 'mod = import_module("hw5_shaked")'
# Change to: 'mod = import_module("your_file_name")' (No .py extension needed)
# Example: mod = import_module("123454321")
# Make sure they are in the same folder.
#
# You can see that you have a test case for almost every method in the hw5 file.
# Most of the test cases, uses random data. So every run you get different inputs to your methods.
# You can run this file multiple times to make sure you catch most of the possible cases.
# If you want, you can specifically define the amount of loops each test case is making
# just by changing the 'loops' variable most of the test cases get as parameter.
# Default 'loops' is set to 16.
#
# Please be noted that this tests don't check if you stands the complexity requirements,
# they only check if you return the correct value for a given input.
#
# For now, I didn't wrote a test for Q5b.
#
# If you have any questions or you find some bugs in this test file, please contact me =)
#
# Enjoy! Shaked.
# -------------------------- #

# External Modules
from random import randint
from urllib.request import urlopen

# Internal Modules
from importlib import import_module

mod = import_module("skeleton5")
for func in mod.__dict__:
    if not func.startswith("_"):
        globals()[func] = mod.__dict__[func]
##from org.cs101.HW5.hw5_shaked import *

globals()["ERROR"] = False


def test_polynomial(loops=16):
    out("Test degree...")
    for i in range(loops):
        degree = randint(0, 16)
        coeffs = [randint(0, 16) for i in range(degree)]
        coeffs.append(randint(1, 16))

        pol = Polynomial(coeffs)
        if not pol.degree() == degree:
            globals()["ERROR"] = True
            err("Error in %s. expected %d but got: %d" % ("test_polynomial:test_degree", degree, pol.degree()))

    out("Test evaluate...")
    expected = [
        {
            "coeffs": [0, 0, 1],
            "x": 10,
            "value": 100,
        },
        {
            "coeffs": [0, 1],
            "x": 10,
            "value": 10,
        },
        {
            "coeffs": [1],
            "x": 10,
            "value": 1,
        },
        {
            "coeffs": [3, 2, 1],
            "x": 10,
            "value": 123,
        },
        {
            "coeffs": [8, 7, 6, -5],
            "x": -5,
            "value": 748,
        },
        {
            "coeffs": [7, 2.5, 9, -10, 3],
            "x": 0.5,
            "value": 9.4375,
        },
        {
            'coeffs': [0.53, 2.31, 14.84, 8.42, 1.69, 2.06],
            'x': 7.18,
            'value': 47698.98,
        },
        {
            'coeffs': [6.26, 4.52],
            'x': 10.09,
            'value': 51.87,
        },
        {
            'coeffs': [8.38, 10.09, 6.9, 14.5, 10.51, 9.91, 11.34, 0.55, 15.5, 8.08],
            'x': 11.32,
            'value': 28880345789.80,
        },
        {
            'coeffs': [10.68, 7.23, 4.57, 4.62, 14.6, 10.72, 2.51, 13.18, 10.76, 0.44, 13.99, 3.88, 4.33, 0.05, 2.84],
            'x': 6.22,
            'value': 387357177392.45,
        },
        {
            'coeffs': [2.81, 16.55, 8.84, 12.31, 16.75, 16.63, 0.75, 13.42, 3.06, 9.71, 16.33, 6.96, 6.64, 0.07, 0.83,
                       5.76],
            'x': 2.21,
            'value': 1098307.86,
        },
        {
            'coeffs': [3.26, 14.0, 1.83, 11.93, 5.74, 1.9, 12.26, 16.29, 1.96, 16.59, 5.1, 9.48, 11.11],
            'x': 6.32,
            'value': 52003625574.27,
        },
        {
            'coeffs': [0],
            'x': 7.06,
            'value': 0.00,
        },
        {
            'coeffs': [5.63, 14.12, 7.77, 0.97, 15.68, 10.84, 5.22, 3.04, 7.89, 1.06, 15.76, 7.04, 14.21, 10.46, 11.0,
                       0.83],
            'x': 7.09,
            'value': 15141332583550.78,
        },
        {
            'coeffs': [0.28, 16.26, 2.82, 10.13, 15.35, 3.76, 12.01, 15.99, 14.74],
            'x': 14.79,
            'value': 36352020203.90,
        },
        {
            'coeffs': [15.28, 6.67, 16.42, 6.01, 7.59, 3.46, 4.18, 13.3, 15.67, 15.49, 2.82],
            'x': 6.00,
            'value': 356894567.14,
        },
        {
            'coeffs': [1.1, 10.21, 16.37, 13.51, 11.15, 14.74, 0.3, 9.43],
            'x': 7.35,
            'value': 11329900.10,
        },
        {
            'coeffs': [13.12, 16.71, 7.67, 7.75, 11.0, 14.83, 7.69, 6.49, 13.04, 16.22],
            'x': 5.65,
            'value': 110249909.00,
        },
        {
            'coeffs': [12.92, 11.52, 3.04, 8.59, 2.54, 14.81, 14.38, 6.37, 10.2],
            'x': 15.19,
            'value': 30288362046.51,
        },
        {
            'coeffs': [11.61, 6.56, 7.68, 1.6, 7.25, 3.24, 0.14],
            'x': 6.84,
            'value': 79643.85,
        },
        {
            'coeffs': [14.16, 15.95, 15.07],
            'x': 14.10,
            'value': 3235.12,
        },
    ]

    epsilon = 0.01
    for data in expected:
        pol = Polynomial(data["coeffs"])
        actual_value = pol.evaluate(data["x"])
        if not abs(actual_value - data["value"]) <= epsilon:
            globals()["ERROR"] = True
            err(
                "Error in %s. Expected %.2f but got %.2f." % (
                    "test_polynomial:test_evaluate", data["value"], actual_value))

    out("Test derivative...")
    expected = [
        {
            'coeffs': [14.27, 0.79, 15.01, 10.43, 7.55, 10.82, 7.98, 10.86],
            'deriv': [0.79, 30.02, 31.29, 30.2, 54.1, 47.88, 76.02],
        },
        {
            'coeffs': [9, 16, 9, 13, 1],
            'deriv': [16.0, 18.0, 39.0, 4.0],
        },
        {
            'coeffs': [10, 6, 14, 3, 3, 10, 3, 7],
            'deriv': [6.0, 28.0, 9.0, 12.0, 50.0, 18.0, 49.0],
        },
        {
            'coeffs': [0],
            'deriv': [0],
        },
        {
            'coeffs': [13, 8],
            'deriv': [8.0],
        },
        {
            'coeffs': [6.71, 11.62],
            'deriv': [11.62],
        },
        {
            'coeffs': [9.43, 16.52, 9.96, 2.22, 11.23],
            'deriv': [16.52, 19.92, 6.66, 44.92],
        },
        {
            'coeffs': [13, 15],
            'deriv': [15.0],
        },
    ]

    for data in expected:
        pol = Polynomial(data["coeffs"])
        actual_derive = pol.derivative()
        if not actual_derive.coeffs == data["deriv"]:
            globals()["ERROR"] = True
            err(
                "Error in %s. Expected %s but got %s." % (
                    "test_polynomial:test_derive", str(data["deriv"]), str(actual_derive.coeffs)))

    out("Test add polynomials...")
    expected = [
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [1, 2, 3],
            'combined': [[2, 4, 6]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [0],
            'combined': [[1, 2, 3]],
        },
        {
            'coeffs1': [0],
            'coeffs2': [1, 2, 3],
            'combined': [[1, 2, 3]],
        },
        {
            'coeffs1': [0],
            'coeffs2': [0],
            'combined': [[0]],
        },
        {
            'coeffs1': [1, 2, 3, 4, 5],
            'coeffs2': [1, 2, 3],
            'combined': [[2, 4, 6, 4, 5]],
        },
        {
            'coeffs1': [1, 2, 3, 4, 5],
            'coeffs2': [-1, -2, -3],
            'combined': [[0, 0, 0, 4, 5]],
        },
        {
            'coeffs1': [7.5, 7.5, 7.5, 0, 7],
            'coeffs2': [0.5, 1.5, 2, 0, 3],
            'combined': [[8, 9, 9.5, 0, 10]],
        },
        {
            'coeffs1': [0, 0, 0, 0, 0, 1],
            'coeffs2': [1],
            'combined': [[1, 0, 0, 0, 0, 1]],
        },
        {
            'coeffs1': [1],
            'coeffs2': [0, 0, 0, 0, 0, 1],
            'combined': [[1, 0, 0, 0, 0, 1]],
        },
        {
            'coeffs1': [0, 0, 0, 0, 9],
            'coeffs2': [0, 0, 0, 0, 9],
            'combined': [[0, 0, 0, 0, 18]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [-1, -2, -3],
            'combined': [[0]],
        },
        {
            'coeffs1': [3, 1, 4],
            'coeffs2': [3, 2, -4],
            'combined': [[6, 3]],
        },
        {
            'coeffs1': [3, 3, 3, 3],
            'coeffs2': [-3, 3, -3, -3],
            'combined': [[0, 6]],
        },
    ]

    for data in expected:
        poly1 = Polynomial(data["coeffs1"])
        poly2 = Polynomial(data["coeffs2"])
        actual = poly1 + poly2
        if not actual.coeffs in data["combined"]:
            globals()["ERROR"] = True
            err(
                "Error in %s. Expected %s but got %s. Run on input: p1=%s p2=%s" % (
                    "test_polynomial:test_add", str(data["combined"]), str(actual.coeffs), str(data["coeffs1"]),
                    str(data["coeffs2"])))

    out("Test sub polynomials...")
    expected = [
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [1, 2, 3],
            'combined': [[0]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [1],
            'combined': [[0, 2, 3]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [0, 2],
            'combined': [[1, 0, 3]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [0, 2, 3],
            'combined': [[1]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [0],
            'combined': [[1, 2, 3]],
        },
        {
            'coeffs1': [0],
            'coeffs2': [1, 2, 3],
            'combined': [[-1, -2, -3]],
        },
        {
            'coeffs1': [0],
            'coeffs2': [0],
            'combined': [[0]],
        },
        {
            'coeffs1': [1, 2, 3, 4, 5],
            'coeffs2': [1, 2, 3],
            'combined': [[0, 0, 0, 4, 5]],
        },
        {
            'coeffs1': [7.5, 7.5, 7.5, 0, 7],
            'coeffs2': [0.5, 1.5, 2, 0, 3],
            'combined': [[7, 6, 5.5, 0, 4]],
        },
        {
            'coeffs1': [0, 0, 0, 0, 0, 1],
            'coeffs2': [1],
            'combined': [[-1, 0, 0, 0, 0, 1]],
        },
        {
            'coeffs1': [1],
            'coeffs2': [0, 0, 0, 0, 0, 1],
            'combined': [[1, 0, 0, 0, 0, -1]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [-1, -2, -3],
            'combined': [[2, 4, 6]],
        },
        {
            'coeffs1': [3, 1, 4],
            'coeffs2': [3, 2, -4],
            'combined': [[0, -1, 8]],
        },
        {
            'coeffs1': [3, 3, 3, 3],
            'coeffs2': [-3, 3, -3, -3],
            'combined': [[6, 0, 6, 6]],
        },
        {
            'coeffs1': [0, 0, 0, 0, 9],
            'coeffs2': [0, 0, 0, 0, 9],
            'combined': [[0]],
        },
        {
            'coeffs1': [1, 2, 3, 4, 5],
            'coeffs2': [5, 4, 3, 2, 1],
            'combined': [[-4, -2, 0, 2, 4]],
        },
        {
            'coeffs1': [0, 0, 3],
            'coeffs2': [-1, -1, 3],
            'combined': [[1, 1]],
        },
    ]

    for data in expected:
        poly1 = Polynomial(data["coeffs1"])
        poly2 = Polynomial(data["coeffs2"])
        actual = poly1 - poly2
        if not actual.coeffs in data["combined"]:
            globals()["ERROR"] = True
            err(
                "Error in %s. Expected %s but got %s. Run on input: p1=%s p2=%s" % (
                    "test_polynomial:test_sub", str(data["combined"]), str(actual.coeffs), str(data["coeffs1"]),
                    str(data["coeffs2"])))

    out("Test mul polynomials...")
    expected = [
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [1, 2, 3],
            'combined': [[1, 4, 10, 12, 9]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [0],
            'combined': [[0]],
        },
        {
            'coeffs1': [0],
            'coeffs2': [1, 2, 3],
            'combined': [[0]],
        },
        {
            'coeffs1': [0],
            'coeffs2': [0],
            'combined': [[0]],
        },
        {
            'coeffs1': [1, 2, 3, 4, 5],
            'coeffs2': [1, 2, 3],
            'combined': [[1, 4, 10, 16, 22, 22, 15]],
        },
        {
            'coeffs1': [7.5, 7.5, 7.5, 0, 7],
            'coeffs2': [0.5, 1.5, 2, 0, 3],
            'combined': [[3.75, 15, 30, 26.25, 41, 33, 36.5, 0, 21]],
        },
        {
            'coeffs1': [0, 0, 0, 0, 0, 1],
            'coeffs2': [1],
            'combined': [[0, 0, 0, 0, 0, 1]],
        },
        {
            'coeffs1': [1, 2, 3],
            'coeffs2': [-1, -2, -3],
            'combined': [[-1, -4, -10, -12, -9]],
        },
        {
            'coeffs1': [3, 1, 4],
            'coeffs2': [3, 2, -4],
            'combined': [[9, 9, 2, 4, -16]],
        },
        {
            'coeffs1': [3, 3, 3, 3],
            'coeffs2': [-3, 3, -3, -3],
            'combined': [[-9, 0, -9, -18, -9, -18, -9]],
        },
        {
            'coeffs1': [3, 3, 3, 3],
            'coeffs2': [0, -1],
            'combined': [[0, -3, -3, -3, -3]],
        },
        {
            'coeffs1': [1, 0, 1],
            'coeffs2': [0, 0, 1],
            'combined': [[0, 0, 1, 0, 1]],
        },
    ]

    for data in expected:
        poly1 = Polynomial(data["coeffs1"])
        poly2 = Polynomial(data["coeffs2"])
        actual = poly1 * poly2
        if not actual.coeffs in data["combined"]:
            globals()["ERROR"] = True
            err(
                "Error in %s. Expected %s but got %s. Run on input: p1=%s p2=%s" % (
                    "test_polynomial:test_mul", str(data["combined"]), str(actual.coeffs), str(data["coeffs1"]),
                    str(data["coeffs2"])))


def test_find_root(loops=16):
    expected = [
        {
            "func": [-3, 1],
            "EPS": 10 ** (-4),
            "expected": [3]
        },
        {
            "func": [-16, 0, 1],
            "EPS": 10 ** (-4),
            "expected": [4, -4]
        },
        {
            "func": [5, 0, 1],
            "EPS": 10 ** (-4),
            "expected": [None]
        },
        {
            "func": [0, 0, 1],
            "EPS": 10 ** (-4),
            "expected": [0]
        },
        {
            "func": [-36, 0, 1],
            "EPS": 10 ** (-4),
            "expected": [6, -6]
        },
    ]

    for data in expected:
        p = Polynomial(data["func"])
        result = p.find_root()
        passed = False

        for root in data["expected"]:
            if result is None or root is None:
                passed = passed or (root is None and result is None)
            else:
                passed = passed or (root - data["EPS"] < result < root + data["EPS"])

        if not passed:
            err("Error in %s.\n Expected: %s | Actual: %s | EPS: %f"
                % ("find_root", str(data["expected"]), str(result), data["EPS"]))


def test_tree(loops=16):
    trees = [
        {
            "root": (2, 5),
            "nodes": [(4, 3), (1, 7), (3, 8)],
            "weight": 16,
            "heavy_path": [2, 4, 3],
            "closest_key": {
                "num": 4.1,
                "key": [4],
            },
        },
        {
            "root": (2, 1),
            "nodes": [(1, 3), (3, 4), (4, -2)],
            "weight": 4,
            "heavy_path": [2, 1],
            "closest_key": {
                "num": 2,
                "key": [2],
            },
        },
        {
            "root": (3, 2),
            "nodes": [(2, 5), (1, -3), (5, 4), (4, 0), (6, -2)],
            "weight": 6,
            "heavy_path": [3, 5, 4],
            "closest_key": {
                "num": -100,
                "key": [1],
            },
        },
        {
            "root": (6, -2),
            "nodes": [(3, 7), (1, -3), (4, 0), (5, -1), (7, 5)],
            "weight": 4,
            "heavy_path": [6, 3, 4, 5],
            "closest_key": {
                "num": 0,
                "key": [1],
            },
        },
        {
            "root": (4, -2),
            "nodes": [(2, -2), (6, -5), (3, -2), (7, -1)],
            "weight": -6,
            "heavy_path": [4, 2, 3],
            "closest_key": {
                "num": 6,
                "key": [6],
            },
        },
        {
            "root": (2, -1),
            "nodes": [(1, 1), (3, 2), (4, 0), (5, 0)],
            "weight": 1,
            "heavy_path": [2, 3, 4, 5],
            "closest_key": {
                "num": 0.5,
                "key": [1],
            },
        },
        {
            "root": (1, 1),
            "nodes": [(2, 2), (3, 3), (4, 4), (5, 5)],
            "weight": 15,
            "heavy_path": [1, 2, 3, 4, 5],
            "closest_key": {
                "num": 1.5,
                "key": [1, 2],
            },
        },
        {
            "root": (-8, 1),
            "nodes": [(-2, 6), (0, 3), (-88, 13), (12, 5)],
            "weight": 15,
            "heavy_path": [-8, -2, 0, 12],
            "closest_key": {
                "num": 10,
                "key": [12],
            },
        },
        {
            "root": (42, 5),
            "nodes": [(52, 8), (32, -1), (36, -6), (30, 0), (50, 1), (56, -7)],
            "weight": 14,
            "heavy_path": [42, 52, 50],
            "closest_key": {
                "num": 0.1,
                "key": [30],
            },
        },
    ]

    for tree in trees:
        t = None
        t = insert(t, tree["root"][0], tree["root"][1])
        for node in tree["nodes"]:
            insert(t, node[0], node[1])

        actual = weight(t)

        if not actual == tree["weight"]:
            globals()["ERROR"] = True
            err("Error in test_%s: Expected: %s but got: %s. Run on input: %s"
                % (str("tree\weight"), str(tree["weight"]), str(actual), str([tree["root"]] + tree["nodes"])))

        actual = heavy_path(t)

        if not actual == tree["heavy_path"]:
            globals()["ERROR"] = True
            err("Error in test_%s: Expected: %s but got: %s. Run on input: %s"
                % (str("tree\heavy_path"), str(tree["heavy_path"]), str(actual), str([tree["root"]] + tree["nodes"])))

        actual = find_closest_key(t, tree["closest_key"]["num"])

        if actual not in tree["closest_key"]["key"]:
            globals()["ERROR"] = True
            err("Error in test_%s: Expected one of: %s but got: %s. Run on input: %s"
                % (str("tree\closest_key"), str(tree["closest_key"]["key"]), str(actual), str([tree["root"]] + tree["nodes"])))


def count_words_naive(words):
    count_list = SimpleDict(200)
    words_set = set(words)
    for word in words_set:
        count_list.insert(word, words.count(word))
    return count_list


def download(url):
    ''' url should be a string containing the full path, incl. http://  '''
    f = urlopen(url)
    btext = f.read()
    text = btext.decode('utf-8')
    # read from the object, storing the page's contents in text.
    f.close()
    return text


def clean(text):
    ''' converts text to lower case, then replaces all characters except
       letters, spaces, newline and carriage return by spaces '''
    letter_set = "abcdefghijklmnopqrstuvwxyz \n\r"
    text = str.lower(text)
    cleaned = ""
    for letter in text:
        if letter in letter_set:
            cleaned += letter
        else:
            cleaned += " "
    return cleaned


def test_count_words(loops=16):
    text = download("http://www.veryabc.cn/movie/uploads/script/harrypotterandthegobletoffire.txt")
    txt = clean(text)

    WORDS = txt.split()

    for i in range(loops):
        start = randint(0, len(WORDS) - 128)
        test_words = [WORDS[randint(start, start + 64)] for i in range(0, 16)]
        actual = count_words(test_words)
        expected = count_words_naive(test_words)

        if not sorted(actual.items(), key=lambda x: x[0]) == sorted(expected.items(), key=lambda x: x[0]):
            globals()["ERROR"] = True
            err("Error in test_%s: Expected: %s but got: %s. Run on input: %s"
                % (str("count_words"), str(expected.items()), str(actual.items()), str(test_words)))


def sort_by_count_naive(words):
    copy_of_words = words.items()[:]
    copy_of_words.sort(key=lambda x: -x[1])
    return copy_of_words


def test_sort_by_count(loops=16):
    text = download("http://www.veryabc.cn/movie/uploads/script/harrypotterandthegobletoffire.txt")
    txt = clean(text)

    WORDS = txt.split()

    for i in range(loops):
        start = randint(0, len(WORDS) - 128)
        test_words = [WORDS[randint(start, start + 64)] for i in range(0, 16)]
        counted_words = count_words_naive(test_words)
        actual = sort_by_cnt(counted_words)
        expected = sort_by_count_naive(counted_words)

        if not actual == expected:
            globals()["ERROR"] = True
            err("Error in test_%s: Expected: %s but got: %s. Run on input: %s"
                % (str("sort_by_count"), str(expected), str(actual), str(test_words)))


def test_pascal(loops=16):
    expected = [[1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
                [1, 5, 10, 10, 5, 1],
                [1, 6, 15, 20, 15, 6, 1],
                [1, 7, 21, 35, 35, 21, 7, 1],
                [1, 8, 28, 56, 70, 56, 28, 8, 1],
                [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]

    pascal_gen = generate_pascal()

    for row in expected:
        next_pascal_row = next(pascal_gen)
        if not next_pascal_row == row:
            globals()["ERROR"] = True
            err("Error in test_%s: Expected: %s but got: %s."
                % (str("pascal"), str(row), str(next_pascal_row)))


def test_bernoulli(loops=16):
    expected = [[1],
                [1, 2],
                [1, 3, 4],
                [1, 4, 7, 8],
                [1, 5, 11, 15, 16],
                [1, 6, 16, 26, 31, 32],
                [1, 7, 22, 42, 57, 63, 64],
                [1, 8, 29, 64, 99, 120, 127, 128],
                [1, 9, 37, 93, 163, 219, 247, 255, 256],
                [1, 10, 46, 130, 256, 382, 466, 502, 511, 512]]

    pascal_gen = generate_bernoulli()

    for row in expected:
        next_bernoulli_row = next(pascal_gen)
        if not next_bernoulli_row == row:
            globals()["ERROR"] = True
            err("Error in test_%s: Expected: %s but got: %s."
                % (str("bernoulli"), str(row), str(next_bernoulli_row)))


def test_upside_down(loops=16):
    for k in range(loops):
        n, m = randint(4, 256), randint(4, 256)
        mat = Matrix(n, m)
        expected_mat = Matrix(n, m)

        for i in range(n):
            for j in range(m):
                value = randint(0, 256)
                mat[i, j] = value
                expected_mat[n - i - 1, j] = value

        actual = upside_down(mat)

        if not actual == expected_mat:
            err("Error in test_%s: Expected: %s but got: %s."
                % (str("upside_down"), str(expected_mat), str(actual)))


def out(message):
    print(">> " + message)


def err(message):
    out("!!!")
    out("!!! " + message + " !!!")
    out("!!!")


def run_tests(loops=16):
    out("Running given tests...")
    test()
    out("Done.")

    out("")

    out("Running awesome random tests...")
    out("Test polynomial...")
    test_polynomial(loops)
    out("Test find root...")
    test_find_root(loops)
    out("Test tree...")
    test_tree(loops)

    try:
        out("Test count words...")
        test_count_words(loops)

        out("...")
        out("It can take a while... But it's totally worth it (^‿^)")
        out("...")

        out("Test sort by count...")
        test_sort_by_count(loops)
    except Exception:
        err("You must have wifi connected in order to test count_words and sort_by_count.")
        err("Please check your internet connection and then try again.")

    out("...")

    out("Test pascal...")
    test_pascal(loops)

    out("Test bernoulli...")
    test_bernoulli(loops)

    out("Test upside down...")
    test_upside_down(loops)

    err("Sorry, no test for Q5b (~_~)")
    out("Done.")
    out("")

    if globals()["ERROR"]:
        err("Sorry, but you have a few errors (￣m￣)")
    else:
        out("If no errors showed up, all tests passed ＼(^o^)／")


run_tests()
