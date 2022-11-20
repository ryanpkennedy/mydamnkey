white_notes = [char for char in 'abcdefgABCDEFG']
sharps = [note+'#' for note in white_notes]
flats = [note+'b' for note in white_notes]
allowed_notes = white_notes + sharps + flats

note_nums_dict = {
    0: ['c', 'C', 'b#', 'B#'],
    1: ['c#', 'C#', 'db', 'Db'],
    2: ['d', 'D'],
    3: ['d#', 'D#', 'eb', 'Eb'],
    4: ['e', 'E', 'fb', 'Fb'],
    5: ['f', 'F', 'e#', 'E#'],
    6: ['f#', 'F#', 'gb', 'Gb'],
    7: ['g', 'G'],
    8: ['g#', 'G#', 'ab', 'Ab'],
    9: ['a', 'A'],
    10: ['a#', 'A#', 'bb', 'Bb'],
    11: ['b', 'B', 'cb', 'Cb'],
}

keys_dict = {
    'C Major': [0,2,4,5,7,9,11],
    'Db Major': [],
    'D Major': [],
    'Eb Major': [],
    'E Major': [],
    'F Major': [],
    'Gb Major': [],
    'G Major': [],
    'Ab Major': [],
    'A Major': [],
    'Bb Major': [],
    'B Major': [],
}

example_notes = 'A B C D E'.split(' ')
example_key = 'C Major'

def validate_notes(notes):
    for note in notes:
        if note not in allowed_notes:
            return False
    return True

def convert_to_numbers(notes):
    notes_num_array = []
    for note in notes:
        for note_num in note_nums_dict:
            if note in note_nums_dict[note_num]:
                notes_num_array.append(note_num)
    return notes_num_array

def test_key(notes, key):
    for note in notes:
        if note not in keys_dict[key]:
            return False
    return True

def find_keys(notes):
    possible_keys = []
    for key in keys_dict:
        if test_key(notes, key):
            possible_keys.append(key)
    return possible_keys

def print_keys(keys_list):
    print('the possible keys are: ', keys_list)


def main_search_notes():
    user_notes = input("enter notes you are playing: ").split(' ')
    if validate_notes(user_notes):
        user_notes_nums = convert_to_numbers(user_notes)
        result_keys = find_keys(user_notes_nums)
        print_keys(result_keys)
    else:
        print('You entered an invalid note, try again')
        main_search_notes()

main_search_notes() 
