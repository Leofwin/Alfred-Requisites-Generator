from random import randint
import uuid

INN_UL_LENGTH = 10
INN_FL_LENGTH = 12
KPP_LENGTH = 9
OGRN_LENGTH = 13
OGRNIP_LENGTH = 15
SNILS_LENGTH = 11

INN_UL_CONTROL = (2, 4, 10, 3, 5, 9, 4, 6, 8)
INN_FL_CONTROL = (
    (7, 2, 4, 10, 3, 5, 9, 4, 6, 8),
    (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8),
)

def _get_random_digits(count):
    return [randint(0, 9) for _ in range(count)]

def _make_int(digits):
    return int("".join(map(str, digits)))

def _get_random_from_aplhabet(alphabet, count):
    return [alphabet[randint(0, len(alphabet) - 1)] for _ in range(count)]

def get_random_inn_ul():
    values = _get_random_digits(INN_UL_LENGTH - 1)
    check_sum = (sum([a * b for a, b in zip(values, INN_UL_CONTROL)]) % 11) % 10
    values += [check_sum]
    return "".join(map(str, values))
    
def get_raddom_inn_fl():
    values = _get_random_digits(INN_FL_LENGTH - 2)
    check_sum_1 = (sum([a * b for a, b in zip(values, INN_FL_CONTROL[0])]) % 11) % 10
    values += [check_sum_1]
    check_sum_2 = (sum([a * b for a, b in zip(values, INN_FL_CONTROL[1])]) % 11) % 10
    values += [check_sum_2]
    return "".join(map(str, values))

def get_random_kpp():
    # simple realization without A-Z letters at 5, 6 position
    return "".join([str(x) for x in _get_random_digits(KPP_LENGTH)])

def get_random_ogrn():
    values = _get_random_digits(OGRN_LENGTH - 1)
    value = _make_int(values)
    check_sum = (value % 11) % 10
    values += [check_sum]
    return "".join(map(str, values))

def get_random_ogrnip():
    values = _get_random_digits(OGRNIP_LENGTH - 1)
    value = _make_int(values)
    check_sum = (value % 13) % 10
    values += [check_sum]
    return "".join(map(str, values))

def get_random_snils():
    values = _get_random_digits(SNILS_LENGTH - 2)
    indexes = list(range(1, len(values) + 1, 1))[::-1]
    check_sum = (sum([a * b for a, b in zip(values, indexes)]) % 101) % 100
    return "".join(map(str, values)) + str(check_sum).zfill(2)

def get_random_guid():
    return uuid.uuid4()
