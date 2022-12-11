import datetime as dt
from datetime import date
import PySimpleGUI as sg

date_format = '%Y-%m-%d'
date_choice = dt.date(date.today().year, 1, 1)  # initial date object
date_choice_str = date_choice.strftime(date_format)  # initial date str
Ymd = (date_choice.year, date_choice.month, date_choice.day)  # Tuple of Ymd (for popup get date)

layout = [[sg.T('Chose a date')],
          [sg.Input(date_choice_str, size=(10, 1), key='-DATE-'), sg.Button('Calender')],
          [sg.Ok(), sg.Exit()]]

window = sg.Window('Date selector', layout)


def Cal_popup(a):
    # initialize date popup with date choice as default. Store choice (tuple) to mdY
    mdY = sg.popup_get_date(start_year=Ymd[0], start_mon=Ymd[1], start_day=Ymd[2])
    if mdY:  # If a date is chosen in popup, update input
        popup_date = dt.date(mdY[2], mdY[0], mdY[1]).strftime(date_format)
        window['-DATE-'](popup_date)


def Check_date(a):
    try:  # check if date is valid; if so => True, else False
        dt.datetime.strptime(a, date_format)
        return True
    except ValueError:
        sg.popup('Wrong date format', 'Try again')
        return False


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Calender':
        Cal_popup(Ymd)
    elif event == 'Ok':
        if Check_date(values['-DATE-']):  # If date is OK: update input; else loop again
            sg.popup(f"You have chosen {values['-DATE-']} as date", title='Conformation')
            break
        else:
            continue

window.close()
