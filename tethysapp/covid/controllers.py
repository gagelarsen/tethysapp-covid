import datetime as dt
from django.shortcuts import render
from tethys_sdk.gizmos import PlotlyView
from tethys_sdk.permissions import login_required

from datetime import datetime
import plotly.graph_objs as go

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    total_confirmed = 81128
    total_deaths = 2765
    total_recovered = 30257
    last_updated = dt.datetime.now()
    conf_by_region = [
        (78064, "Mainland China"),
        (1261, "South Korea"),
        (691, "Others"),
        (322, "Italy"),
        (178, "Japan")
    ]

    death_by_region = [
        (78064, "Mainland China"),
        (1261, "South Korea"),
        (691, "Others"),
        (322, "Italy"),
        (178, "Japan")
    ]

    recov_by_region = [
        (78064, "Mainland China"),
        (1261, "South Korea"),
        (691, "Others"),
        (322, "Italy"),
        (178, "Japan")
    ]

    x_ = []

    x_ = [datetime(year=2013, month=10, day=x) for x in range(1, 21)]

    mainland = [6 * x for x in range(0, 20)]
    recover = [3 * x for x in range(0, 20)]
    other = [2 * x for x in range(0, 20)]

    my_plotly_view = PlotlyView([
        go.Scatter(x=x_, y=mainland),
        go.Scatter(x=x_, y=recover),
        go.Scatter(x=x_, y=other),
    ])

    context = {
        'total_confirmed': total_confirmed,
        'total_deaths': total_deaths,
        'total_recovered': total_recovered,
        'last_updated': last_updated,
        'conf_by_region': conf_by_region,
        'death_by_region': death_by_region,
        'recov_by_region': recov_by_region,
        'plot_view': my_plotly_view,
    }

    return render(request, 'covid/home.html', context)