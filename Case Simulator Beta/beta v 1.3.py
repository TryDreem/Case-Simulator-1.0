import random
import time
from items import items

from colorama import Fore, Style, init

init(autoreset=True)


case_prices = {
    "recoil_case": 3,
    "cs20_case": 3,
    "dreams_nightmares_case": 4
}

def determine_condition(float_value):
    if 0 < float_value < 0.07:
        return "Factory New"
    elif 0.07 <= float_value < 0.15:
        return "Minimal Wear"
    elif 0.15 <= float_value < 0.37:
        return "Field-Tested"
    elif 0.37 <= float_value < 0.44:
        return "Well-Worn"
    else:
        return "Battle-Scarred"

def calculate_final_price(price, value_float):
    if 0.005 <= value_float < 0.01:
        return price * 1.5
    elif 0.003 <= value_float < 0.005:
        return price * 2
    elif 0.002 <= value_float < 0.003:
        return price * 4
    elif 0.001 < value_float < 0.002:
        return price * 5
    elif 0.0005 < value_float < 0.001:
        return price * 7
    elif 0 < value_float < 0.0005:
        return price * 10
    elif 0.15 > value_float >= 0.07:
        return price * 0.8
    elif 0.37 > value_float >= 0.15:
        return price * 0.6
    elif 0.44 > value_float >= 0.37:
        return price * 0.5
    elif 1 > value_float >= 0.44:
        return price * 0.4
    else:
        return price


