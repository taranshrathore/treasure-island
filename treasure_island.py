import os
import sys
import time
import random

# ─────────────────────────────────────────────
#  ANSI COLOR PALETTE
# ─────────────────────────────────────────────
class C:
    RED    = '\033[91m'
    GREEN  = '\033[92m'
    YELLOW = '\033[93m'
    BLUE   = '\033[94m'
    MAGENTA= '\033[95m'
    CYAN   = '\033[96m'
    WHITE  = '\033[97m'
    BOLD   = '\033[1m'
    RESET  = '\033[0m'
    GOLD   = '\033[38;5;220m'
    ORANGE = '\033[38;5;208m'
    DARK   = '\033[38;5;240m'

# ─────────────────────────────────────────────
#  ASCII ART BANK
# ─────────────────────────────────────────────
TITLE_ART = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

DRAGON_ART = r"""
                                                    __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
                ___-==_       _-~o~  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |    \\ \ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
          '         ~-|      /|    |-~\~~       __--~~
                      |-~~-_/ |    |   ~\_   _-~            /\
                           /  \     \__   \/~                \__
                       _--~ _/ | .-~~____--~-/                  ~~==.
                      ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                 -_     ~\      ~~---l__i__i__--~~_/
                                 _-~-__   ~)  \--______________--~~
                               //.-~~~-~_--~- |-------~~~~~~~~
                                      //.-~~~--\
"""

SHARK_ART = r"""
                             ,-
                           ,'::|
                          /::::|
                        ,'::::o\                                      _..
         ____    _____,-:::::o   :                                ,-' /  `.
       .'    `. ,'                :                         __,  ,'   \    :
      /   .-.  \      ,-'''''-----:                        /  / /      `--./
     /   /   \  \    :            :                       /  / / ____
    /   /     \  \   :            :                     _/ /  / ,'  `\
   /   /  .-.  \  \  :           ,'          __...---'''  /  / /      \
  /   /  /   \  \  \ :          ,'     __,--'             /  / /  ,---./
 /  _/  /     \  \  `:         ,'  ,-''                  /  / /  /    \
`-'  `-'       `-'   `-'------'`--'                      `--`-'  `----'
"""

ZOMBIE_ART = r"""
        _....._
      .`  o o  `.
     /   .--.    \
    |   ( >< )    |
    |    `--'     |
     \  ________ /
      `----------'
      /|  BRAINS |\ 
     / |__________| \
    /  (  )   (  )   \
   /___________________\
"""

CAVE_ART = r"""
     /\         /\
    /  \       /  \
   / /\ \_____/ /\ \
  / /  (       )  \ \
 / /    )_____( \  \ \
/_/    /       \  \  \_\
|     |  o   o  |  |   |
|     |    ___  |  |   |
|     |   (   ) |  |   |
|_____|___(   )_|__|___|
          `---'
"""

TREASURE_ART = r"""
      _______
     /       \
    /  $   $  \
   |   $$$$$   |
   |  $     $  |
   |   $$$$$   |
    \  $   $  /
     \_______/
    /|  GOLD |\
   / |_______| \
  /  (__)(___)  \
 (________________)
"""

FIRE_ART = r"""
    )  )   (   )  )
   (  (   )  (  (
    ) ) ) (   ) ) )
   (_(_(__(   )_)_)_)
      |  FIRE  |
      |________|
   ~~~~~~~~~~~~~~~~~~~
"""

ISLAND_ART = r"""
          *    .  *       .
   .  *       .       .
.     .  *      .      .  *
      __|__
     / ooo \
    /ooooooo\
   /ooooooooo\
  /___________\
 ~~~~~~~~~~~~~~~
"""

SHIP_ART = r"""
      |    |    |
     )_)  )_)  )_)
    )___))___))___)\\
   )____)____)_____)\\\\
 _____|____|____|____\\\\\___
--------\                 /--------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^
"""

GAMEOVER_ART = r"""
  ██████╗  █████╗ ███╗   ███╗███████╗
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
 ██║  ███╗███████║██╔████╔██║█████╗  
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
  ██████╗ ██╗   ██╗███████╗██████╗   
 ██╔═══██╗██║   ██║██╔════╝██╔══██╗  
 ██║   ██║██║   ██║█████╗  ██████╔╝  
 ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  
 ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║  
  ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝  
"""

