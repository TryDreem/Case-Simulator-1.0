import random
import time


from colorama import Fore, Style, init

init(autoreset= True)

rarities = {
    "Xiaomi Redmi A2": {"rarity": " (common)", "color": Fore.WHITE, "price": 50},
    "Samsung Galaxy A15": {"rarity": " (rare)", "color": Fore.BLUE, "price": 110},
    "Samsung S23 Ultra": {"rarity": " (very rare)", "color": Fore.MAGENTA, "price": 650},
    "iPhone 15 Pro Max": {"rarity": " (legendary)", "color": Fore.LIGHTMAGENTA_EX, "price": 1350},

    "Geforce GT 730": {"rarity": " (common)", "color": Fore.WHITE, "price": 60},
    "Radeon RX 560": {"rarity": " (rare)", "color": Fore.BLUE, "price": 90},
    "Geforce RTX 3070": {"rarity": " (very rare)", "color": Fore.MAGENTA, "price": 350},
    "Geforce RTX 4090": {"rarity": " (legendary)", "color": Fore.LIGHTMAGENTA_EX, "price": 2000},

    "The last of us I PS5 Disk": {"rarity": " (common)", "color": Fore.WHITE, "price": 40},
    "DualSense": {"rarity": " (rare)", "color": Fore.BLUE, "price": 70},
    "PlayStation VR 2": {"rarity": " (very rare)", "color": Fore.MAGENTA, "price": 700},
    "PlayStation 5 Pro": {"rarity": " (legendary)", "color": Fore.LIGHTMAGENTA_EX, "price": 900}
}

case_prices = {
    "alpha_case": 150,
    "beta_case":150,
    "gamma_case":150
}



def greeting():
    collected_items = []
    balance = 1000
    intrigue_enabled = True
    print("Hello,welcome to Case Simulator beta!")

    while True:
        print(f"Your current balance is {Fore.LIGHTWHITE_EX}{balance}${Style.RESET_ALL}")
        print("Please choose any case you want to open...\n")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1.Alpha Case(150$) 2.Beta Case(150$) 3.Gamma Case(150$)\n"
              f"{Fore.LIGHTYELLOW_EX}4.Sell item  {Fore.LIGHTGREEN_EX}5.Sell all items  {Fore.LIGHTCYAN_EX}"
              f"{Fore.LIGHTRED_EX}6.Exit{Style.RESET_ALL}\n")
        if intrigue_enabled:
            print("Press '/' to disable intrigue ")
        choice = input("Choose one of the cases and write down it below...")


        if choice == "1" or choice.lower() == "alpha case":
            case_price = case_prices["alpha_case"]
            if balance >= case_price:
                balance -= case_price
                print("Well,you chose Alpha Case")
                item, rarity, item_price = open_alpha_case(intrigue_enabled)
                collected_items.append((item, rarity,item_price))
            else:
                print("Sorry,you don't have enough money")


        elif choice == "2" or choice.lower() == "beta case":
            case_price = case_prices["beta_case"]
            if balance >= case_price:
                balance -= case_price
                print("Fine,you chose Beta Case")
                item, rarity, item_price = open_beta_case(intrigue_enabled)
                collected_items.append((item, rarity, item_price))
            else:
                print("Sorry,you don't have enough money")


        elif choice == "3" or choice.lower() == "gamma case":
            case_price = case_prices["gamma_case"]
            if balance >= case_price:
                balance -= case_price
                print("Great,you chose Gamma Case")
                item, rarity, item_price = open_gamma_case(intrigue_enabled)
                collected_items.append((item, rarity, item_price))
            else:
                print("Sorry,you don't have enough money")


        elif choice == "4" or choice.lower() == "s":
           if collected_items:
               print("Which item would you like to sell?")
               for i, (item, rarity, price) in enumerate(collected_items):
                   item_color = rarities[item]["color"]
                   print(f'{i+1}.{item_color} {item} - {rarity} ({price}${Style.RESET_ALL})')
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
                           sold_item, sold_rarity, sold_price = collected_items.pop(idx)
                           sold_item_color = rarities[sold_item]['color']
                           sold_items.append(f'{sold_item_color}{sold_item} ({sold_price}$)')
                           total_price += sold_price

                   balance += total_price
                   print(f"You sold {','.join(sold_items)} for {total_price}$")
               else:
                   print("Invalid range or no items for selling.")

           else:
               print("You have no items for selling")


        elif choice == "5" or choice.lower() == "sa":
            if collected_items:
                total_price = sum(price for _, _, price in collected_items)
                collected_items.clear()
                balance += total_price
                print(f"You sold all your items for {total_price}$")
            else:
                print("You don't have any items for selling")


        elif choice == "6" or choice.lower() == "exit" :
            print("Thank for playing!Here are all the items you got:")
            for item, rarity, item_price in collected_items:
                item_color = rarities[item]["color"]
                print(f'{item_color}{item}{rarity}{item_price}${Style.RESET_ALL}')
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
                print(f"You have received {amount}$, now your balance is: {balance}$")
            else:
                print("Please enter a positive amount")


        else:
            print("I'm so sorry,could you choose again?")


def delay_with_intrigue(enabled):
    if enabled:
        print(Fore.GREEN + "Wait... what is it!?\n",end= "",flush = True)
        for _ in range (4):
            time.sleep(1) # Задержка на 1 секунду
            print(Fore.GREEN + ".", end='', flush=True) # Выводим точки для интриги
        print() # Переход на новую строку

def open_alpha_case(intrigue_enabled):
    items = ["Xiaomi Redmi A2","Samsung Galaxy A15","Samsung S23 Ultra","iPhone 15 Pro Max"]
    probabilities = [0.7, 0.23, 0.06, 0.01]
    result = random.choices(items,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    item_color = rarities[result]["color"]
    item_price = rarities[result]["price"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}")
    return result, rarities[result]['rarity'], item_price

def open_beta_case(intrigue_enabled):
    items = ["Geforce GT 730","Radeon RX 560","Geforce RTX 3070","Geforce RTX 4090"]
    probabilities = [0.75, 0.18, 0.06, 0.01]
    result = random.choices(items,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    item_color = rarities[result]["color"]
    item_price = rarities[result]["price"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}")
    return result, rarities[result]['rarity'], item_price

def open_gamma_case(intrigue_enabled):
    items = ["The last of us I PS5 Disk","DualSense","PlayStation VR 2","PlayStation 5 Pro"]
    probabilities = [0.6, 0.35, 0.03, 0.02]
    result = random.choices(items,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    item_color = rarities[result]["color"]
    item_price = rarities[result]["price"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}")
    return result, rarities[result]['rarity'], item_price

greeting()