def greeting():
    collected_items = []
    balance = 150
    intrigue_enabled = True
    extra_attempt_1 = 1
    extra_attempt_2 = 3
    print("Hello,welcome to Case Simulator beta!")


    while True:
        print(f"Your current balance is {Fore.LIGHTWHITE_EX}{balance:.2f}${Style.RESET_ALL}")
        print("Please choose any case you want to open...\n")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1.Recoil Case(3$) 2.CS20 Case (3$) 3.Dreams & Nightmares Case/(4$)\n"
              f"{Fore.LIGHTYELLOW_EX}4.Sell item  {Fore.LIGHTGREEN_EX}5.Sell all items  {Fore.LIGHTCYAN_EX}"
              f"{Fore.LIGHTRED_EX}6.Exit{Style.RESET_ALL}\n")
        if intrigue_enabled:
            print("Press '/' to disable intrigue ")
        choice = input("Choose one of the cases and write down it below...")


        if choice == "1" or choice.lower() == "recoil case":
            case_price = case_prices["recoil_case"]
            if balance >= case_price:
                balance -= case_price
                print("Well,you chose Recoil case")
                item, rarity, item_price, condition, float_value = open_recoil_case(intrigue_enabled)
                collected_items.append((item, rarity,item_price, condition, float_value))
            else:
                extra_attempt_2 += 1
                print("Sorry,you don't have enough money")


        elif choice == "2" or choice.lower() == "cs20 case":
            case_price = case_prices["cs20_case"]
            if balance >= case_price:
                balance -= case_price
                print("Fine,you chose CS20 Case")
                item, rarity, item_price, condition, float_value = open_cs20_case(intrigue_enabled)
                collected_items.append((item, rarity, item_price, condition, float_value))
            else:
                extra_attempt_2 += 1
                print("Sorry,you don't have enough money")


        elif choice == "3" or choice.lower() == "dreams nightmares case":
            case_price = case_prices["dreams_nightmares_case"]
            if balance >= case_price:
                balance -= case_price
                print("Great,you chose Gamma Case")
                item, rarity, item_price, condition, float_value = open_dreams_nightmares_case(intrigue_enabled)
                collected_items.append((item, rarity, item_price,condition,float_value))
            else:
                extra_attempt_2 += 1
                print("Sorry,you don't have enough money")


        elif choice == "4" or choice.lower() == "s":
           if collected_items:
               print("Which item would you like to sell?")
               for i, (item, rarity, price, condition, float_value) in enumerate(collected_items):
                   item_color = items[item]["color"]
                   final_price = calculate_final_price(price, float_value)
                   print(f'{i+1}.{item_color} {item} -{rarity} ({final_price:.2f}$){Style.RESET_ALL}'
                         f'{Fore.LIGHTWHITE_EX} [{condition} : {float_value:.4f}]{Style.RESET_ALL}')
               item_choice = input("Enter the number of the item(s) for selling").strip()
               items_to_sell = set()

               for part in item_choice.split('*'):
                   if "-" in part:
                       start, end = part.split('-')
                       if start.isdigit() and end.isdigit():
                           items_to_sell.update(range(int(start) -1, int(end)))
                   elif part.isdigit():
                       items_to_sell.add(int(part) - 1)


               exclude_items = item_choice.split('*')[1:]
               for exclude in exclude_items:
                   if exclude.isdigit():
                       items_to_sell.discard(int(exclude) - 1)


               if items_to_sell:
                   sold_items = []
                   total_price = 0

                   for idx in sorted(items_to_sell,reverse = True):
                       if 0 <= idx < len(collected_items):
                           sold_item, sold_rarity, sold_price, sold_condition, sold_float_value = collected_items.pop(idx)
                           sold_item_color = items[sold_item]['color']
                           final_price = calculate_final_price(sold_price, sold_float_value)
                           sold_items.append(f'{sold_item_color}{sold_item} ({final_price:.2f}$) '
                                             f'{Fore.LIGHTWHITE_EX}'
                                             f'[{sold_condition} : {sold_float_value:.4f}]{Style.RESET_ALL}')
                           total_price += final_price

                   balance += total_price
                   print(f"You sold {', '.join(sold_items)} for {total_price:.2f}$")
               else:
                   print("Invalid range or no items for selling.")

           else:
               print("You have no items for selling")


        elif choice == "5" or choice.lower() == "sa":
            if collected_items:
                total_price = sum(calculate_final_price(price, float_value)
                                  for _, _, price, _, float_value in collected_items)
                collected_items.clear()
                balance += total_price
                print(f"You sold all your items for {total_price:.2f}$")
            else:
                print("You don't have any items for selling")


        elif choice == "6" or choice.lower() == "exit" :
            print("Thank for playing!Here are all the items you got:")
            for item, rarity, item_price, condition, float_value in collected_items:
                item_color = items[item]["color"]
                final_price = calculate_final_price(item_price, float_value)
                print(f'{item_color}{item}{rarity}({final_price:.2f}$){Style.RESET_ALL}'
                      f' {Fore.LIGHTWHITE_EX}[{condition} : {float_value:.4f}] {Style.RESET_ALL}')
            break
        elif choice == "/":
            intrigue_enabled = not intrigue_enabled # Переключаем состояние интриги
            state = "enabled" if intrigue_enabled else "disabled"
            print(f"Intrigue is now {state}.")

        elif choice.lower().startswith("give"):
            choice = choice.replace(" ", "")
            amount_str = choice[4:]
            if amount_str.isdigit():
                amount = int(amount_str)
                balance += amount
                print(f"You have received {amount:.2f}$, now your balance is: {balance:.2f}$")
            else:
                print("Please enter a positive amount")

        if balance < 100:
            if extra_attempt_1 >= 1:
                while True:
                    print(f"Your current balance is {Fore.LIGHTWHITE_EX}{balance:.2f}${Style.RESET_ALL}")
                    print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}You can type 'tips' or '100' to get extra 100$ or type 'skip'"
                          f"{Style.RESET_ALL}")
                    user_input = input("Type your choice...")
                    if user_input.lower() == "tips" or user_input == "100":
                        balance += 100
                        extra_attempt_1 -= 1
                        print(f"Your current balance is {Fore.LIGHTWHITE_EX}{balance:.2f}${Style.RESET_ALL}")
                        break
                    elif user_input.lower() == "skip":
                        extra_attempt_1 -= 1
                        break
                    else:
                        print("Type 'tips', '100' or 'skip'")

        if balance < 100:
            if extra_attempt_2 >= 3:
                while True:
                    print(f"Your current balance is {Fore.LIGHTWHITE_EX}{balance:.2f}${Style.RESET_ALL}")
                    print(f"{Fore.LIGHTWHITE_EX}{Style.BRIGHT}You can type 'tips' or '100' to get extra 100$ or type 'skip'"
                          f"{Style.RESET_ALL}")
                    user_input = input("Type your choice...")
                    if user_input.lower() == "tips" or user_input == "100":
                        balance += 100
                        extra_attempt_2 -= 3
                        print(f"Your current balance is {Fore.LIGHTWHITE_EX}{balance:.2f}${Style.RESET_ALL}")
                        break
                    elif user_input.lower() == "skip":
                        extra_attempt_2 -= 3
                        break
                    else:
                        print("Type 'tips', '100' or 'skip'")




        else:
            print("I'm so sorry,could you choose again?")



