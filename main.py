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
# from abc import ABC,abstractmethod
# import json
# class Book(ABC):
#     def __init__(self,title,author,isbn,page_count):
#         self.__title=title
#         self.__author=author
#         self.__isbn=isbn
#         self.__page_count=page_count
#     @abstractmethod
#     def get_info(self):
#         pass
#     @abstractmethod
#     def read_page(self):
#         pass
#     @abstractmethod
#     def bookmark_page(self):
#         pass
#
#     def save_to_json(self, filename):
#         data = {
#             'title': self.title,
#             'author': self.author,
#             'isbn': self.isbn,
#             'page_count': self.page
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#         return f"Ma'lumotlar {filename} ga yozildi"
#     @property
#     def title(self):
#         return self.__title
#     @title.setter
#     def title(self,new):
#         self.__title=new
#     @title.deleter
#     def title(self):
#         del self.__title
#
#     @property
#     def author(self):
#         return self.__author
#
#     @author.setter
#     def author(self,new):
#         self.__author=new
#     @author.deleter
#     def author(self):
#         del self.__author
#
#     @property
#     def isbn(self):
#         return self.__isbn
#
#     @isbn.setter
#     def isbn(self,new):
#         self.isbn=new
#
#     @isbn.deleter
#     def isbn(self):
#         del self.__isbn
#
#     @property
#     def page(self):
#         return self.__page_count
#     @page.setter
#     def page(self,new):
#         self.page=new
#
# class Ebook(Book):
#     def __init__(self,title,author,isbn,page_count,duration):
#         super().__init__(title,author,isbn,page_count)
#         self.duration=duration
#
#     def get_info(self):
#         return f" kitob malumotlari kitob nomi :{self.title}, kitob muallifi{self.author} kitob varoqlar soni: {self.page} kitob isbn {self.isbn}"
#
#     def read_page(self,num):
#         return f"siz shuncha {num} o'qidiz"
#
#     def bookmark_page(self,num):
#         return f"{num+26} bet qodi"
#
#
# class AudioBook(Book):
#     def __init__(self, title, author, isbn, page_count, duration):
#         super().__init__(title, author, isbn, page_count)
#         self.duration = duration
#
#     def get_info(self):
#         return f"Kitob nomi: {self.title}, Muallifi: {self.author}, ISBN: {self.isbn}, Sahifa soni: {self.page}, Davomiyligi: {self.duration} soat"
#
#     def read_page(self, num):
#         return f"Siz {num}-sahifani o'qidiz"
#
#     def bookmark_page(self, num):
#         return f"{num + 1}-sahifaga belgi qo'yildi"
#
#     def play(self):
#         return f"{self.title} kitobi o'ynatilyapti, davomiyligi {self.duration} soat"
#
#     def save_to_json(self, filename):
#         data = {
#             'title': self.title,
#             'author': self.author,
#             'isbn': self.isbn,
#             'page_count': self.page,
#             'duration': self.duration
#         }
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=4)
#         return f"Ma'lumotlar {filename} ga yozildi"
# ebook = Ebook("Python O'rganish", "Isfandiyor", "1234567890", 350, 5)
# audiobook = AudioBook("Python Pro", "Isfandiyor", "0987654321", 450, 10)
#
# print(ebook.get_info())
# print(audiobook.get_info())
#
# ebook.save_to_json("ebook_data.json")
# audiobook.save_to_json("audiobook_data.json")

from telebot import TeleBot
from telebot.types import Message
from buttns import sportchilar_buton,sport_buton

