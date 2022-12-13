import doctest
from typing import Union


class Essay:
    """
    Класс описывает объём эссе
    """

    def __init__(self, required_volume: Union[int, float], actual_volume: Union[int, float]):
        """Инициализация экземпляра класса
        :param required_volume: Необходимый объём эссе.
        :param actual_volume: Текущий объём эссе.
        >>> essay = Essay(500, 0)
        """
        if not isinstance(required_volume, (int, float)):
            raise TypeError
        if not required_volume > 0:
            raise ValueError
        self.required_volume = required_volume

        if not isinstance(actual_volume, (int, float)):
            raise TypeError
        if actual_volume < 0:
            raise ValueError
        self.actual_volume = actual_volume

    def is_essay_full(self) -> bool:
        """
            Метод проверяет полное ли эссе
            :return: Является ли эссе полным
            >>> essay = Essay(500, 500)
            """
        ...

    def is_essay_empty(self) -> bool:
        """
            Метод проверяет пустое ли эссе
            :return: Является ли эссе пустым
            >>> essay = Essay(500, 0)
            """
        ...

    def add_words_to_essay(self, words: float) -> None:
        """
            Добавление слов в эссе
            :param words: Количество добавленных слов
            :raise ValueError: Если количество добавляемых слов превышает свободное место в эссе, вызываем ошибку
            >>> essay = Essay(500, 100)
            >>> essay.add_words_to_essay(350)
            """
        if not isinstance(words, (int, float)):
            raise TypeError("Добавляемые слова должны быть типа int или float")
        if words < 0:
            raise ValueError("Добавляемые слова должны быть положительным числом")
        ...


# TODO Написать 3 класса с документацией и аннотацией типов
class Notebook:
    def __init__(self, words_amount: Union[int], name: Union[str]):
        if not isinstance(words_amount, int):
            raise TypeError("Количество слов должно быть тиипа int")
        self.words_amount = words_amount
        if not isinstance(name, str):
            raise TypeError("Название блокнота должно быть типа str")
        self.name = name

    def add_words_to_notebook(self, words: int) -> None:
        """
        Добавление слов в блокнот
        :param words: количество слов
        >>> notebook = Notebook(20, "")
        >>> notebook.add_words_to_notebook(10)
        """
        if not isinstance(words, int):
            raise TypeError("Количество добавляемых слов должно быть типа int")
        if words < 0:
            raise ValueError("Количество добавляемых слов должно быть больше 0")
        ...

    def change_name(self, name: str):
        """
        Переименование блокнота
        :param name: название блокнота
        >>> notebook = Notebook(20,"Блокнот")
        >>> notebook.change_name("Блокнотик")
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
