import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture(scope='class')
    def list_books(self):
        list_books = BooksCollector()
        list_books.add_new_book(name='Бойцовский клуб')
        list_books.set_book_genre(name='Бойцовский клуб', genre='Ужасы')
        list_books.add_new_book(name='Вождь краснокожих')
        list_books.set_book_genre(name='Вождь краснокожих', genre='Комедии')
        list_books.add_new_book(name='Гарри Поттер')
        list_books.set_book_genre(name='Гарри Поттер', genre='Фантастика')
        return list_books

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_duplication(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book, genre',
                             [
                                 ['The Great Gatsby', 'Фантастика'],
                                 ['Wuthering Heights', 'Детективы'],
                                 ['The Handmaid\'s', 'Ужасы'],
                                 ['Things Fall Apart', 'Комедии'],
                                 ['1984', 'Ужасы'],
                                 ['Beloved', 'Мультфильмы'],
                                 ['The Catcher in the Rye', 'Детективы']
                             ])
    def test_set_book_genre_valid_genre(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_book_genre_returns_correct_genre(self, list_books):
        assert list_books.get_book_genre('Бойцовский клуб') == 'Ужасы'

    def test_get_books_with_specific_genre_search_books_by_genre(self, list_books):
        assert list_books.get_books_with_specific_genre('Комедии') == ['Вождь краснокожих']

    def test_get_books_genre_dict_of_books(self, list_books):
        assert list_books.get_books_genre() == {'Бойцовский клуб': 'Ужасы',
                                                'Вождь краснокожих': 'Комедии',
                                                'Гарри Поттер': 'Фантастика'}

    def test_get_books_for_children(self, list_books):
        assert list_books.get_books_for_children() == ['Вождь краснокожих', 'Гарри Поттер']

    def test_add_book_in_favorites_add_two_books(self, list_books):
        list_books.add_book_in_favorites('Гарри Поттер')
        list_books.add_book_in_favorites('Бойцовский клуб')

        assert len(list_books.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_one_book(self, list_books):
        list_books.delete_book_from_favorites('Бойцовский клуб')

        assert len(list_books.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_return_list(self, list_books):
        assert list_books.get_list_of_favorites_books() == ['Гарри Поттер']
