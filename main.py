import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.size = (720, 1800)

class MainWindow(Screen):
    pass

class LengthWindow(Screen):
    pass

class WeightWindow(Screen):
    pass

class TimeWindow(Screen):
    pass

class SpeedWindow(Screen):
    pass

class VolumeWindow(Screen):
    pass

class DataWindow(Screen):
    pass

class TemperatureWindow(Screen):
    pass

class AreaWindow(Screen):
    pass

class CurrenciesWindow(Screen):
    pass

class CalculatorWindow(Screen):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if "Error" in prior:
            prior = ""
        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
        self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        # add + to textbox
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
    pass

class WindowManager(ScreenManager):
    pass

class P(FloatLayout):
    pass




kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (0.06222222, 0.13333333, 0.26666666, 0.7)
        return kv


if __name__ == "__main__":
    MyMainApp().run()