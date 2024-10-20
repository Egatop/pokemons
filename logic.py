from random import randint
import requests
from datetime import datetime, timedelta
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
     

        self.img = self.get_img()
        self.name = self.get_name()
        self.sound = self.get_sound()
        self.hp =  randint(550,650)
        self.power =  randint(55,100)
        self.last_feed_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self
        

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']["front_default"])
        else:
            return None
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return None
        

    def get_sound(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['cries']['latest'])
        else:
            return None
    def info(self):
        return f"Имя твоего покеомона: {self.name}",self.img, self.sound, self.hp, self.power
    

    def attack(self, enemy):
        if enemy.hp > self.power:
            if isinstance(enemy, Wizard):
                chance = randint(1,3)
                if chance == 1:
                    return f"Покемон-волшебник применил щит в сражении, урон не засчитан. Оставшееся у @{enemy.pokemon_trainer} hp:{enemy.hp}"
                else:
                    enemy.hp -= self.power
                    return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} \nИгрок @{self.pokemon_trainer} нанёс {self.power} единиц урона по @{enemy.pokemon_trainer} \nОставшееся у @{enemy.pokemon_trainer} hp:{enemy.hp}"
            else:
                enemy.hp -= self.power
                return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer} \nИгрок @{self.pokemon_trainer} нанёс {self.power} единиц урона по @{enemy.pokemon_trainer} \nОставшееся у @{enemy.pokemon_trainer} hp:{enemy.hp}"
        
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! \n@{self.pokemon_trainer} получил прибавку к силе и его здоровье переформированно\nпокемон противника был убит"

        
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def send_sound(self):
        return self.sound
    
     
class Wizard(Pokemon):
    def __init__(self,pokemon_trainer ):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.sound = self.get_sound()
        self.hp =  randint(500,700)
        self.power =  randint(50,90)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self

    def info(self):
        return 'у тебя покемон волшебник', super().info()
    def attack(self, enemy,id):
        result = super().attack(enemy)
        if enemy.hp == 0:
            self.hp =  randint(550,700)
            self.power += 10
            del Pokemon.pokemons[id]
        return result
    def feed(self): 
        result = super().feed(120,30)
        return(result)
 

class Fighter(Pokemon):
    def __init__(self,pokemon_trainer ):
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.sound = self.get_sound()
        self.power=randint(70,120)
        self.hp = randint(400,550)
        self.last_feed_time = datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self

    def info(self):
        return 'у тебя покемон боец',super().info()
    def attack(self, enemy, id):
        super_power = randint(10,25)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        if enemy.hp == 0:
            self.hp =  randint(400,550)
            self.power += 20
            del Pokemon.pokemons[id]
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    def feed(self): 
        result = super().feed(200,40)
        return(result)

    
    
class Ordinary(Pokemon):
     def info(self):
        return 'у тебя обычный покемон',super().info()
     def attack(self, enemy,id):
        result = super().attack(enemy)
        if enemy.hp == 0:
            self.hp =  randint(550,650)
            self.power += 15
            del Pokemon.pokemons[id]
        return result
     def feed(self): 
        result = super().feed(120,25)
        return(result)



