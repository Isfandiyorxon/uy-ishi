#1-misol
# from abc import ABC, abstractmethod
# import json
#
# class Vehicle(ABC):
#
#     def __init__(self, brend, model, year, mileage):
#         self.__brend = brend
#         self.__model = model
#         self.__year = year
#         self.__mileage = mileage
#     @property
#     def brend(self):
#         return self.__brend
#     @brend.setter
#     def brend(self,new):
#         self.__brend=new
#     @brend.deleter
#     def brend(self):
#         del  self.__brend
#
#     @property
#     def model(self):
#         return self.__model
#     @model.setter
#     def model(self, new):
#         self.__model = new
#     @model.deleter
#     def model(self):
#         del self.__model
#
#     @property
#     def year(self):
#         return self.__year
#     @year.setter
#     def year(self,new):
#         self.__year=new
#     @year.deleter
#     def year(self):
#         del self.__year
#
#     @property
#     def mileage(self):
#         return self.__mileage
#     @mileage.setter
#     def mileage(self,new):
#         self.__mileage=new
#     @mileage.deleter
#     def mileage(self):
#         del self.__mileage
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self,brend, model, year, mileage,num_doors):
#         super().__init__(brend, model, year, mileage)
#         self.num_doors = num_doors
#
#     def signalchalish(self):
#         return f" bib bib"
#
#     def start(self):
#         return f" mashina yurdi"
#     def stop(self):
#         return f"mashina to'xtadi"
#
#     def save_to_json(self, filename):
#         data = {
#             'brend': self.brend,
#             'model': self.model,
#             'year': self.year,
#             'mileage': self.mileage,
#             'num_doors': self.num_doors
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#         return f"Ma'lumotlar {filename} ga yozildi"
#
#
# class Bicycle(Vehicle):
#     def __init__(self,brend, model, year, mileage,gear_count):
#         super().__init__(brend, model, year, mileage)
#         self.gear_count = gear_count
#
#     def start(self):
#         return f"mototsikl yurdi"
#     def stop(self):
#         return  f"mototsikl to'xtadi"
#
#     def signalchalish(self):
#         return  f"fib fib"
#
#     def save_to_json(self, filename):
#         data = {
#             'brend': self.brend,
#             'model': self.model,
#             'year': self.year,
#             'mileage': self.mileage,
#             'gear_count': self.gear_count
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#         return f"Ma'lumotlar {filename} ga yozildi"
#
#
#
# bike=Bicycle("Yamaha", "MT-07", 2021, 15000, 6)
# bike.save_to_json("motolar.json")
# car=Car("BMW","F90",2022,1565,4)
# car.save_to_json("moshinalar.json")

#2-misol
from abc import ABC,abstractmethod
import json
class Book(ABC):
    def __init__(self,title,author,isbn,page_count):
        self.__title=title
        self.__author=author
        self.__isbn=isbn
        self.__page_count=page_count
    @abstractmethod
    def get_info(self):
        pass
    @abstractmethod
    def read_page(self):
        pass
    @abstractmethod
    def bookmark_page(self):
        pass

    def save_to_json(self, filename):
        data = {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'page_count': self.page
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return f"Ma'lumotlar {filename} ga yozildi"
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,new):
        self.__title=new
    @title.deleter
    def title(self):
        del self.__title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self,new):
        self.__author=new
    @author.deleter
    def author(self):
        del self.__author

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self,new):
        self.isbn=new

    @isbn.deleter
    def isbn(self):
        del self.__isbn

    @property
    def page(self):
        return self.__page_count
    @page.setter
    def page(self,new):
        self.page=new

class Ebook(Book):
    def __init__(self,title,author,isbn,page_count,duration):
        super().__init__(title,author,isbn,page_count)
        self.duration=duration

    def get_info(self):
        return f" kitob malumotlari kitob nomi :{self.title}, kitob muallifi{self.author} kitob varoqlar soni: {self.page} kitob isbn {self.isbn}"

    def read_page(self,num):
        return f"siz shuncha {num} o'qidiz"

    def bookmark_page(self,num):
        return f"{num+26} bet qodi"

    
class AudioBook(Book):
    def __init__(self, title, author, isbn, page_count, duration):
        super().__init__(title, author, isbn, page_count)
        self.duration = duration

    def get_info(self):
        return f"Kitob nomi: {self.title}, Muallifi: {self.author}, ISBN: {self.isbn}, Sahifa soni: {self.page}, Davomiyligi: {self.duration} soat"

    def read_page(self, num):
        return f"Siz {num}-sahifani o'qidiz"

    def bookmark_page(self, num):
        return f"{num + 1}-sahifaga belgi qo'yildi"

    def play(self):
        return f"{self.title} kitobi o'ynatilyapti, davomiyligi {self.duration} soat"

    def save_to_json(self, filename):
        data = {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'page_count': self.page,
            'duration': self.duration
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return f"Ma'lumotlar {filename} ga yozildi"
ebook = Ebook("Python O'rganish", "Isfandiyor", "1234567890", 350, 5)
audiobook = AudioBook("Python Pro", "Isfandiyor", "0987654321", 450, 10)

print(ebook.get_info())
print(audiobook.get_info())

ebook.save_to_json("ebook_data.json")
audiobook.save_to_json("audiobook_data.json")