def delay_with_intrigue(enabled):
    if enabled:
        print(Fore.GREEN + "Wait... what is it!?\n",end= "",flush = True)
        for _ in range (4):
            time.sleep(1) # Задержка на 1 секунду
            print(Fore.GREEN + ".", end='', flush=True) # Выводим точки для интриги
        print() # Переход на новую строку

def open_recoil_case(intrigue_enabled):
    items_in_case = [
        "Ump-45 | Roadblock","Negev | Drop Me","MAC-10 | Monkeyflage","Galil AR | Destroyer","FAMAS | Meow 36",
        "Glock-18 | Winterized","M4A4 | Poly Mag","R8 Revolver | Crazy 8","M249 | Downtown","P90 | Vent Rush",
        "Dual Berettas | Flora Carnivora","SG 553 | Dragon Tech","Sawed-Off | Kiss♥Love","P250 | Visions",
        "AK-47 | Ice Coaled","AWP | Chromatic Aberration","USP-S | Printstream","★ Broken Fang Gloves | Needle Point",
        "★ Broken Fang Gloves | Yellow-banded","★ Moto Gloves | Finish Line","★ Hand Wraps | CAUTION!",
        "★ Moto Gloves | Blood Pressure","★ Specialist Gloves | Field Agent","★ Sport Gloves | Nocts",
        "★ Specialist Gloves | Tiger Strike","★ Driver Gloves | Snow Leopard","★ Sport Gloves | Slingshot"]
    probabilities = [0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.032, 0.032, 0.032, 0.032, 0.032,
                     0.01067, 0.01067, 0.01067, 0.0032, 0.0032, 0.00026, 0.00026, 0.00026, 0.00026, 0.00026,
                     0.00026, 0.00026, 0.00026, 0.00026, 0.00026]
    result = random.choices(items_in_case,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    float_value = init_float_value()
    condition = determine_condition(float_value)
    item_color = items[result]["color"]
    item_price = items[result]["price"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}"
          f"{Fore.LIGHTWHITE_EX} [{condition} : {float_value:.4f}] {Style.RESET_ALL}")
    return result, items[result]['rarity'], item_price, condition, float_value


def init_float_value():
    if random.random() < 0.02:
        float_value = random.uniform(0, 0.007)
    elif 0.02 <= random.random() < 0.9:
        float_value = random.uniform(0.007, 0.5)
    else:
        float_value = random.uniform(0.5, 1)
    return float_value


