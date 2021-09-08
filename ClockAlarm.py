#use user input to set alarm to on or off


class Alarm_Clock:
    def __init__(self):
        self.is_on_or_off = False
        self.current_time = 0
        self.alarm_time = 0


    def turn_alarm_on_off(self):

        print("alarm clock says hi")
        button = input("Do you want to set alarm to on or off? Type on or off")
        if button == "on":
            self.is_on_or_off = True
            print("You turned on the alarm clock")
        elif button == "off":
            self.is_on_or_off = False
            print("The alarm clock is currently shut down")
            exit()
        else:
            self.turn_alarm_on_off()

    def set_current_time(self):
        print("time to set our current time")
        self.current_time = int(input("Input current time military style"))
        print(self.current_time)

    def set_alarm(self):
        print("below is the current time")
        print(self.current_time)
        alarm_button = int(input("time to set the alarm using military time"))
        if alarm_button == self.current_time:
            print("ALARM ALARM ALARM  TIME TO WAKE UP")
        else:
            print("sleepy time")