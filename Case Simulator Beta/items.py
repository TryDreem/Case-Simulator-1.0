
from colorama import Fore, Style, init


items = {
    "Ump-45 | Roadblock": {"rarity": " (Rare)", "color": Fore.BLUE, "price" : 0.2},
    "Negev | Drop Me": {"rarity": " (Rare)", "color": Fore.BLUE, "price" : 0.18},
    "MAC-10 | Monkeyflage": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.2},
    "Galil AR | Destroyer": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.17},
    "FAMAS | Meow 36": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.22},
    "Glock-18 | Winterized": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.23},
    "M4A4 | Poly Mag": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.24},
    "R8 Revolver | Crazy 8": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.7},
    "M249 | Downtown": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.22},
    "P90 | Vent Rush": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.33},
    "Dual Berettas | Flora Carnivora": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.75},
    "SG 553 | Dragon Tech": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.35},
    "Sawed-Off | Kiss♥Love": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 8.77},
    "P250 | Visions": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 8.11},
    "AK-47 | Ice Coaled": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 13.61},
    "AWP | Chromatic Aberration": {"rarity": " (Covert)", "color": Fore.LIGHTRED_EX, "price": 14},
    "USP-S | Printstream": {"rarity": " (Covert)", "color": Fore.LIGHTRED_EX, "price": 104.55},
    "★ Broken Fang Gloves | Needle Point": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 113.54},
    "★ Broken Fang Gloves | Yellow-banded": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 132.16},
    "★ Moto Gloves | Finish Line": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 290.43},
    "★ Hand Wraps | CAUTION!": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 383.85},
    "★ Moto Gloves | Blood Pressure": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 354.39},
    "★ Specialist Gloves | Field Agent": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 614.07},
    "★ Sport Gloves | Nocts": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 841.08},
    "★ Specialist Gloves | Tiger Strike": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 916.2},
    "★ Driver Gloves | Snow Leopard": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 984.22},
    "★ Sport Gloves | Slingshot": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 2262.14},

#recoil case items from above



    "SCAR-20 | Assault": {"rarity": " (Rare)", "color": Fore.BLUE, "price" : 0.24},
    "MAG-7 | Popdog": {"rarity": " (Rare)", "color": Fore.BLUE, "price" : 0.25},
    "Dual Berettas | Elite 1.6": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.27},
    "Tec-9 | Flash Out": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.3},
    "MAC-10 | Classic Crate": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.32},
    "FAMAS | Decommissioned": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.43},
    "Glock-18 | Sacrifice": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 1.02},
    "Five-SeveN | Buddy": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.45},
    "P250 | Inferno": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.52},
    "UMP-45 | Plastique": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.55},
    "M249 | Aztec": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.87},
    "MP5-SD | Agent": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 2.45},
    "AUG | Death by Puppy": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 10.55},
    "P90 | Nostalgia": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 10.69},
    "MP9 | Hydra": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 17.27},
    "FAMAS | Commemoration": {"rarity": " (Covert)", "color": Fore.LIGHTRED_EX, "price": 12.09},
    "AWP | Wildfire": {"rarity": " (Covert)", "color": Fore.LIGHTRED_EX, "price": 138.03},
    "★ Classic Knife | Forest DDPAT": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 128.5},
    "★ Classic Knife | Safari Mesh": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 128.77},
    "★ Classic Knife | Scorched": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 143.41},
    "★ Classic Knife | Stained": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 183.79},
    "★ Classic Knife | Blue Steel": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 214.17},
    "★ Classic Knife | Vanilla": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 321.66},
    "★ Classic Knife | Crimson Web": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 354.09},
    "★ Classic Knife | Slaughter": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 375.31},
    "★ Classic Knife | Case Hardened": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 387.37},
    "★ Classic Knife | Fade": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 615.84},

#cs20 case items from above



    "SCAR-20 | Poultrygeist": {"rarity": " (Rare)", "color": Fore.BLUE, "price" : 0.23},
    "MAG-7 | Foresight": {"rarity": " (Rare)", "color": Fore.BLUE, "price" : 0.23},
    "P2000 | Lifted Spirits": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.24},
    "MP5-SD | Necro Jr.": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.24},
    "Sawed-Off | Spirit Board": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.25},
    "MAC-10 | Ensnared": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.26},
    "Five-SeveN | Scrawl": {"rarity": " (Rare)", "color": Fore.BLUE, "price": 0.28},
    "PP-Bizon | Space Cat": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.3},
    "XM1014 | Zombie Offensive": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.35},
    "M4A1-S | Night Terror": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.48},
    "USP-S | Ticket to Hell": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.49},
    "G3SG1 | Dream Glade": {"rarity": " (Restricted)", "color": Fore.MAGENTA, "price": 1.5},
    "MP7 | Abyssal Apparition": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 6.77},
    "FAMAS | Rapid Eye Movement": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 6.8},
    "Dual Berettas | Melondrama": {"rarity": " (Classified)", "color": Fore.LIGHTMAGENTA_EX, "price": 7.08},
    "MP9 | Starlight Protector": {"rarity": " (Covert)", "color": Fore.LIGHTRED_EX, "price": 15.41},
    "AK-47 | Nightwish": {"rarity": " (Covert)", "color": Fore.LIGHTRED_EX, "price": 68.08},
    "★ Shadow Daggers | Autotronic": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 138.37},
    "★ Falchion Knife | Autotronic": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 217.07},
    "★ Falchion Knife | Gamma Doppler Phase 4": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 405.11},
    "★ Falchion Knife | Gamma Doppler Phase 1": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 431.05},
    "★ Huntsman Knife | Gamma Doppler Phase 2": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 496.96},
    "★ Falchion Knife | Gamma Doppler Emerald": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 1057.3},
    "★ Butterfly Knife | Black Laminate": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 1137.13},
    "★ Butterfly Knife | Autotronic": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 2241.17},
    "★ Butterfly Knife | Gamma Doppler Phase 2": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 4348.8},
    "★ Butterfly Knife | Gamma Doppler Emerald": {"rarity": " (Exceedingly Rare)", "color": Fore.LIGHTYELLOW_EX, "price": 16709.8},

#Dreams & Nightmares Case items from above



}