WIN_ART = r"""
 __   __ ___  _   _  __        _____ _   _ _
 \ \ / // _ \| | | | \ \      / /_ _| \ | | |
  \ V /| | | | | | |  \ \ /\ / / | ||  \| | |
   | | | |_| | |_| |   \ V  V /  | || |\  |_|
   |_|  \___/ \___/     \_/\_/  |___|_| \_(_)
"""

# ─────────────────────────────────────────────
#  GAME STATE
# ─────────────────────────────────────────────
class GameState:
    def __init__(self):
        self.health    = 3
        self.inventory = []
        self.score     = 0
        self.name      = "Adventurer"

state = GameState()

# ─────────────────────────────────────────────
#  UTILITY FUNCTIONS
# ─────────────────────────────────────────────
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, delay=0.03, color=''):
    """Print text character-by-character for dramatic effect."""
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause(seconds=0.8):
    time.sleep(seconds)

def hud():
    """Display the heads-up display: HP, score, inventory."""
    hearts    = (C.RED    + "❤ " + C.RESET) * state.health
    deadheart = (C.DARK   + "♡ " + C.RESET) * (3 - state.health)
    print(f"\n{hearts}{deadheart}   "
          f"{C.GOLD}Score: {state.score:,} pts{C.RESET}", end="")
    if state.inventory:
        items = "  |  " + C.CYAN + "  ".join(state.inventory) + C.RESET
        print(items, end="")
    print("\n" + C.DARK + "─" * 60 + C.RESET + "\n")

def get_input(prompt, valid_options):
    """
    BUG FIX: Original used `if x == "A" or "B"` which ALWAYS evaluates True
    because non-empty strings are truthy in Python.
    FIXED:   Normalise to lowercase and check membership properly.
    """
    valid_lower = [opt.lower() for opt in valid_options]
    while True:
        print(C.YELLOW + prompt + C.RESET)
        raw    = input(C.BOLD + "  >>> " + C.RESET).strip()
        choice = raw.lower()                          # normalise case
        if choice in valid_lower:
            return choice
        else:
            opts = " / ".join(valid_options)
            print(C.RED + f"  ⚠  Invalid! Choose: {opts}\n" + C.RESET)

def death_scene(cause, art=""):
    """
    Deduct a life and print the death screen.
    Returns True if the player is completely dead (0 lives left).
    """
    state.health -= 1
    clear()
    if art:
        print(C.RED + art + C.RESET)
    typewrite(f"\n💀  {cause}", delay=0.04, color=C.RED)
    pause(0.8)

    if state.health > 0:
        lives_left = "life" if state.health == 1 else "lives"
        typewrite(f"\n  You have {state.health} {lives_left} remaining... respawning.",
                  color=C.YELLOW)
        pause(1.5)
        return False   # still alive
    else:
        print(C.RED + GAMEOVER_ART + C.RESET)
        typewrite("  All lives lost. The island swallows you whole.", color=C.RED)
        print(f"\n  {C.GOLD}Final Score: {state.score:,} pts{C.RESET}\n")
        pause(2)
        return True    # truly dead

# ─────────────────────────────────────────────
#  INTRO
# ─────────────────────────────────────────────
def intro():
    clear()
    print(C.CYAN + TITLE_ART + C.RESET)
    typewrite("  ⚓   TREASURE ISLAND  ─  The Legend of the Lost Chest   ⚓",
              delay=0.04, color=C.GOLD + C.BOLD)
    typewrite("  " + "─" * 58, color=C.CYAN)
    pause(0.4)

    print(f"\n  {C.WHITE}What is your name, adventurer?{C.RESET}")
    name = input(C.BOLD + "  >>> " + C.RESET).strip()
    state.name = name if name else "Adventurer"

    clear()
    typewrite(f"\n  Welcome, {state.name}. Your legend begins now...", color=C.GREEN)
    pause(0.4)
    typewrite("  An ancient treasure chest is buried on a cursed island.", delay=0.03)
    typewrite("  Hundreds have tried. Zero have returned.", delay=0.03, color=C.RED)
    typewrite("  You have 3 lives. Every choice matters.", delay=0.03, color=C.YELLOW)
    typewrite("  Some paths hide secret items that could save your life.", delay=0.03, color=C.CYAN)
    pause(1)