bot=TeleBot('7775694509:AAEz4s1ZBwi8xWwQZ8fdYE7vEH7OAIwTRG8')
sportchilar={'Tayson':{'photo':'https://assets.gq.ru/photos/60d19758b7d84cdfa6d01788/16:9/w_2560%2Cc_limit/GettyImages-51763505.jpeg',
                         'ismi':'Tayson',
                         'tug\'ilgan sanasi':"1966 yil"
                 },
'MuhammadAli':{'photo':'https://cdn.britannica.com/86/192386-050-D7F3126D/Muhammad-Ali-American.jpg',
                         'ismi':'MuhammadAli',
                         'tug\'ilgan sanasi':'1942 yil',
                 },
'Artur Taymazov':{'photo':'https://storage.kun.uz/source/thumbnails/_medium/3/BmTE2o589GBQSB1_Yj9D2TmWDMEpeQ3E_medium.jpg',
                         'ismi':'Artur Taymazov',
                         'tug\'ilgan sanasi':'1979 yil',
                 },
'Diyora Keldiyorova':{'photo':'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Diyora_Keldiyorova_at_the_2024_Summer_Olympics_02.jpg/1200px-Diyora_Keldiyorova_at_the_2024_Summer_Olympics_02.jpg',
                         'ismi':'Diyora Keldiyorova',
                         'tug\'ilgan sanasi':'1998 yil',
                 },
'Wilhelm Steinitz':{'photo':'https://upload.wikimedia.org/wikipedia/commons/3/37/Wilhelm_Steinitz.jpg',
                         'ismi':'Wilhelm Steinitz',
                         'tug\'ilgan sanasi':'1836 yil',
                 },
'Johann Zukertor':{'photo':'https://upload.wikimedia.org/wikipedia/commons/c/c3/Johannes_Zukertort.jpg',
                         'ismi':'Johann Zukertor',
                         'tug\'ilgan sanasi':'1842 yil',
                 }
       }
@bot.message_handler(commands=['start'])
def reaction_to_start(message:Message):
    chat_id=message.chat.id
    bot.send_message(chat_id,f"Assalomy alaykum {message.from_user.full_name}")
    @bot.message_handler(regexp='sprot')
    def reation_text(message:Message):
        chat_id=message.chat.id
        bot.send_message(chat_id,"Sport turlari",reply_markup=sport_buton())

    @bot.message_handler(regexp='Boks🥊')
    def freaction_to_text(message: Message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Sporchilar", reply_markup=sport_buton(message.text))

    @bot.message_handler(regexp='Kurash🥋')
    def freaction_to_text(message: Message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Sporchilar", reply_markup=sport_buton(message.text))

    @bot.message_handler(regexp='Shahmat♟')
    def freaction_to_text(message: Message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Sporchilar", reply_markup=sport_buton(message.text))


def worker(message: Message):
    chat_id = message.chat.id
    photo = sportchilar[message.text]['photo']
    nomi = sportchilar[message.text]['ismi']
    muallifi = sportchilar[message.text]['tug\'ilgan sanas']


    caption = f" *Ismi*: {nomi}\n *Tug'ilgan sanasi*: {muallifi}\n"
    bot.send_photo(chat_id, photo, caption=caption, parse_mode='Markdown', has_spoiler=True)

@bot.message_handler(func=lambda message:message.text =='Johann Zukertor')
def reaction_to_ozb(message:Message):
    worker(message)
@bot.message_handler(func=lambda message:message.text =='Wilhelm Steinitz')
def reaction_to_ozb(message:Message):
    worker(message)
@bot.message_handler(func=lambda message:message.text =='Diyora Keldiyorova')
def reaction_to_ozb(message:Message):
    worker(message)
@bot.message_handler(func=lambda message:message.text =='Artur Taymazov')
def reaction_to_ozb(message:Message):
    worker(message)

@bot.message_handler(func=lambda message:message.text =='Tayson')
def reaction_to_ozb(message:Message):
    worker(message)
@bot.message_handler(func=lambda message:message.text =='MuhammadAli')
def reaction_to_ozb(message:Message):
    worker(message)

@bot.message_handler(regexp='🔙 orqaga')
def reation_to_bec(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Sport", reply_markup=sport_buton())



if __name__ == '__main__':
    bot.polling()
