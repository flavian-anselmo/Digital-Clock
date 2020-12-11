"""
A digital clock 
->made this project when leaning about the date time module
->I used the pytz module to get different time zones 
->A user can change the time zone by selecting a time zone from the drop down list
->the default timezone used is 'Africa/Nairobi'->
j=0
for i in pytz.common_timezones:
    j+=1
    if i=='Africa/Nairobi':
        break 
print(j-1,i)
Run the above code to get the timezone that 'Africa/Nairobi' belongs
"""
from tkinter import *
from tkinter.font import Font#get the desired font
import datetime
from datetime import datetime
import pytz

win = Tk()
win.title("Digital Clock")
win.geometry("310x200")
win.resizable(False,False)
#current_time = datetime.now(pytz.timezone('Africa/Djibouti')) # get the current time
def my_digital_clock():
    current_time = datetime.now(pytz.timezone(timezone_list.get())) # get the current time from the drop_down list
    time_display=current_time.strftime('%H:%M:%S')
    digital_time_lb.config(text=time_display,fg="red")#updates the label to the current time
    day_display=datetime.now()
    day_display=current_time.strftime('%B,%d:%Y')
    print(str(day_display))
    digital_DAY_lb.config(text=day_display,fg="green")
    #print(timezone_list.set(str(pytz.common_timezones[0])))
    #used strftime() to format the display of the current time
    #%H->hours
    #%M->minutes
    #%s->seconds
    #%B->month name
    #%Y->year
    #%d->day
    #change the time after a specific millisecond
    win.after(80,my_digital_clock)
    
my_font = Font(size=100)
#display the time
digital_time_lb = Label(win,font=("Times new roman",30))
digital_time_lb.pack()
#display the day/month/Year
digital_DAY_lb = Label(win,font=("Times new roman",30))
digital_DAY_lb.pack()
 
timezone_list=StringVar()
#set the default time zone for Nairobi
zone=timezone_list.set(str(pytz.common_timezones[42]))#default timezone is 'Africa/Nairobi'(42)
#used the OptionMenu()->function
drop_down=OptionMenu(win,timezone_list,*pytz.common_timezones)
drop_down.pack()

my_digital_clock()#function call
win.mainloop()
"""
add a label to dislay the time on our screen
the time should change at a pecific time
->display the time zone 
->choose the time zone and display the time
"""
"""
.config()->used to update the label
win.config(text="change")

"""