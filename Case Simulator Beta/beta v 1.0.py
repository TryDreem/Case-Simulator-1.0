import random
import time
from colorama import Fore, Style, init

init(autoreset= True)

rarities = {
    "Xiaomi Redmi A2": {"rarity": " (common)", "color": Fore.WHITE},
    "Samsung Galaxy A15": {"rarity": " (rare)", "color": Fore.BLUE},
    "Samsung S23 Ultra": {"rarity": " (very rare)", "color": Fore.MAGENTA},
    "iPhone 15 Pro Max": {"rarity": " (mythical)", "color": Fore.RED},

    "Geforce GT 730": {"rarity": " (common)", "color": Fore.WHITE},
    "Radeon RX 560": {"rarity": " (rare)", "color": Fore.BLUE},
    "Geforce RTX 3070": {"rarity": " (very rare)", "color": Fore.MAGENTA},
    "Geforce RTX 4090": {"rarity": " (mythical)", "color": Fore.RED},

    "The last of us I PS5 Disk": {"rarity": " (common)", "color": Fore.WHITE},
    "DualSense": {"rarity": " (rare)", "color": Fore.BLUE},
    "PlayStation VR 2": {"rarity": " (very rare)", "color": Fore.MAGENTA},
    "PlayStation 5 Pro": {"rarity": " (mythical)", "color": Fore.RED}
}

def greeting():
    collected_items = []
    intrigue_enabled = True
    print("Hello,welcome to Case Simulator beta!")

    while True:
        print("Please choose any case you want to open...")
        print("1.Alpha Case\n2.Beta Case\n3.Gamma Case\n4.Exit")
        if intrigue_enabled:
            print("Press '/' to disable intrigue ")
        choice = input("Choose one of the cases and write down it below...")

        if choice == "1" or choice.lower() == "alpha case":
            print("Well,you chose Alpha Case")
            item, rarity = open_alpha_case(intrigue_enabled)
            collected_items.append((item, rarity))
        elif choice == "2" or choice.lower() == "be1ta case":
            print("Fine,you chose Beta Case")
            item, rarity = open_beta_case(intrigue_enabled)
            collected_items.append((item, rarity))
        elif choice == "3" or choice.lower() == "gamma case":
            print("Great,you chose Gamma Case")
            item, rarity = open_gamma_case(intrigue_enabled)
            collected_items.append((item, rarity))
        elif choice == "4" or choice.lower() == "exit" :
            print("Thank for playing!Here are all the items you got:")
            for item, rarity in collected_items:
                item_color = rarities[item]["color"]
                print(f'{item_color}{item}{rarity}{Style.RESET_ALL}')
            break
        elif choice == "/":
            intrigue_enabled = not intrigue_enabled # Переключаем состояние интриги
            state = "enabled" if intrigue_enabled else "disabled"
            print(f"Intrigue is now {state}.")

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
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}")
    return result, rarities[result]['rarity']

def open_beta_case(intrigue_enabled):
    items = ["Geforce GT 730","Radeon RX 560","Geforce RTX 3070","Geforce RTX 4090"]
    probabilities = [0.75, 0.18, 0.06, 0.01]
    result = random.choices(items,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    item_color = rarities[result]["color"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}")
    return result, rarities[result]['rarity']

def open_gamma_case(intrigue_enabled):
    items = ["The last of us I PS5 Disk","DualSense","PlayStation VR 2","PlayStation 5 Pro"]
    probabilities = [0.6, 0.35, 0.03, 0.02]
    result = random.choices(items,probabilities)[0]
    delay_with_intrigue(intrigue_enabled)
    item_color = rarities[result]["color"]
    print(f"Congratulations!You got: {item_color}{result}{Style.RESET_ALL}")
    return result, rarities[result]['rarity']

greeting()

