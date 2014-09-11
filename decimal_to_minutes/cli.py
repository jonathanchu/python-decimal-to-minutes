from decimal import Decimal
from math import floor
import sys

import click


@click.command()
@click.argument('time', required=True)
def main(time):
    """Converts a decimal to minutes."""
    time_hours = Decimal(time)
    time_minutes = time_hours * 60
    time_seconds = time_minutes * 60

    hours_part = floor(time_hours % 60)
    minutes_part = floor(time_minutes % 60)
    seconds_part = floor(time_seconds % 60)

    click.echo("{h}:{m}:{s}".format(
        h=int(hours_part),
        m=int(minutes_part),
        s=int(seconds_part),
    ))
