from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from plyer import notification

class Interface(MDBoxLayout):
    mini_sec=0
    sec=0
    minuts=0
    run =False
    def timer(self,*args):
        Interface.mini_sec+=10
        if Interface.mini_sec==100:
            Interface.mini_sec=0
            Interface.sec+=1
            if Interface.sec==60:
                Interface.sec=0
                Interface.minuts+=1
        self.ids.displaytimer.text="{0:0=2d}".format(Interface.minuts)+" : "+"{0:0=2d}".format(Interface.sec)+" : "+"{0:0=2d}".format(Interface.mini_sec)
    def start_timer(self):
        print("Starting")
        if Interface.run==False:
            Clock.schedule_interval(self.timer,1/10)
            Interface.run=True
            self.ids.mdicon.icon='timer-pause-outline'
            self.ids.progrss.start()

        else:
            Clock.unschedule(self.timer)
            Interface.run = False
            self.ids.mdicon.icon = 'timer-play-outline'
            self.ids.progrss.stop()
            notification.notify(title="Timer Duration", message= "fdafdf")

class Custombutton(ButtonBehavior,CommonElevationBehavior,MDAnchorLayout):
    pass

class TimerApp(MDApp):
    def changetheme(self,appbar):
        if self.theme_cls.theme_style=='Light':
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.primary_palette = "Amber"
            appbar.right_action_items= [["weather-sunny", lambda x:self.changetheme(appbar)]]
        else:
            self.theme_cls.primary_palette = "Purple"
            self.theme_cls.theme_style = "Light"
            appbar.right_action_items = [["weather-night", lambda x: self.changetheme(appbar)]]

    def build(self):
        self.theme_cls.primary_palette="Purple"
        self.theme_cls.theme_style="Light"

TimerApp().run()