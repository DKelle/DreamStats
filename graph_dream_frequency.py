from get_datetimes import get_datetimes
from datetime import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.io as pio

def init_ploty():
    api_key = open('plotly_apikey.secret', 'r').readline().rstrip().lstrip()
    username = open('plotly_username.secret', 'r').readline().rstrip().lstrip()
    plotly.tools.set_credentials_file(username=username, api_key=api_key)

    orcapath = open('orcapath.secret', 'r').readline().rstrip().lstrip()
    plotly.io.orca.config.executable = orcapath
    plotly.io.orca.config.save()

def create_graph(freq):
    # Add credentials... fuck plotly
    init_ploty()

    months = [f[0] for f in freq]
    data = [f[1] for f in freq]

    # Create and style traces
    line = go.Scatter(
        x = months,
        y = data,
        name = 'Dream frequency by month',
        line = dict(
            color = ('rgb(205, 12, 24)'),
            width = 4)
    )
    data = [line]

    # Edit the layout
    layout = dict(title = 'Number of dreams per month',
                    xaxis = dict(title = 'Month'),
                    yaxis = dict(title = 'Number of dreams'),
                    autosize=False,
                    width=2000,
                    height=700,
                  )

    fig = dict(data=data, layout=layout)
    pio.write_image(fig, 'frequency.png')
    print ('run "open frequency.png" to see the graph!')

def get_frequency_by_month(dates):
    # Freq is a list of the format [('jan', 6), ('feb', 18) ...]
    freq = []

    # Keep track of the current month... Staring at October is a bit of hack. I know this is when dreams start
    prev_month = 'Oct 2014'

    # Keep count of number of dreams for the current month
    count = 0
    for date in dates:
        month = date.strftime("%b %Y")

        # If we are still in the same month, then we have another dream in this month
        if month == prev_month:
            count = count + 1
        else:
            # We are in a new month. Add the previous month to our list
            freq.append((prev_month, count))

            # We are entering a new month. If we have just gone from January to December
            # Make sure to add 0s for the months in between
            prev_month_id = int(datetime.strptime(prev_month, '%b %Y').strftime('%m'))
            cur_month_id = int(date.strftime('%m'))
            if not prev_month_id + 1 == cur_month_id:
                for i in range(prev_month_id+1, 13):
                    skipped_month = datetime.strptime(str(i), '%m')
                    skipped_month = '{} {}'.format(skipped_month.strftime('%b'), prev_month.split()[-1])
                    freq.append((skipped_month, 0))
                for i in range(1, cur_month_id):
                    skipped_month = datetime.strptime(str(i), '%m')
                    skipped_month = '{} {}'.format(skipped_month.strftime('%b'), month.split()[-1])
                    freq.append((skipped_month, 0))

            # Reset the count for the next month
            count = 1

        prev_month = month


    # We probably didn't append data for the last month, so append it
    freq.append((prev_month, count))
    print ('here is the freq {}'.format(freq))
    return freq

if __name__ == "__main__":
    print("Make sure to run with python3!")
    datetimes = get_datetimes()
    freq = get_frequency_by_month(datetimes)

    create_graph(freq)

    """
       _____   __    __                 __  .__
      /  _  \_/  |__/  |_  ____   _____/  |_|__| ____   ____
     /  /_\  \   __\   __\/ __ \ /    \   __\  |/  _ \ /    \
    /    |    \  |  |  | \  ___/|   |  \  | |  (  <_> )   |  \
    \____|__  /__|  |__|  \___  >___|  /__| |__|\____/|___|  /
            \/                \/     \/                    \/

    ATTENTION: We are using plotly as our graphing API. They force you to have an account to ues the API.
    Fuck them, that is stupid as hell. But anway, if you are experiencing bugs, it may be related to this,
    so look into that first.

    Next, plotly has all kinds of weird dependencies in order to output static images like pngs.
    I had to install coda (a package manager for python to install non-python libs), which I used to
    install orca (idk, I guess plotly needs this). We also had to manucally set the path to the orca binary.
    Look in init_plotly

    I believe that this code does not depend on having coda installed (in fact, we actually isntall minicoda, no coda)
    So if something messes up with coda eventually we should be okay.
    It does however depend on orca, which can be found at <orcapath.txt>.
    Check to make sure we still have this here if we start seeing bugs in the future
    """
