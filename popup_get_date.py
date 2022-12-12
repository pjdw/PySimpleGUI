import datetime as dt
from datetime import date
import PySimpleGUI as sg

DATE_FORMAT = '%Y-%m-%d'
DATE_CHOICE = dt.date(date.today().year, 1, 1)  # initial date object
DATE_CHOICE_STR = DATE_CHOICE.strftime(DATE_FORMAT)  # initial date str
ymd = (DATE_CHOICE.year, DATE_CHOICE.month, DATE_CHOICE.day)  # Tuple of ymd (for popup get date)
sg.set_options(font=('Helvetica Neue', 14))

layout = [[sg.T('Chose a date')],
          [sg.Input(DATE_CHOICE_STR, size=(10, 1), key='-DATE-'), sg.Button('Calender')],
          [sg.Ok(), sg.Exit()]]

window = sg.Window('Date selector', layout)


def cal_popup():
    # initialize date popup with date choice as default. Store choice (tuple) to mdy
    mdy = sg.popup_get_date(start_year=ymd[0], start_mon=ymd[1], start_day=ymd[2])
    if mdy:  # If a date is chosen in popup, update input
        popup_date = dt.date(mdy[2], mdy[0], mdy[1]).strftime(DATE_FORMAT)
        window['-DATE-'](popup_date)  # set input to popup


def check_date(a):
    try:  # check if date is valid; if so => True, else False
        dt.datetime.strptime(a, DATE_FORMAT)
    except ValueError:
        sg.popup('Wrong date format', 'Try again')
        return False
    else:
        return True


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Calender':
        cal_popup()
    elif event == 'Ok':
        if check_date(values['-DATE-']):  # If date is OK: update input; else loop again
            sg.popup(f"You have chosen {values['-DATE-']} as date", title='Conformation')
            break
        else:
            continue

window.close()
