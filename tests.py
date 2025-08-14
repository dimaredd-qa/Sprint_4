import pytest

from conftest import favorite_one_book
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, bookscollector):
        bookscollector.add_new_book('Гордость и предубеждение и зомби')
        bookscollector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(bookscollector.get_books_genre()) == 2


    @pytest.mark.parametrize('name',[
        'Заводной апельсин: Избранные страницы!!!!',    #41 символов
        'Мастер и Маргарита: эпилог вечной любви!!!',   #42 символов
        'Война и мир: эпическое полотно Льва Толстого в четырёх томах'  #60 символов
    ])
    def test_add_new_book_when_name_book_more40_symbol_false(self, bookscollector, name):
        bookscollector.add_new_book(name)
        assert len(bookscollector.get_books_genre()) == 0


    @pytest.mark.parametrize('name', [
        'Гарри Поттер и Философский Камень: Дюна',  #39 символов
        'Гарри Поттер и Философский Камень: Лис',   #38 символов
        'Три товарища: роман о дружбе и потерях!!',  # 40 символов
        'Гарри Поттер и Всё',    #18 символов
        'A' #1 символ
    ])
    def test_add_new_book_when_name_book_max40_symbol_true(self, bookscollector, name):
        bookscollector.add_new_book(name)
        assert name in bookscollector.get_books_genre()


    def test_add_new_book_when_readding_name_book_false(self, only_one_book):
        repeat_name = 'Физика'
        only_one_book.add_new_book(repeat_name)
        assert len(only_one_book.get_books_genre()) == 1


    def test_add_new_book_when_name_null_false(self, bookscollector):
        name = ''
        bookscollector.add_new_book(name)
        assert len(bookscollector.get_books_genre()) == 0


    def test_set_book_genre_valid_true(self, bookscollector):
        bookscollector.add_new_book("Алгебра")
        bookscollector.set_book_genre("Алгебра", "Фантастика")
        assert bookscollector.get_book_genre("Алгебра") == "Фантастика"


    def test_set_book_genre_when_not_exist_genre_false(self,bookscollector):
        bookscollector.add_new_book("Химия")
        bookscollector.set_book_genre("Химия", "Триллер")
        assert bookscollector.get_book_genre("Химия") == ""


    def test_set_book_genre_when_not_exist_book_false(self, bookscollector):
        bookscollector.set_book_genre('Физика', 'Ужасы')
        assert len(bookscollector.get_books_genre()) == 0


    def test_get_book_genre_for_existing_book_true(self, collector_three_books):
        genre = collector_three_books.get_book_genre('Проклятье')
        assert genre == 'Ужасы'


    def test_get_books_with_specific_genre_valid_true(self, collector_three_books):
        books = collector_three_books.get_books_with_specific_genre('Ужасы')
        assert len(books) == 2


    def test_get_books_genre_returns_all_books_true(self, collector_three_books):
        books_genre = collector_three_books.get_books_genre()
        assert len(books_genre) == 3


    def test_get_books_for_children_valid_true(self, collector_three_books):
        children_books = collector_three_books.get_books_for_children()
        assert len(children_books) == 1


    def test_add_book_in_favorites_true(self, favorite_one_book):
        assert favorite_one_book.get_list_of_favorites_books() == ['Бэтмен']


    def test_delete_book_in_favorites_true(self, favorite_one_book):
        favorite_one_book.delete_book_from_favorites('Бэтмен')
        assert favorite_one_book.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books_returns_correct_list(self, favorite_one_book):
        favorite_book = favorite_one_book.get_list_of_favorites_books()
        assert favorite_book == ['Бэтмен']











