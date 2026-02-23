import os, time, sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.03):
    for char in text:
        sys.stdout.write(char); sys.stdout.flush(); time.sleep(speed)
    print()

def ultimate_ui_toolkit():
    while True:
        clear()
        print(f"\033[96m{'ID':<4} | {'STYLE NAME':<18} | {'PREVIEW'}\033[0m\n" + "═" * 55)
        menu = [
            ("1", "Simple Line", "----------"), ("2", "Thick Bar", "██████████"),
            ("3", "Pattern", "~*~*~*~*~*"), ("4", "Centered Text", "--- TITLE ---"),
            ("5", "Fancy Box", "╔═════════╗"), ("6", "Empty Spaces", "Word    Word"),
            ("7", "Unlimited Table", "| A | B | C |"), ("8", "Simple Box", "[  TEXT  ]"),
            ("9", "Typewriter", "T..y..p..i..n..g"), ("10", "Loading Bar", "[████░░░░░░]"),
            ("11", "Rainbow Line", "RED-YEL-GRN-BLU")
        ]
        for i, name, pre in menu:
            print(f"{i:<4} | {name:<18} | {pre}\n" + "-" * 55)
        
        choice = input("Pick a style (1-11) or 'q': ").strip().lower()
        if choice == 'q': break
        if choice not in [str(x) for x in range(1, 12)]:
            input("\n\033[91m[!] ERROR: Invalid ID. Press Enter...\033[0m"); continue
        clear()

        if choice == "1":
            c, n = input("Char: "), int(input("How many? "))
            print(f"\n[ RESULT ]\n{c*n}\n\n[ THE CODE ]\nprint('{c}' * {n})")
        elif choice == "2":
            n = int(input("Blocks: "))
            print(f"\n[ RESULT ]\n{'█'*n}\n\n[ THE CODE ]\nprint('█' * {n})")
        elif choice == "3":
            p, n = input("Pattern: "), int(input("Repeats: "))
            print(f"\n[ RESULT ]\n{p*n}\n\n[ THE CODE ]\nprint('{p}' * {n})")
        elif choice == "4":
            t, w, f = input("Text: "), int(input("Width: ")), input("Filler: ")
            print(f"\n[ RESULT ]\n{t.center(w, f)}\n\n[ THE CODE ]\nprint('{t}'.center({w}, '{f}'))")
        elif choice == "5":
            t = input("Text: "); w = len(t) + 2
            print(f"\n[ RESULT ]\n╔{'═'*w}╗\n║ {t} ║\n╚{'═'*w}╝")
            print(f"\n[ THE CODE ]\nprint(f'╔{{\"═\"*{w}}}╗\\n║ {t} ║\\n╚{{\"═\"*{w}}}╝')")
        elif choice == "6":
            w1, w2, g = input("W1: "), input("W2: "), int(input("Gap: "))
            print(f"\n[ RESULT ]\n{w1}{' '*g}{w2}\n\n[ THE CODE ]\nprint('{w1}' + (' ' * {g}) + '{w2}')")
        elif choice == "7":
            cols = input("Cols: ").split()
            h = "| " + " | ".join([f"{c:<10}" for c in cols]) + " |"
            d = "| " + " | ".join(["-"*10 for _ in cols]) + " |"
            print(f"\n[ RESULT ]\n{h}\n{d}\n\n[ THE CODE ]\ncols={cols}\nprint('| ' + ' | '.join([f'{{c:<10}}' for c in cols]) + ' |')")
        elif choice == "8":
            t = input("Text: ")
            print(f"\n[ RESULT ]\n[  {t.upper()}  ]\n\n[ THE CODE ]\nprint(f'[  {{ \"{t}\".upper() }}  ]')")
        elif choice == "9":
            m = input("Message: "); print("\n[ RESULT ]"); typewriter(m)
            print(f"\n[ THE CODE ]\nimport time, sys\nfor c in '{m}': sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.05)")
        elif choice == "10":
            print("\n[ SIMULATING ]")
            for i in range(11):
                b = "█"*i + "░"*(10-i); print(f"\rProgress: [{b}] {i*10}%", end=""); time.sleep(0.1)
            print(f"\n\n[ THE CODE ]\n import time\n for i in range(11):\n    b = '█'*i + '░'*(10-i)\n    print(f'\\rProgress: [{{b}}] {{i*10}}%', end=''); time.sleep(0.1)")
        elif choice == "11":
            rb = ["\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m"]
            print("\n[ RESULT ]")
            for i in range(30): print(f"{rb[i%5]}█", end="")
            print("\033[0m\n\n[ THE CODE ]\n rb={rb}\nfor i in range(30): print(f'{{rb[i%5]}}█', end='')\n FOR ALL THE CODE LOOK AT THE BOTTOM OF THE CODE")
        
        input("\n\n" + "="*40 + "\nPress [ENTER] to return...")

ultimate_ui_toolkit()

# [█] 

# [░]

# N = Number

#1
#print("F"*N)

#2
#print("█"*N)

#3
#print('F' * N)

#4
#print('text' . center(14, '-'))

#5
#print(f"╔{'═'* Number }╗\n| Text |\n╚{'═'* Number}╝")


#6
#print('text' + ( ' * N) + "Text')

#7
#cols=['text', 'text', ...]
#print('| ' + '|' .join([f'{c:<10}' for c in cols] + ' \'))

#8
#print(f'[ { "text".upper{} } ]')

#9
#import time, sys
#for c in 'text': sys.stdout.write(c); s9ys.stdout.flush(); time.sleep(0.05)

#10
#import time
#for i in range(11):
#    b =  b = '█'*i + '░'*(10-i)
#    print(f'\rProgress. [{b}] {i*10}%', end=''); time.sleep(0.1)

#11
#rb = ["\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m"]
#rb={rb}
#for i in range(30): print(f'{{rb[1%5]}}█', end=)
