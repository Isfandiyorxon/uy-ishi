from telebot.types import ReplyKeyboardMarkup, KeyboardButton
def sport_buton():
    markub=ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    btn1 = KeyboardButton("Boks🥊")
    btn2=KeyboardButton("Kurash🥋")
    btn3=KeyboardButton("Shahmat♟")
    markub.add(btn1,btn2,btn3)
    return markub
def sportchilar_buton(sport:str):
    markub=ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    btn1, btn2 = None, None
    if sport == 'Boks🥊':
        btn1=KeyboardButton('Tayson')
        btn2=KeyboardButton('MuhammadAli')

    elif sport == 'Kurash🥋':
        btn1=KeyboardButton('Artur Taymazov')
        btn2=KeyboardButton('Diyora Keldiyorova')
    elif sport == 'Shahmat♟':
        btn1=KeyboardButton('Wilhelm Steinitz ')
        btn2=KeyboardButton('Johann Zukertor')


    back=KeyboardButton('🔙 orqaga')
    markub.add(btn1,btn2,back)
    return markub