HISTORY_FILE = 'history.txt'

def show_history():
    try:
        file = open(HISTORY_FILE, 'r')
        lines = file.readlines()
        file.close()
        
        if len(lines) == 0:
            print('No history found.')
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print('No history file found.')

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print('History Cleared')

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + ' = ' + str(result) + '\n')
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Please enter in the format: number operator number')
        return
    
    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid number format.")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2        
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print('Error: Division by zero is not allowed.')
            return
        result = num1 / num2
    else:
        print('Invalid operator. Please use +, -, *, or /')
        return

    if result == int(result):
        result = int(result)

    print(f'Result: {result}')
    save_to_history(user_input, result)

def main():
    print('__ Simple Calculator (type history, clear or exit) __')

main()

while True:
    user_input = input('Enter calculation (+, -, *, /) or command: history, clear, exit: ').strip().lower()
    
    if user_input == 'exit':
        print('Goodbye!')
        break
    elif user_input == 'history':
        show_history()
    elif user_input == 'clear':
        clear_history()
    else:
        calculate(user_input)
