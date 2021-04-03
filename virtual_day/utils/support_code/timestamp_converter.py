from virtual_day.utils import constants


def convert_datetime_with_short_month(datetime) -> str:
    result_datetime = datetime.strftime(
            f'%d {constants.MONTHS[int(datetime.strftime("%m")) - 1][1]} %Y')
    return result_datetime


def convert_datetime_with_hours_short(datetime) -> str:
    result_datetime = datetime.strftime(
            f'%d {constants.MONTHS[int(datetime.strftime("%m")) - 1][1]} %Y %H:%M')
    return result_datetime


def convert_datetime_with_long_month(datetime) -> str:
    result_datetime = datetime.strftime(
            f'%d {constants.MONTHS[int(datetime.strftime("%m")) - 1][2]} %Y')
    return result_datetime


def convert_datetime_with_hours_long(datetime) -> str:
    result_datetime = datetime.strftime(
            f'%d {constants.MONTHS[int(datetime.strftime("%m")) - 1][2]} %Y %H:%M')
    return result_datetime
