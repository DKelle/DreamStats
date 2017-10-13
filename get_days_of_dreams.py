from get_number_of_dream_entries import get_day_lines

def main():
    with open('dreams_copy.txt', 'r') as f:
        lines = f.readlines()
        dates = get_day_lines(lines)
        for date in dates:
            print date

if __name__ == "__main__":
    main()
