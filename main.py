# Initial name ideas were:
# - Game Name: The Battle of Os
# - Creature Name: Anima
#
# Final names:
# - Game Name: World of Os
# - Creature Name: Enima (Elemental Animals, or Elemental Anima)
import random
import sys

animals = ['Rat', 'Ox', 'Tiger', 'Rabbit',
           'Dragon', 'Snake', 'Horse', 'Goat',
           'Monkey', 'Rooster', 'Dog', 'Pig']

elements = {'Fire': {'Destroys': 'Metal', 'Destroyed By': 'Water', 'Strengthens': 'Earth', 'Colour': 'Red'},
            'Metal': {'Destroys': 'Wood', 'Destroyed By': 'Fire', 'Strengthens': 'Water', 'Colour': 'White'},
            'Wood': {'Destroys': 'Earth', 'Destroyed By': 'Metal', 'Strengthens': 'Fire', 'Colour': 'Green'},
            'Earth': {'Destroys': 'Water', 'Destroyed By': 'Wood', 'Strengthens': 'Metal', 'Colour': 'Yellow'},
            'Water': {'Destroys': 'Fire', 'Destroyed By': 'Earth', 'Strengthens': 'Wood', 'Colour': 'Blue'}}

stats = {'Health': {'Min': 200, 'Max': 400},
         'Attack': {'Min': 50, 'Max': 150},
         'Defense': {'Min': 50, 'Max': 150},
         'Speed': {'Min': 50, 'Max': 150}}