# ─────────────────────────────────────────────
#  STAGE 1 — The Crossroads
# ─────────────────────────────────────────────
def stage_1():
    while True:
        clear()
        print(C.CYAN + SHIP_ART + C.RESET)
        hud()
        typewrite("  ── STAGE 1: The Crossroads ──", color=C.GOLD + C.BOLD)
        print()
        typewrite("  You stand at a three-way fork in a dense jungle.", delay=0.03)
        typewrite("  LEFT  → A misty forest trail. Birds chirp cautiously.", delay=0.03)
        typewrite("  RIGHT → A road scarred with dragon-claw gouges on every tree.", delay=0.03, color=C.RED)
        typewrite("  FORWARD → A dark cave with glowing eyes deep inside...", delay=0.03, color=C.MAGENTA)

        # ── random encounter ──────────────────
        if random.random() < 0.4:
            print()
            typewrite("  ⚡ A wandering merchant appears!", color=C.YELLOW)
            typewrite('  "Buy a map for 50 gold? It marks the safe door." [yes/no]', color=C.YELLOW)
            ans = get_input("", ["yes", "no"])
            if ans == "yes" and state.score >= 50:
                state.score     -= 50
                state.inventory.append("🗺  Treasure Map")
                typewrite("  The merchant winks and vanishes. Map acquired!", color=C.GREEN)
                pause(0.8)

        choice = get_input("\n  Where do you go? [left / right / forward]",
                           ["left", "right", "forward"])

        if choice == "left":
            state.score += 100
            typewrite("\n  Good instinct. You slip into the forest...", color=C.GREEN)
            pause(0.8)
            return True

        elif choice == "right":
            dead = death_scene(
                f"A dragon erupts from the treeline! {state.name} is turned to cinders."
                " The claw marks were a warning.",
                DRAGON_ART
            )
            if dead:
                return False
            # respawn → loop back

        elif choice == "forward":
            clear()
            print(C.MAGENTA + CAVE_ART + C.RESET)
            typewrite("\n  You step inside... pitch black... then your eyes adjust.", delay=0.04, color=C.MAGENTA)
            pause(1)
            typewrite("  You find an ancient torch and a rusty key left by a past explorer!", color=C.GOLD)
            state.inventory.append("🔦 Torch")
            state.inventory.append("🗝  Rusty Key")
            state.score += 150
            typewrite("  Smart detour. The torch lights your path through the forest.", color=C.GREEN)
            pause(1.2)
            return True

# ─────────────────────────────────────────────
#  STAGE 2 — The Shore
# ─────────────────────────────────────────────
def stage_2():
    while True:
        clear()
        print(C.BLUE + ISLAND_ART + C.RESET)
        hud()
        typewrite("  ── STAGE 2: The Shore ──", color=C.GOLD + C.BOLD)
        print()
        typewrite("  You burst out of the jungle onto a rocky shoreline.", delay=0.03)
        typewrite("  The treasure island floats in the haze, half a mile out.", delay=0.03, color=C.GREEN)
        print()
        typewrite("  SWIM → Brave the open water yourself.", delay=0.03)
        typewrite("  WAIT → Sit tight and see what washes up.", delay=0.03)
        typewrite("  BOAT → Take the leaky rowing boat tied to the dock.", delay=0.03)

        # ── random life jacket event ──────────
        if random.random() < 0.35:
            print()
            typewrite("  ⚡ A fisherman tosses you a life jacket! [take it? yes/no]", color=C.YELLOW)
            ans = get_input("", ["yes", "no"])
            if ans == "yes":
                state.inventory.append("🦺 Life Jacket")
                state.score += 50
                typewrite("  Wise choice.", color=C.GREEN)
                pause(0.6)

        choice = get_input("\n  What do you do? [swim / wait / boat]",
                           ["swim", "wait", "boat"])

        if choice == "swim":
            if "🦺 Life Jacket" in state.inventory:
                typewrite("\n  The life jacket keeps the sharks at bay. You power across!", color=C.GREEN)
                state.score += 150
                pause(0.8)
                return True
            else:
                dead = death_scene(
                    f"A great white erupts from below and drags {state.name} under."
                    " The water runs red. Should've grabbed that jacket.",
                    SHARK_ART
                )
                if dead:
                    return False

        elif choice == "wait":
            typewrite("\n  You sit. You wait. You squint at the horizon...", delay=0.04)
            pause(1.2)
            event = random.choice(["rescue_boat", "dolphin", "tide"])
            if event == "rescue_boat":
                typewrite("  A captain pulls up: 'Need a lift?' You're on the island in minutes.", color=C.GREEN)
                state.score += 200
                pause(0.8)
                return True
            elif event == "dolphin":
                typewrite("  A dolphin surfaces, chatters at you, and somehow guides you across. Nature is wild.", color=C.CYAN)
                state.score += 250
                pause(0.8)
                return True
            else:
                dead = death_scene(
                    f"The tide surges — a rogue wave sweeps {state.name} out to sea."
                    " Patience has its limits.",
                    SHARK_ART
                )
                if dead:
                    return False

        elif choice == "boat":
            typewrite("\n  You untie the creaking boat and start rowing hard...", delay=0.04)
            pause(1)
            if random.random() < 0.4:
                typewrite("  The hull splits! Water floods in fast!", color=C.RED)
                if "🦺 Life Jacket" in state.inventory:
                    typewrite("  Your life jacket kicks in — you doggy-paddle to the island. Embarrassing. Effective.", color=C.GREEN)
                    state.score += 80
                    return True
                else:
                    dead = death_scene(
                        f"The boat sinks. {state.name} sinks with it."
                        " Should've checked the hull.",
                        SHARK_ART
                    )
                    if dead:
                        return False
            else:
                typewrite("  You make it across! The island looms ahead.", color=C.GREEN)
                state.score += 175
                pause(0.8)
                return True

