import datetime as dt
from datetime import date
import PySimpleGUI as sg

init_date = dt.date(date.today().year, 1, 1)                                       # initial date for input field
DATE_FORMAT = '%Y-%m-%d'                                                           # Date format for conversion etc

sg.set_options(font=('Helvetica Neue', 14))

# layout with text, input field, calendar button and OK/Exit
layout = [[sg.T('Date: '), sg.I(init_date, key='-DATE-', s=(9, 1)), sg.B(button_text='Calendar', key='-CAL-')],
          [sg.Ok(), sg.Exit()]]

window = sg.Window('Calendar', layout)


def popup_cal(a):
    if check_date(a):                                                             # check if input is valid date string
        a = dt.datetime.strptime(a, DATE_FORMAT).timetuple()                      # convert to date tuple for popup
        mdY = sg.popup_get_date(start_year=a[0], start_mon=a[1], start_day=a[2])  # store output from popup
        if mdY:                                                                   # If date selected . . .
            popup_date = dt.date(mdY[2], mdY[0], mdY[1]).strftime(DATE_FORMAT)    # convert and store . . .
            window['-DATE-'](popup_date)                                          # update (key from input field)


def check_date(a):
    try:                                                                          # check if date is valid
        dt.datetime.strptime(a, DATE_FORMAT)
    except ValueError:                                                            # confirm non valid date
        sg.popup('Wrong date format', 'Try again')
        return False
    else:                                                                         # date is valid
        return True


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):                                          # chosen to exit/close
        sg.popup(f'Existing ...{chr(10)}Until next time')
        break
    elif event == '-CAL-':                                                        # pressed the calendar button
        popup_cal(values['-DATE-'])                                               # popup function with input content
    elif event == 'Ok':
        if check_date(values['-DATE-']):                                          # If date is OK: confirm and break
            sg.popup(f"You have chosen {values['-DATE-']} as date", title='Conformation')
            break
        else:                                                                     # date not valid; loop again
            continue
