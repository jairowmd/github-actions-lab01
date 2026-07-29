from calculadora import *


def test_soma():

    assert soma(2,3) == 5


def test_subtracao():

    assert subtracao(10,5) == 5


def test_multiplicacao():

    assert multiplicacao(4,3) == 12


def test_divisao():

    assert divisao(10,2) == 5