# ─────────────────────────────────────────────
#  STAGE 3 — The Guardian's Riddle
# ─────────────────────────────────────────────
def stage_3():
    while True:
        clear()
        hud()
        typewrite("  ── STAGE 3: The Guardian's Riddle ──", color=C.GOLD + C.BOLD)
        print()
        typewrite("  You step onto the island. The air smells of old gold and danger.", delay=0.03)
        typewrite("  A stone altar blocks the path forward. A riddle is carved into it:\n", delay=0.03)
        typewrite('  "I speak without a mouth, hear without ears,', delay=0.04, color=C.CYAN)
        typewrite('   I have no body, but I come alive with the wind."', delay=0.04, color=C.CYAN)
        print()
        typewrite("   A) A Shadow", delay=0.03)
        typewrite("   B) An Echo", delay=0.03)
        typewrite("   C) A Flame", delay=0.03)

        choice = get_input("\n  🧠 Answer the riddle: [a / b / c]", ["a", "b", "c"])

        if choice == "b":
            typewrite("\n  ✅  CORRECT.  The altar shudders and slides aside.", color=C.GREEN)
            state.score += 250
            pause(0.5)
            if "🗝  Rusty Key" in state.inventory:
                typewrite("  Your rusty key catches the light — it unlocks a hidden side chest!", color=C.GOLD)
                state.score += 300
                state.inventory.append("💎 Ancient Gem")
                typewrite("  Ancient Gem acquired. This might be useful later...", color=C.CYAN)
            pause(1)
            return True
        else:
            typewrite("\n  ❌  WRONG.  The ground trembles. A zombie guardian rises!", color=C.RED)
            print(C.RED + ZOMBIE_ART + C.RESET)

            if "🗝  Rusty Key" in state.inventory:
                typewrite("  The key glows and repels the spirit — narrowly!", color=C.GOLD)
                typewrite("  The key crumbles to dust. One-time protection, now gone.", color=C.YELLOW)
                state.inventory.remove("🗝  Rusty Key")
                typewrite("  You may answer again...", color=C.CYAN)
                pause(1)
                # let them try again — loop continues
            else:
                dead = death_scene(
                    f"The zombie horde tears {state.name} apart."
                    " The island is unforgiving to the ignorant.",
                    ZOMBIE_ART
                )
                if dead:
                    return False

