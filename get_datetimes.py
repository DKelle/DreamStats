from datetime import datetime
from get_number_of_dream_entries import get_day_lines

def get_datetimes():
    datetimes = []
    with open('dreams_copy.txt', 'r') as f:
        lines = f.readlines()
        dates = get_day_lines(lines)


    for date in dates:
        date = date.lstrip().rstrip()
        try:
            datetimes.append(datetime.strptime(date, '%A, %B %d, %Y'))
        except Exception as e:
            print 'Hit exception while converting the following date: {}'.format(date)
            print e

    return datetimes

def main():
    dates = get_datetimes()
    for d in dates:
        print d

if __name__ == "__main__":
    main()
