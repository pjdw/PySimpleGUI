# CalendarButton and Popup_get_date in PySimpleGUI
In this repository you find some basic programmes for choosing a date with [PySimpleGUI](https://www.pysimplegui.org/en/latest/).  
I started with `CalendarButton` button. After selecting a date with the button, I could not get focus on the edit window (see my post on [github](https://github.com/PySimpleGUI/PySimpleGUI/issues/6083)).
The crazy thing was if cmd-Tab twice, focus is back. This is a bit inconvenient, so I tried `popug_get_date`. I used on extra function but focus is ok now.


### Build up program:
- importing libraries 
- Declaring variables (mainly dates)
- Defining the layout
- Defining a window and reading this in an event loop

### Two functions:
1. Fire up the popup get date and store the output
2. Check if date in input field is OK.

That's really all.


My default value for the date string is `%Y-%m-%d`. If you wish you can change the corresponding variable. Keep in mind that the popup returns a tuple in the form of `m, d, Y`. First I convert this to a date object and then to a string (see the popup function).

NB: you can also enter the date directly in the input field.

If ok is pressed then date is validated and if OK,  value is confirmed. Else date error is displayed and you can try agian.

#### Personal note:
I took me some time to figure out how to match the input field with the output of the popup. My first thought was to update the corresponding key in the value dictionary, but it didn't work out. Finally I discoverd `window['-KEY']` and that did the trick.
