import datetime as dt
from datetime import date
import PySimpleGUI as sg

DATE_FORMAT = '%Y-%m-%d'
INITIAL_DATE = dt.date(date.today().year, 1, 1)  # initial date object
INITIAL_DATE_STR = INITIAL_DATE.strftime(DATE_FORMAT)  # initial date str
MDY = (INITIAL_DATE.month, INITIAL_DATE.day, INITIAL_DATE.year,)  # Tuple of MDY (for CalendarB)
sg.set_options(font=('Helvetica Neue', 14))

layout = [[sg.T('Chose a date')],
          [sg.I(INITIAL_DATE_STR, size=(10, 1), key='-DATE-'),
           sg.CalendarButton("Calendar", target='-DATE-', default_date_m_d_y=MDY, format = DATE_FORMAT)],
          [sg.Ok(), sg.Exit()]]

window = sg.Window('Date selector', layout)


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
    # elif event == 'Calender':
    #     cal_popup()
    elif event == 'Ok':
        if check_date(values['-DATE-']):  # If date is OK: update input; else loop again
            sg.popup(f"You have chosen {values['-DATE-']} as date", title='Conformation')
            break
        else:
            continue

window.close()
