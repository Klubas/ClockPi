import time
import Adafruit_CharLCD as LCD

class Screen:
    def __init__(self, env='pi'):
       self.lcd = None
       self.config_screen()
       current_date = time.strftime('%a %b %d, 20%y')
       current_time = time.strftime('%H:%M:%S')
       self.lcd.message(current_date + '\n' + current_time)
    
    def config_screen(self):
        lcd_rs        = 25 
        lcd_en        = 24
        lcd_d4        = 23
        lcd_d5        = 17
        lcd_d6        = 18
        lcd_d7        = 22
        lcd_backlight = 4
        lcd_columns   = 16
        lcd_rows      = 2
        
        self.lcd = LCD.Adafruit_CharLCD(
            lcd_rs
            , lcd_en
            , lcd_d4
            , lcd_d5
            , lcd_d6
            , lcd_d7
            , lcd_columns
            , lcd_rows
            , lcd_backlight
        )
        
        self.lcd.home()
        self.lcd.clear()
        self.lcd.autoscroll(False)

    def auto_update_time(self):
        pass

if __name__ == '__main__':
    screen = Screen()