class Enima:
    def __init__(self, animal_list, element_list, stats_list):
        self.element = random.choice(list(element_list))
        self.animal = random.choice(animal_list)
        self.name = self.element + " " + self.animal + "o"
        self.health = random.randint(stats_list['Health']['Min'], stats_list['Health']['Max'])
        self.attack = random.randint(stats_list['Attack']['Min'], stats_list['Attack']['Max'])
        self.defense = random.randint(stats_list['Defense']['Min'], stats_list['Defense']['Max'])
        self.speed = random.randint(stats_list['Speed']['Min'], stats_list['Speed']['Max'])
        self.is_alive = True

    def get_name(self):
        return self.name

    def get_element(self):
        return self.element

    def get_animal(self):
        return self.animal

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

    def show_stats(self):
        print(
            "Health: ", self.get_health(),
            "Attack: ", self.get_attack(),
            "Defense: ", self.get_defense(),
            "Speed: ", self.get_speed())

    def deal_damage(self, opp_enima, element_list):
        own_element = self.get_element()
        target_element = opp_enima.get_element()
        if element_list[own_element]['Destroys'] == target_element:
            bonus = 1.5
        elif element_list[own_element]['Strengthens'] == target_element:
            bonus = 0.5
        else:
            bonus = 1.0
        return Combat.calc_damage(self.get_attack(), opp_enima.get_defense(), bonus), bonus

    def take_damage(self, damage: float):
        self.health = self.health - damage

    def check_if_dead(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return 1
        else:
            return 0


class Player:
    def __init__(self):
        self.enima = []
        self.lead = None

    def set_enima(self, enima_obj):
        self.enima.append(enima_obj)

    def arrange_party(self):
        temp_list = [self.enima[self.lead]]
        del self.enima[self.lead]

        for enima_obj in self.enima:
            temp_list.append(enima_obj)

        self.enima = temp_list

    def switch(self, current_enima: int, target_enima: int, i: int):
        UserInterface.switch_lead_message(self, i)
        self.enima[current_enima], self.enima[target_enima] = self.enima[target_enima], self.enima[current_enima]
        UserInterface.new_lead_message(self)


class UserInterface:
    @staticmethod
    def show_lead_info(player: Player):
        if player == you:
            player_name = "Your"
        else:
            player_name = "Joey's"
        print(f"{player_name} Enima:     {player.enima[0].get_name()} "
              f"HP {player.enima[0].get_health()}   "
              f"[ATK] {player.enima[0].get_attack()}  "
              f"(DEF) {player.enima[0].get_defense()}  "
              f"<SPD> {player.enima[0].get_speed()}")
        # Use this code instead if you only want to show HP. Will have to rewrite some parts of the code.
        # print(f"Joey's Enima:   {player.enima[0].get_name()} HP {player.enima[0].get_health()}")

    @staticmethod
    def show_options(player: Player):
        print("\nWhat will you do?")
        print("(1) Attack")
        print(f"(2) Switch to: {player.enima[1].get_name()} "
              f"HP {player.enima[1].get_health()}   "
              f"[ATK] {player.enima[1].get_attack()}  "
              f"(DEF) {player.enima[1].get_defense()}  "
              f"<SPD> {player.enima[1].get_speed()}")
        print(f"(3) Switch to: {player.enima[2].get_name()} "
              f"HP {player.enima[2].get_health()}   "
              f"[ATK] {player.enima[2].get_attack()}  "
              f"(DEF) {player.enima[2].get_defense()}  "
              f"<SPD> {player.enima[2].get_speed()}")

    @staticmethod
    def switch_failed(target: Enima):
        print(f"{target.get_name()} is dead. Please choose another one.")

    @staticmethod
    def switch_lead_message(player: Player, i: int):
        if i == 1:
            print(f"{player.enima[0].get_name()} has been switched out.", end=" ")
        else:
            print(f"Youngster Joey switched out {player.enima[0].get_name()}.", end=" ")

    @staticmethod
    def new_lead_message(player: Player):
        rand_dialog = random.choice(range(7))
        if rand_dialog == 0:
            print(f"Go {player.enima[0].get_name()}!")
        elif rand_dialog == 1:
            print(f"It's your turn, {player.enima[0].get_name()}!")
        elif rand_dialog == 2:
            print(f"{player.enima[0].get_name()}, let him feel the pain!")
        elif rand_dialog == 3:
            print(f"Just do it, {player.enima[0].get_name()}!")
        elif rand_dialog == 4:
            print(f"{player.enima[0].get_name()}, show him no mercy!")
        elif rand_dialog == 5:
            print(f"Fear is for the weak, {player.enima[0].get_name()}!")
        else:
            print(f"You are the bone of my sword, {player.enima[0].get_name()}!")

    @staticmethod
    def display_damage(attacker: Enima, target: Enima, damage: int, pain: float):
        if pain == 1.5:
            print(f"{attacker.get_name()} attacks {target.get_name()}!")
            print(f"{target.get_name()} received {damage} damage. It looks quite painful!")
        elif pain == 0.5:
            print(f"{attacker.get_name()} attacks {target.get_name()}!")
            print(f"{target.get_name()} received {damage} damage, but it's just a scratch...")
        else:
            print(f"{attacker.get_name()} attacks {target.get_name()}!")
            print(f"{target.get_name()} received {damage} damage.")

    @staticmethod
    def enima_died(dead_enima: Enima):
        print(f"{dead_enima.get_name()} has died!")

    @staticmethod
    def choose_next_enima(player: Player):
        if all(e.get_health() <= 0 for e in player.enima):
            GameStates.game_lost()
            return {}

        print("\nSend out your next Enima: ")
        temp_dict = {}
        for pos, e in enumerate(player.enima):
            if e.get_health() > 0:
                print(f"({pos}) {e.get_name()} "
                      f"HP {e.get_health()} "
                      f"[ATK] {e.get_attack()} "
                      f"(DEF) {e.get_defense()} "
                      f"<SPD> {e.get_speed()}")
                temp_dict[pos] = e
        return temp_dict


def choose_randomly(random_value):
    result = random_value

    # 60% to choose Attack, 20% to switch to 2nd Enima, 20% to switch to 3rd Enima
    if result <= 0.60:
        response = 1
    elif (result > 0.60) and (result <= 0.80):
        response = 2
    else:
        response = 3

    return response


class InputProcessor:
    @staticmethod
    def check_if_input_valid(is_true: bool, expected_values):
        while is_true:
            response = input()
            if response in expected_values:
                return int(response)
            else:
                print("Invalid choice. Please choose other options:", *expected_values)

    @staticmethod
    def check_inputs(your_input: int, bot_input: int, player: Player, bot: Player, element_list):
        if your_input != 1 and bot_input != 1:
            if player.enima[your_input - 1].check_if_dead() == 1:
                UserInterface.switch_failed(player.enima[your_input - 1])
                new_input = InputProcessor.check_if_input_valid(True, ["1", "2", "3"])
                InputProcessor.check_inputs(new_input, bot_input, player, bot, element_list)
            else:
                player.switch(0, your_input - 1, 1)
            if bot.enima[bot_input - 1].check_if_dead() == 1:
                if bot_input == 2:
                    bot_input = 3
                else:
                    bot_input = 2
                # temp_list = []
                # for e in bot.enima:
                #     if e.get_health() > 0:
                #         temp_list.append(e)
                #     else:
                #         pass
                # bot_input = random.randint(0, len(temp_list) - 1)
            bot.switch(0, bot_input - 1, 0)
        elif your_input != 1 and bot_input == 1:  # Bot attacks you
            if player.enima[your_input - 1].check_if_dead() == 1:  # Check if switch-in target dead
                UserInterface.switch_failed(player.enima[your_input - 1])  # If so, inform player
                new_input = InputProcessor.check_if_input_valid(True, ["1", "2", "3"])  # Ask for another choice
                InputProcessor.check_inputs(new_input, bot_input, player, bot, element_list)
            else:
                player.switch(0, your_input - 1, 1)
            result = Combat.resolve_damage_steps(bot.enima[0], player.enima[0], element_list)
            switched = Combat.switch_if_enima_dead(result, player)
            if switched in (0, 1):
                pass
            else:
                GameStates.exit_game()
        elif your_input == 1 and bot_input != 1:  # You attack bot
            if bot.enima[bot_input - 1].check_if_dead() == 1:
                if bot_input == 2:
                    bot_input = 3
                else:
                    bot_input = 2
                # temp_list = []
                # for e in bot.enima:
                #     if e.get_health() > 0:
                #         temp_list.append(e)
                #     else:
                #         pass
                # bot_input = random.randint(0, len(temp_list) - 1)
            bot.switch(0, bot_input - 1, 0)
            result2 = Combat.resolve_damage_steps(player.enima[0], bot.enima[0], element_list)
            switched = Combat.switch_if_bot_enima_died(result2, bot)
            if switched in (0, 1):
                pass
            else:
                GameStates.exit_game()
        else:
            go_first = Combat.compare_speed(player.enima[0].get_speed(), bot.enima[0].get_speed())
            if go_first:  # Player attacks, then bot attacks
                result2 = Combat.resolve_damage_steps(player.enima[0], bot.enima[0], element_list)
                switched = Combat.switch_if_bot_enima_died(result2, bot)
                if switched == 1:
                    pass
                elif switched == 0:
                    result = Combat.resolve_damage_steps(bot.enima[0], player.enima[0], element_list)
                    switched = Combat.switch_if_enima_dead(result, player)
                    if switched == 100:
                        GameStates.exit_game()
                else:
                    GameStates.exit_game()
            else:  # Bot attacks, then player attacks
                result = Combat.resolve_damage_steps(bot.enima[0], player.enima[0], element_list)
                switched = Combat.switch_if_enima_dead(result, player)
                if switched == 1:
                    pass
                elif switched == 0:
                    result2 = Combat.resolve_damage_steps(player.enima[0], bot.enima[0], element_list)
                    switched = Combat.switch_if_bot_enima_died(result2, bot)
                    if switched == 100:
                        GameStates.exit_game()
                else:
                    GameStates.exit_game()


class Combat:
    @staticmethod
    def compare_speed(player_enima_spd: int, bot_enima_speed: int):
        if player_enima_spd == bot_enima_speed:
            return random.randint(0, 1)
        elif player_enima_spd > bot_enima_speed:
            return 1
        else:
            return 0

    @staticmethod
    def calc_damage(attack: int, defense: int, element_bonus: float):
        return ((attack * 520) / (defense + 400)) * element_bonus + random.randint(0, 32)

    @staticmethod
    def resolve_damage_steps(attacker: Enima, target: Enima, element_list):
        damage, painfulness = attacker.deal_damage(target, element_list)
        target.take_damage(round(damage))
        UserInterface.display_damage(attacker, target, round(damage), painfulness)
        has_died = target.check_if_dead()
        if has_died == 1:
            UserInterface.enima_died(target)
            return 1
        else:
            return 0

    @staticmethod
    def switch_if_enima_dead(result, player: Player):
        if result == 1:
            while True:
                remaining_enima = UserInterface.choose_next_enima(player)
                if not remaining_enima:
                    return 100
                response2 = int(input())
                if response2 in remaining_enima:
                    player.switch(0, response2, 1)
                    return 1
                else:
                    print("Invalid choice. Please choose again.")
        else:
            return 0

    @staticmethod
    def switch_if_bot_enima_died(result, bot: Player):
        if result == 1:  # if result is 1, bot's Enima just died this turn
            for _ in bot.enima:
                if any(e.get_health() > 0 for e in bot.enima):  # If any of Joey's Enima is alive, allow switching
                    rand_e = random.choice(bot.enima[1:])  # Choose random Enima
                    while rand_e.get_health() <= 0:  # While chosen Enima is dead
                        rand_e = random.choice(bot.enima[1:])  # Continue choosing a random Enima
                    bot.switch(0, bot.enima.index(rand_e), 0)  # Switch after a live Enima is found
                    return 1
                else:
                    GameStates.game_won()  # Invoke a method to end the game, Player wins
                    return 100
        else:  # If result is 0, bot's Enima is still alive, there is nothing to do so just return 0
            return 0


class GameStates:
    someone_lost = False

    @staticmethod
    def game_lost():
        GameStates.someone_lost = True
        print("\nYou are out of useable Enima! You have lost the game :C")

    @staticmethod
    def game_won():
        GameStates.someone_lost = True
        print("\nYoungster Joey is out of useable Enima! You have won the game!")

    @staticmethod
    def exit_game():
        go_out_with_a_bang = input("\nPress any key to exit.\n")
        if go_out_with_a_bang:
            sys.exit(0)


if __name__ == '__main__':
    start_message = (
        "Hey there, welcome to the world of Os. \n"
        f"One boring afternoon, some scientists decided to experiment on animals and made them fight each other.\n" 
        f"This resulted in the creation of Enima, elemental animals whose sole purpose is to fight.\n" 
        f"" 
        f"So that's the backstory. Now take these Enima with you, and go spill some blood!\n")

    print(start_message)

    you = Player()
    joey = Player()

    # 1. Drafting stage
    current_choice = 0

    while current_choice < 3:
        print(f"Choose your Enima (Choice {current_choice + 1} of 3): ")

        enima_list = []

        draft_choice = 0
        while draft_choice < 3:
            new_enima = Enima(animals, elements, stats)
            enima_list.append(new_enima)
            draft_choice += 1

        for num, item in enumerate(enima_list):
            print(f"({num + 1})", item.get_name())
            item.show_stats()

        valid_choice = False
        while not valid_choice:
            enima_choice = input()
            if enima_choice == "1" or enima_choice == "2" or enima_choice == "3":
                you.set_enima(enima_list[int(enima_choice) - 1])
                print(you.enima[current_choice].get_name(), "has been added to your cage.")
                del enima_list[int(enima_choice) - 1]
                valid_choice = True
            else:
                print("Invalid choice. Please choose 1, 2 or 3.")

        joey.set_enima(enima_list[random.randint(0, 1)])
        print("Younger Joey has randomly chosen one of the remaining Enima.\n")

        current_choice += 1

    # 2. Lead selection
    print("Which Enima to start with?")
    for num, enima in enumerate(you.enima):
        print(f"({num+1})", enima.get_name())

    lead = None
    valid_choice = False
    while not valid_choice:
        lead_choice = input()
        if lead_choice == "1" or lead_choice == "2" or lead_choice == "3":
            print(f"{you.enima[int(lead_choice) - 1].get_name()} has been chosen as lead.\n")
            you.lead = int(lead_choice) - 1
            valid_choice = True
        else:
            print("Invalid choice. Please choose 1, 2 or 3.")

    joey.lead = random.randint(0, 2)
    # print("Joey's lead is", joey.lead)

    you.arrange_party()
    joey.arrange_party()
    you.lead = 0
    joey.lead = 0

    # 3. Battle!
    print("Let the fight begin!")
    turn_counter = 1
    while not GameStates.someone_lost:
        print(f"Turn {turn_counter}:\n")
        UserInterface.show_lead_info(you)
        UserInterface.show_lead_info(joey)
        UserInterface.show_options(you)
        player_input = InputProcessor.check_if_input_valid(True, ["1", "2", "3"])
        ai_input = choose_randomly(random.random())
        if all(e.get_health() <= 0 for e in joey.enima[1:]):
            ai_input = 1
        InputProcessor.check_inputs(player_input, ai_input, you, joey, elements)
        print()
        turn_counter += 1

