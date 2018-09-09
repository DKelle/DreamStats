from get_number_of_dream_entries import get_day_lines

def get_dreams():
    with open('dreams_copy.txt', 'r') as f:
        lines = f.readlines()
    day_lines = get_day_lines(lines)

    dreams = []
    for line in lines:
        if line not in day_lines and len(line) > 1:
            dreams.append(line)
    return dreams

if __name__ == "__main__":
    print(get_dreams())