# ─────────────────────────────────────────────
#  STAGE 4 — The Final Door
# ─────────────────────────────────────────────
def stage_4():
    while True:
        clear()
        hud()
        typewrite("  ── STAGE 4: The Final Door ──", color=C.GOLD + C.BOLD)
        print()
        typewrite("  Three doors stand at the end of a long torchlit corridor.", delay=0.03)
        typewrite("  The treasure lies behind exactly one. The others are traps.", delay=0.03, color=C.RED)
        print()
        print(f"  {C.RED}🔴  RED DOOR{C.RESET}    — scorched edges, reeking of sulfur")
        print(f"  {C.YELLOW}🟡  YELLOW DOOR{C.RESET} — scratched with claw marks and bullet holes")
        print(f"  {C.BLUE}💙  BLUE DOOR{C.RESET}   — etched with ocean waves, a gemstone slot at its centre")

        if "🗺  Treasure Map" in state.inventory:
            typewrite("\n  📍 Your map has a red X over the BLUE DOOR — that's it!", color=C.GOLD)
        if "💎 Ancient Gem" in state.inventory:
            typewrite("  ✨ Your ancient gem pulses near the BLUE DOOR's slot...", color=C.CYAN)

        choice = get_input("\n  🚪 Choose your door: [red / yellow / blue]",
                           ["red", "yellow", "blue"])

        if choice == "red":
            dead = death_scene(
                f"A wall of fire explodes outward! {state.name} is incinerated instantly."
                " The sulfur was a dead giveaway.",
                FIRE_ART
            )
            if dead:
                return False

        elif choice == "yellow":
            dead = death_scene(
                f"A horde of zombie guards floods the corridor!"
                f" {state.name} is overwhelmed in seconds."
                " Those claw marks should've told you everything.",
                ZOMBIE_ART
            )
            if dead:
                return False

        elif choice == "blue":
            if "💎 Ancient Gem" in state.inventory:
                typewrite("\n  You slot the gem in. The door GLOWS. It swings open silently.", color=C.GOLD)
                state.score += 200
            else:
                typewrite("\n  The door is locked... but the hinges are old. You shoulder it open.", color=C.CYAN)
            pause(1)
            return True

# ─────────────────────────────────────────────
#  VICTORY SCREEN
# ─────────────────────────────────────────────
def victory():
    clear()
    print(C.GOLD + TREASURE_ART + C.RESET)
    typewrite(WIN_ART, color=C.GOLD)
    pause(0.5)

    # bonuses
    bonus_msg = []
    if state.health == 3:
        state.score += 1000
        bonus_msg.append(f"  {C.GOLD}🏆 FLAWLESS — no deaths:     +1,000 pts{C.RESET}")
    if "💎 Ancient Gem" in state.inventory:
        state.score += 500
        bonus_msg.append(f"  {C.CYAN}💎 Ancient Gem bonus:         +500 pts{C.RESET}")
    if "🔦 Torch" in state.inventory:
        state.score += 100
        bonus_msg.append(f"  {C.YELLOW}🔦 Torch collector bonus:     +100 pts{C.RESET}")

    if bonus_msg:
        typewrite("\n  ── Bonus Points ──", color=C.GOLD)
        for msg in bonus_msg:
            print(msg)

    typewrite(f"\n  🎉  Congratulations, {state.name.upper()}! You found the treasure!", color=C.GOLD)
    print()
    typewrite(f"  Final Score   : {state.score:,} pts", color=C.GOLD)
    typewrite(f"  Lives Left    : {'❤ ' * state.health}{'♡ ' * (3 - state.health)}", color=C.RED)
    typewrite(f"  Items Found   : {len(state.inventory)}", color=C.CYAN)

    # rank
    print()
    if state.score >= 2500:
        rank, col = "🥇  LEGENDARY TREASURE HUNTER", C.GOLD
    elif state.score >= 1800:
        rank, col = "🥈  MASTER ADVENTURER", C.YELLOW
    elif state.score >= 1200:
        rank, col = "🥉  SKILLED EXPLORER", C.WHITE
    else:
        rank, col = "🏅  BRAVE SOUL", C.CYAN
    typewrite(f"  Rank          : {rank}", color=col)
    typewrite("\n  The legend of the island grows by one more name...", color=C.MAGENTA)
    pause(2)

# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────
def play_again():
    print(f"\n  {C.YELLOW}Play again? [yes / no]{C.RESET}")
    ans = input(C.BOLD + "  >>> " + C.RESET).strip().lower()
    return ans == "yes"

def main():
    global state
    while True:
        state = GameState()   # fresh state each run
        intro()

        stages = [stage_1, stage_2, stage_3, stage_4]
        survived = True

        for stage in stages:
            if not stage():
                survived = False
                break

        if survived:
            victory()

        if not play_again():
            break

    typewrite("\n  Thanks for playing Treasure Island. ⚓\n", color=C.CYAN)

if __name__ == "__main__":
    main()
