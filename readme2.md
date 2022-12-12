This program lets you chose a date; that simple.
It uses [PySimpleGUI](https://www.pysimplegui.org/en/latest/). In this case I use `popup_get_date`. 

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
