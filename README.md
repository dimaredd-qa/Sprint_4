#проект содержит автоматизированные тесты для класса `BooksCollector`

Cтруктура проекта:
qa_python/
├── main.py          # Класс BooksCollector
├── tests.py         # Автоматизированные тесты
├── conftest.py      # Фикстуры для тестов
└── README.md        # Документация

Функциональность класса
Основные методы:
add_new_book(name) — добавляет новую книгу.

set_book_genre(name, genre) — устанавливает жанр книги.

get_books_with_specific_genre(genre) — возвращает книги определённого жанра.

get_books_for_children() — возвращает книги, подходящие для детей.

add_book_in_favorites(name) — добавляет книгу в избранное.

delete_book_from_favorites(name) — удаляет книгу из избранного.