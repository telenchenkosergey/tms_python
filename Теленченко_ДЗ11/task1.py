# Создать класс Публикация, в котором будут содержаться три параметра Заголовок,
# Автор, Год выпуска, а также функция display для вывода этих параметров.
# Также создать двух наследников Публикации: Книга и Журнал.
# В Книге появится новый параметр isbn, а в Журнале - номер выпуска. Не забываем
# о выводе этих параметров через функцию display.
# Также создать общую для всех функцию выводящую имя издательства. Имя должно
# быть полем класса.

class Publication:
    _publisher = 'Penguin Pinky'

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}'
    
    def get_publisher(self):
        return f'Publisher: {self._publisher}'
    

class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        return super().display() + f'\nISBN: {self.isbn}'
    

class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        return super().display() + f'\nISBN: {self.issue_number}'
