# -*- coding: utf-8 -*-
"""Simple application to implements subject described in readme.md

See readme.md :)
"""
import logging
import random
import re

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s\t%(asctime)s\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S%z')


class Main:
    """Main class"""
    DEFAULT_MIN = 1
    DEFAULT_MAX = 100

    def __init__(self, min_value: int = None, max_value: int = None):
        self.number_of_rounds = 0
        self.__min_value = min_value if min_value is not None else Main.DEFAULT_MIN
        self.__max_value = max_value if max_value is not None else Main.DEFAULT_MAX
        if self.__max_value < self.__min_value:
            self.__min_value, self.__max_value = self.__max_value, self.__min_value
        logging.debug('Init min to %s', self.__min_value)
        logging.debug('Init max to %s', self.__max_value)


    def start(self):
        """run the app"""
        to_guess = random.randint(self.__min_value, self.__max_value)
        logging.debug('Number to guess: %s', to_guess)
        logging.debug('Reset number of round')
        self.number_of_rounds = 0

        typed = None
        while True:

            typed = input("Try a number: ")

            self.number_of_rounds += 1
            logging.debug('Turn: %s; Input: %s', self.number_of_rounds, typed)

            if not re.match(r"^[0-9]+$", typed):
                logging.warning('Not an integer !!')
                print('Input "{}" is not a number'.format(typed))
                continue

            typed_int = int(typed)
            if typed_int < to_guess:
                print('Program: +')
                continue

            if to_guess < typed_int:
                print('Program: -')
                continue

            print('Program: You win in {} steps!'.format(self.number_of_rounds))
            break


    def __str__(self):
        return '[{} <-> {}]'.format(self.__min_value, self.__max_value)

    def __eq__(self, other):
        """Overrides the basic EQ implementation

        :param other: (object) The object we want self to be compared with
        :return: (bool) True if it's the same object, False otherwise
        """
        if isinstance(self, other.__class__) is False:
            return False

        return str(self) == str(other)



Main(1, 100).start()
