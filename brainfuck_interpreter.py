import argparse
from functions import clean_code, create_bracket_shifts, execute

parser = argparse.ArgumentParser(description='Brainfuck interpreter')
parser.add_argument('--path', type=str, help='Path to brainfuck file')
args = parser.parse_args()

def interpret():
    try:
        file = args.path
        with open(file, 'r') as f:
            txt = f.read()
            correct_sequence = clean_code(txt)
            shifts = create_bracket_shifts(correct_sequence)
            execute(correct_sequence, shifts)

    except FileNotFoundError as e:
        print('No such file or directory: ' + e.filename)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    interpret() 