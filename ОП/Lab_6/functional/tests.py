import pytest
import sys
import functional.qsort as qs

def test_quicks_int_input():
    assert qs.quicks([51, 26, 478, 5, ]) == [5, 26, 51, 478]
    assert qs.quicks([56, 415, 54, 33, ]) == [33, 54, 56, 415]


def test_quicks_float_input():
    assert qs.quicks([54.52, 54.65, 12.56]) == [12.56, 54.52, 54.65]
    assert qs.quicks([65.21, 89.54, 21.63]) == [21.63, 65.21, 89.54]


def test_quicks_negatives():
    assert qs.quicks([-14, -35, -650]) == [-650, -35, -14]
    assert qs.quicks([-46, -64, -7]) == [-64, -46   , -7]


def test_quicks_error_string():
    assert qs.quicks(['like', 'I', 'trains']) == ['I', 'like', 'trains']


def test_quicks_mixed():
    assert qs.quicks([-35, 64, 13.67, 31, -76]) == [-76, -35, 13.67, 31, 64]


def test_quicks_sing_num():
    assert qs.quicks([17]) == [17]


def test_quicks_empty():
    assert qs.quicks([]) == []


def test_checki_ints():
    assert qs.checkitem([13, 66, 31, 67]) == [13, 66, 31, 67]
    assert qs.checkitem(['13', 64, 35, '90', '09']) == [13, 64, 35, 90, 9]


def test_checki_floats():
    assert qs.checkitem([52.65, 75.1, '.64', '.9']) == [52.65, 75.1, 0.64, 0.9]


def test_checki_error_str():
    assert not qs.checkitem(['KEKS'])
    assert not qs.checkitem([''])


def test_checki_negatives():
    assert qs.checkitem([-1, '-1', '-10000']) == [-1, -1, -10000]


def test_checki_mix():
    assert qs.checkitem([.4, '0.8', 6, -51, '-10000']) == [0.4, 0.8, 6, -51, -10000]
