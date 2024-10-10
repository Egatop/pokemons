import telebot 
from config import token
from random import randint
from logic import Pokemon, Wizard, Fighter, Ordinary

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,6)
        if chance == 1 or chance == 4 or chance == 5:
            pokemon = Ordinary(message.from_user.username)
            bot.send_message(message.chat.id, f'Имя твоего покемона:{pokemon.get_name()} здоровье:{Pokemon.pokemons[message.from_user.username].info()[1][3]}, сила:{Pokemon.pokemons[message.from_user.username].info()[1][4]} \n Класс: ordinary')
            bot.send_message(message.chat.id, 'Фото твоего Покемона')
            bot.send_photo(message.chat.id, pokemon.show_img())
            bot.send_message(message.chat.id, 'Крик твоего покемона!')
            bot.send_document(message.chat.id, Pokemon.pokemons[message.from_user.username].info()[1][2])
        elif chance == 2:
            pokemon = Fighter(message.from_user.username)
            bot.send_message(message.chat.id, f'Имя твоего покемона:{pokemon.get_name()} здоровье:{Pokemon.pokemons[message.from_user.username].info()[1][3]}, сила:{Pokemon.pokemons[message.from_user.username].info()[1][4]} \n Класс: Fighter')
            bot.send_message(message.chat.id, 'Фото твоего Покемона')
            bot.send_photo(message.chat.id, pokemon.show_img())
            bot.send_message(message.chat.id, 'Крик твоего покемона!')
            bot.send_document(message.chat.id, Pokemon.pokemons[message.from_user.username].info()[1][2])
        elif chance == 3 or chance == 6:
            pokemon = Wizard(message.from_user.username)
            bot.send_message(message.chat.id, f'Имя твоего покемона:{pokemon.get_name()} здоровье:{Pokemon.pokemons[message.from_user.username].info()[1][3]}, сила:{Pokemon.pokemons[message.from_user.username].info()[1][4]} \n Класс: Wizard')
            bot.send_message(message.chat.id, 'Фото твоего Покемона')
            bot.send_photo(message.chat.id, pokemon.show_img())
            bot.send_message(message.chat.id, 'Крик твоего покемона!')
            bot.send_document(message.chat.id, Pokemon.pokemons[message.from_user.username].info()[1][2])
        
        

    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username  in Pokemon.pokemons.keys():
         bot.send_message(message.chat.id, f'{Pokemon.pokemons[message.from_user.username].info()[1][0]} здоровье:{Pokemon.pokemons[message.from_user.username].info()[1][3]}, сила:{Pokemon.pokemons[message.from_user.username].info()[1][4]}')
         bot.send_message(message.chat.id, f'{Pokemon.pokemons[message.from_user.username].info()[0]}')
         bot.send_message(message.chat.id, 'Фото твоего Покемона')
         bot.send_photo(message.chat.id, Pokemon.pokemons[message.from_user.username].info()[1][1])
         bot.send_message(message.chat.id, 'Крик твоего покемона!')
         bot.send_document(message.chat.id, Pokemon.pokemons[message.from_user.username].info()[1][2])
      
    else:
        bot.reply_to(message, "Ты еще не создал своего покемона")

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            id = message.reply_to_message.from_user.username
            res = pok.attack(enemy,id)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")



bot.infinity_polling(none_stop=True)

