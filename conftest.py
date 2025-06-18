import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def bookscollector():
    collector = BooksCollector()
    #return collector
    yield collector
    #collector.books_genre.clear()

@pytest.fixture
def only_one_book():
    collector = BooksCollector()
    collector.add_new_book('Физика')
    return collector

@pytest.fixture
def collector_three_books():
    collector = BooksCollector()
    collector.add_new_book('Проклятье')
    collector.add_new_book('Заклятье')
    collector.add_new_book('Варкрафт')
    collector.set_book_genre('Проклятье', 'Ужасы')
    collector.set_book_genre('Заклятье', 'Ужасы')
    collector.set_book_genre('Варкрафт', 'Фантастика')
    return collector

@pytest.fixture
def favorite_one_book():
    collector = BooksCollector()
    collector.add_new_book('Бэтмен')
    collector.add_book_in_favorites('Бэтмен')
    return collector



