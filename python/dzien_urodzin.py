import datetime
import calendar

def translation(day_name):

    match day_name:
        case 'Monday':
            return 'Poniedziałek'
        case 'Tuesday':
            return 'Wtorek'
        case 'Wednesday':
            return 'Środa'
        case 'Thursday':
            return 'Czwartek'
        case 'Friday':
            return 'Piątek'
        case 'Saturday':
            return 'Sobota'
        case 'Sunday':
            return 'Niedziela'
        

date_of_birth = input("Podaj swoją datę urodzin w formacie dzień-miesiąc-rok (np. 01-01-1999): ")
day, month, year = date_of_birth.split("-")

date_of_birth = datetime.datetime(int(year), int(month), int(day))

#print(date_of_birth.weekday())

date_name = calendar.day_name[date_of_birth.weekday()]

day_name = calendar.day_name[date_of_birth.weekday()]
print(translation(day_name))

