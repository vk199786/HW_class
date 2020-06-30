# coding=utf-8
class Animals:

    def __init__(self, type, name, weight, voice):
        self.type = type
        self.name = name
        self.weight = weight
        self.voice = voice

    def make_voice(self):
        print(f'{self.type} издал {self.voice}!')

    def feed_animals(self):
        print(f'Покормлен: {self.type}')


class Birds(Animals):


    def __init__(self, type, name, weight, voice):
        super(Birds, self).__init__(type, name, weight, voice)

    def pick_up_eggs(self):
        print(f'Собраны яйца у {self.type} - {self.name}')


bird_type_1 = Birds('Гусь', 'Серый', 1.5, 'Га-га')
bird_type_2 = Birds('Гусь', 'Белый', 1.65, 'Вонючие галлы лезут на нашу стену!')
bird_type_3 = Birds('Курица', 'Ко-Ко', 1, 'Ко-ко')
bird_type_4 = Birds('Курица', 'Кукареку', 1.15, 'Ко-ко')
bird_type_5 = Birds('Утка', 'Кряква', 1.85, 'Кря-кря')


class Milk_Animals(Animals):

    def __init__(self, type, name, weight, voice):
        super(Milk_Animals, self).__init__(type, name, weight, voice)

    def get_milk(self):
        print(f'Собрано молоко у {self.type} - {self.name}')


milk_animals_type_1 = Milk_Animals('Корова', 'Манька', 850, 'Муу-Муу')
milk_animals_type_2 = Milk_Animals('Коза', 'Рога', 140, 'Бе-Бе')
milk_animals_type_3 = Milk_Animals('Коза', 'Копыта', 155, 'Бе-Бе')


class Wool_Animals(Animals):
    def __init__(self, type, name, weight, voice):
        super(Wool_Animals, self).__init__(type, name, weight, voice)

    def get_wool(self):
        print(f'Собрана шерсть у {self.type} - {self.name}')


wool_animals_type_1 = Wool_Animals('Овца', 'Барашек', 160, 'Мее-Мее')
wool_animals_type_2 = Wool_Animals('Овца', 'Кудрявый', 100, 'Мее-Мее')

print(bird_type_1.name)
print(bird_type_1.pick_up_eggs())
print(bird_type_1.make_voice())
print(bird_type_1.feed_animals())
print(milk_animals_type_1.get_milk())
print(wool_animals_type_1.get_wool())

#overall_weight_birds = bird_type_1.weight + bird_type_2.weight + bird_type_3.weight + bird_type_4.weight
#overall_weight_milk = milk_animals_type_1.weight + milk_animals_type_2.weight + milk_animals_type_3.weight
#overall_weight_wool = wool_animals_type_1.weight + wool_animals_type_1.weight
#overall_weight = overall_weight_birds + overall_weight_milk + overall_weight_wool
#print(f'Общий вес животных: {overall_weight} кг')

overall_weight_dict = {}
overall_weight_dict[bird_type_1.name] = bird_type_1.weight
overall_weight_dict[bird_type_2.name] = bird_type_2.weight
overall_weight_dict[bird_type_3.name] = bird_type_3.weight
overall_weight_dict[bird_type_4.name] = bird_type_4.weight
overall_weight_dict[milk_animals_type_1.name] = milk_animals_type_1.weight
overall_weight_dict[milk_animals_type_2.name] = milk_animals_type_2.weight
overall_weight_dict[milk_animals_type_3.name] = milk_animals_type_3.weight
overall_weight_dict[milk_animals_type_3.name] = milk_animals_type_3.weight
overall_weight_dict[wool_animals_type_1.name] = wool_animals_type_1.weight
overall_weight_dict[wool_animals_type_2.name] = wool_animals_type_2.weight
print(overall_weight_dict)

total_weight = 0
for animal_name, animal_weight in overall_weight_dict.items():
    total_weight = total_weight + animal_weight
print(f'Общий вес животных: {total_weight} кг')

count = 0
id = 0
for animal_name, animal_weight in overall_weight_dict.items():
    if count < animal_weight:
        count = animal_weight
        id = animal_name
print(f'Максимальный вес у {id}: {count} кг')

#print(max(overall_weight_dict, key=overall_weight_dict.get))


