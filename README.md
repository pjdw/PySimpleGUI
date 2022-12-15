# CalendarButton and Popup_get_date in PySimpleGUI
In this repository you find some basic programmes for choosing a date with [PySimpleGUI](https://www.pysimplegui.org/en/latest/).  
I started with `CalendarButton` button.  
When selecting a date with the button and returning to main window, I could not get focus on the edit field (see my post on [github](https://github.com/PySimpleGUI/PySimpleGUI/issues/6083)).  
The crazy thing was with cmd-Tab twice, focus is back. This is a bit inconvenient.  
If a date is selected from the calendar button, this is displayed in input.  
I did not figured out yet how to sync the input value with the calendar button date at launch. **If anybody has ideas . . .** 

I also gave `popup_get_date` a try. I had to use on extra function to start the popup, but no focus problems and button and input are in sync both ways. Think I stick with that one.

**Personal note:**
I took me some time to figure out how to match the input field with the output of the popup. My first thought was to update the corresponding key in the value dictionary, but it didn't work out. Finally I discoverd `window['-KEY-']` and that did the trick.
