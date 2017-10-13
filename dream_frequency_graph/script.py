import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from get_number_of_dream_entries import get_day_lines
import matplotlib.pyplot as plt
import re

def get_formatted_date(date):
    # eg. input (\tFirday, March 19, 2016)
    split = date.split(',')
    day = "".join(split[0].split())
    month = "".join(split[1].split()[0].split())
    year = "".join(split[2].split())
    return (day, month, year)
    # eg. return value: (Thursday, March, 2016)

def get_formatted_dates(dates):
    # Format every date on which a dream occured
    formatted_dates = [get_formatted_date(date) for date in dates]
    return formatted_dates

def get_month_diff(fdate, ldate):
    # Get the number of months between two dates
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    f_month, f_year = fdate[1:]
    l_month, l_year = ldate[1:]
    f_index = months.index(f_month.lower())
    l_index = months.index(l_month.lower())
    month_diff = l_index - f_index
    year_diff = int(l_year) - int(f_year)
    number_of_months = 12*year_diff + month_diff
    return number_of_months

def init_date_counts(first_date, last_date):
    # Create an array of 0s
    # index 14 means 14 months after October 2014 (date of first dream)
    number_of_months = get_month_diff(first_date, last_date)
    date_counts = [0] * (number_of_months + 1)
    return date_counts

def get_counts(count, dates):
    # Make a list of how many dreams happened in each month
    first = dates[0]
    for date in dates:
        month_diff = get_month_diff(first, date)
        count[month_diff] += 1

def create_graph(counts):
    # Finally graph these counts
    plt.plot(counts)
    plt.ylabel('Occurances per month')
    plt.xlabel('Months since october 2014')
    plt.show()

def main():
    with open('../dreams_copy.txt', 'r') as f:
        lines = f.readlines()
        dates = get_day_lines(lines)

    if dates:
        # Change strip the numeric day, and white space from all dates
        formatted_dates = get_formatted_dates(dates)

        # Create a list full of X 0s.
        # Where X is the number of months since the journal was created
        counts = init_date_counts(formatted_dates[0], formatted_dates[-1])

        # Actually fill this count list with the number of dreams in each month
        get_counts(counts, formatted_dates)

        # Graph these counts
        create_graph(counts)

if __name__ == "__main__":
    main()
