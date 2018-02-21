from telebot import types
import calendar

def create_calendar(year, month):
    markup = types.InlineKeyboardMarkup()
    #First row - Month and Year
    row=[]
    row.append(types.InlineKeyboardButton(calendar.month_name[month]+" "+str(year),callback_data="ignore"))
    markup.row(*row)
    #Second row - Week Days
    week_days=["M","T","W","R","F","S","U"]
    row=[]
    for day in week_days:#для кожного дня тижня
        row.append(types.InlineKeyboardButton(day, callback_data="ignore"))#створити кнопку
    markup.row(*row)#додати рядок "M","T","W","R","F","S","U"
    my_calendar = calendar.monthcalendar(year, month)
    print(my_calendar)
    for week in my_calendar:#[[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 0, 0, 0, 0]]
        row=[]
        for day in week:#[0, 0, 0, 1, 2, 3, 4]
            if(day==0):
                row.append(types.InlineKeyboardButton(" ",callback_data="ignore"))#при зворотньомцу виклику повертажться "ignore"
            else:
                row.append(types.InlineKeyboardButton(str(day),callback_data="calendar-day-"+str(day)))#при зворотньому виклику повертався "calendar-day-13"
        markup.row(*row)#[ ,  ,  , 1, 2, 3, 4]
    #Last row - Buttons
    row=[]
    row.append(types.InlineKeyboardButton("<",callback_data="previous-month"))
    row.append(types.InlineKeyboardButton(" ",callback_data="ignore"))
    row.append(types.InlineKeyboardButton(">",callback_data="next-month"))
    markup.row(*row)
    return markup



def create_watch(hours, minut):
    markup = types.InlineKeyboardMarkup()
    row = []
    row.append(types.InlineKeyboardButton("▲", callback_data="hours_inc"))
    row.append(types.InlineKeyboardButton("▲", callback_data="minut_inc"))
    markup.row(*row)
    row = []
    row.append(types.InlineKeyboardButton(str(hours) if int(hours)>=10 else "0"+str(hours),
                                          callback_data="hours"))
    row.append(types.InlineKeyboardButton(str(minut) if int(minut)>=10 else "0"+str(minut),
                                          callback_data="minutes"))
    markup.row(*row)
    row = []
    row.append(types.InlineKeyboardButton("▼", callback_data="hours_dec"))
    row.append(types.InlineKeyboardButton("▼", callback_data="minut_dec"))
    markup.row(*row)
    return markup