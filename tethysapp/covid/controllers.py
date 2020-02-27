import datetime as dt
from django.shortcuts import render
from tethys_sdk.gizmos import PlotlyView
from tethys_sdk.permissions import login_required


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

    line_plot_view = PlotlyView(
        height='500px',
        width='500px',
        template='plotly_dark',
        engine='highcharts',
        title='Plot Title',
        subtitle='Plot Subtitle',
        spline=True,
        x_axis_title='Date',
        x_axis_units='days',
        y_axis_title='Count',
        series=[
            {
                'name': 'Mainland China',
                'color': '#FFA500',
                'data': [
                    [0, 5], [10, 10],
                    [20, 15], [30, 30],
                    [40, 50],
                    [50, 70], [60, 100],
                    [70, 130], [80, 150]
                ]
            },
            {
                'name': 'Other',
                'color': '#FFFF00',
                'data': [
                    [0, 0], [10, 2],
                    [20, 4], [30, 6],
                    [40, 10],
                    [50, 15], [60, 20],
                    [70, 24], [80, 26]
                ]
            },
            {
                'name': 'Recovered',
                'color': '#008000',
                'data': [
                    [0, 0], [10, .25],
                    [20, 1], [30, 2],
                    [40, 3],
                    [50, 5], [60, 7],
                    [70, 10], [80, 14]
                ]
            }
        ]
    )

    context = {
        'total_confirmed': total_confirmed,
        'total_deaths': total_deaths,
        'total_recovered': total_recovered,
        'last_updated': last_updated,
        'conf_by_region': conf_by_region,
        'death_by_region': death_by_region,
        'recov_by_region': recov_by_region,
        'plot_view': line_plot_view,
    }

    return render(request, 'covid/home.html', context)