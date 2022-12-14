# Some code to select a date GUI-style
These programmes let you chose a date. 
It uses [PySimpleGUI](https://www.pysimplegui.org/en/latest/). I used both `CalendarButton` and `popup_get_date`.


### Build up program:
- importing libraries 
- Declaring variables (mainly dates)
- Defining the layout
- Defining a window and reading this in an event loop

### Two functions:
1. Check if date in input field is OK.
2. When `popup_get_date` is used I use an additional function to start the popup.

That's really all.

My default format for the date string is `%Y-%m-%d`. If you wish you can change the corresponding variable.  
Keep in mind that the popup returns a tuple in the form of `m, d, Y`. First I convert this to a date object and then to a string (see the popup function).

If ok is pressed in the main window, date is validated and if OK, value is confirmed. Else date error is displayed, and you can try again.

NB: You don't have to use the button; you can also enter the date directly in the input field. But then it needs to be checked.


#### Personal note:
I took me some time to figure out how to match the input field with the output of the popup.  
My first thought was to update the corresponding key in the value dictionary, but it didn't work out.  
Finally, I discoverd `window['-KEY']` and that did the trick.
