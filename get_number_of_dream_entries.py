def get_day_lines(lines):
    fname = 'dreams_copy.txt'
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

    dates = []
    for line in lines:
        split = line.split(',')
        if len(split) > 2:
            day, month, year = split[:3]
            has_day = [True if d in day.lower() else False for d in days]
            has_month = [True if m in month.lower() else False for m in months]
            if any(has_day) and any(has_month):
                dates.append(line)

    return dates

if __name__ == "__main__":
    with open('dreams_copy.txt', 'r') as f:
        lines = f.readlines()
        dates = get_day_lines(lines)
        print len(dates)
