
import logging

class FirstClass:
    def __init__(self):
        self.current_number = 0
        self.logger = logging.getLogger(__name__)

    def increment_number(self):
        self.current_number += 1
        self.logger.warning('увеличиваем на 1')

    def decrement_number(self):
        self.current_number -= 1
        self.logger.warning('уменьшаем на 1')

    def clear_number(self):
        self.current_number = 0
        self.logger.warning('обнуляем счетчик')


