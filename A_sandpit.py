import os, time

def clear():
    """Wipes the terminal screen clean."""
    # 'nt' is the internal name for Windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise, it's Mac or Linux
    else:
        os.system('clear')

clear()


first = "apple"
secound = "banana"

print(f"Frist: {first} | Secound {secound}")

first, secound = secound, first

print("I've sewiched thing around....")
print(f"Frist: {first} | secound {secound}")


text = "Hello"

# Center with default space padding
centered_text_spaces = text.center(20)
print(f"'{centered_text_spaces}'")
# Output: '       Hello        '

# Center with a specific fill character (e.g., '*')
centered_text_asterisks = text.center(20, '*')
print(f"'{centered_text_asterisks}'")
# Output: '*******Hello********'


title = "MY APP"
sub = "v1.0"

# Center both while printing, no extra variables needed
print(f"""
{title:^30}
{sub:^30}
This part is normal left-aligned text.
It stays exactly where it starts.
""")

lines = ["Menu", "Options", "Exit", "Help"]

# Center the first 2, join with the rest
print("\n".join([line.center(20) for line in lines[:2]] + lines[2:]))

for i in range(11):
    b =  b = '█'*i + '░'*(10-i)
    print(f'\rProgress. [{b}] {i*10}%', end=''); time.sleep(0.1)

print("\n\033[93m   GAME END\033[0m",)

print('Game History'.center(18, '-'))
clear()