def open_cs20_case(intrigue_enabled):
    items_in_case = [
        "SCAR-20 | Assault", "MAG-7 | Popdog", "Dual Berettas | Elite 1.6", "Tec-9 | Flash Out",
        "MAC-10 | Classic Crate",
        "FAMAS | Decommissioned", "Glock-18 | Sacrifice", "Five-SeveN | Buddy", "P250 | Inferno", "UMP-45 | Plastique",
        "M249 | Aztec", "MP5-SD | Agent", "AUG | Death by Puppy", "P90 | Nostalgia", "MP9 | Hydra",
        "FAMAS | Commemoration", "AWP | Wildfire", "★ Classic Knife | Forest DDPAT", "★ Classic Knife | Safari Mesh",
        "★ Classic Knife | Scorched", "★ Classic Knife | Stained", "★ Classic Knife | Blue Steel",
        "★ Classic Knife | Vanilla", "★ Classic Knife | Crimson Web", "★ Classic Knife | Slaughter",
        "★ Classic Knife | Case Hardened", "★ Classic Knife | Fade"
    ]
    probabilities = [0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.032, 0.032, 0.032, 0.032, 0.032,
                     0.01067, 0.01067, 0.01067, 0.0032, 0.0032, 0.00026, 0.00026, 0.00026, 0.00026, 0.00026,
                     0.00026, 0.00026, 0.00026, 0.00026, 0.00026]
    result = random.choices(items_in_case,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    if random.random() < 0.02:
        float_value = random.uniform(0, 0.007)
    elif 0.02 <= random.random() < 0.9:
        float_value = random.uniform(0.007, 0.5)
    else:
        float_value = random.uniform(0.5, 1)
    condition = determine_condition(float_value)
    item_color = items[result]["color"]
    item_price = items[result]["price"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}"
          f"{Fore.LIGHTWHITE_EX} [{condition} : {float_value:.4f}] {Style.RESET_ALL}")
    return result, items[result]['rarity'], item_price, condition, float_value

def open_dreams_nightmares_case(intrigue_enabled):
    items_in_case = [
        "SCAR-20 | Poultrygeist", "MAG-7 | Foresight", "P2000 | Lifted Spirits", "MP5-SD | Necro Jr.",
        "Sawed-Off | Spirit Board",
        "MAC-10 | Ensnared", "Five-SeveN | Scrawl", "PP-Bizon | Space Cat", "XM1014 | Zombie Offensive",
        "M4A1-S | Night Terror",
        "USP-S | Ticket to Hell", "G3SG1 | Dream Glade", "MP7 | Abyssal Apparition", "FAMAS | Rapid Eye Movement",
        "Dual Berettas | Melondrama", "MP9 | Starlight Protector", "AK-47 | Nightwish", "★ Shadow Daggers | Autotronic",
        "★ Falchion Knife | Autotronic", "★ Falchion Knife | Gamma Doppler Phase 4",
        "★ Falchion Knife | Gamma Doppler Phase 1",
        "★ Huntsman Knife | Gamma Doppler Phase 2", "★ Falchion Knife | Gamma Doppler Emerald",
        "★ Butterfly Knife | Black Laminate", "★ Butterfly Knife | Autotronic",
        "★ Butterfly Knife | Gamma Doppler Phase 2",
        "★ Butterfly Knife | Gamma Doppler Emerald"
    ]
    probabilities = [0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.1141, 0.032, 0.032, 0.032, 0.032, 0.032,
                     0.01067, 0.01067, 0.01067, 0.0032, 0.0032, 0.00042, 0.00042, 0.00042, 0.00026, 0.00026,
                     0.00026, 0.00026, 0.00013, 0.0001, 0.00007]
    result = random.choices(items_in_case,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    if random.random() < 0.02 :
        float_value = random.uniform(0, 0.007)
    elif 0.02 <= random.random() < 0.9:
        float_value = random.uniform(0.007, 0.5)
    else:
        float_value = random.uniform(0.5, 1)
    condition = determine_condition(float_value)
    item_color = items[result]["color"]
    item_price = items[result]["price"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}"
          f"{Fore.LIGHTWHITE_EX} [{condition} : {float_value:.4f}] {Style.RESET_ALL}")
    return result, items[result]['rarity'], item_price, condition, float_value

greeting()

