import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.uix
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.core.window import Window
from forex_python.converter import CurrencyRates

import pandas as pd


class MainWindow(Screen):
    pass

class LengthWindow(Screen):

    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["m", "mm", "cm", "km", "in", "ft", "yd", "mile"],
             'Conversion': [1, 10 ** (-3), 10 ** (-2), 10 ** 3, 0.0254, 0.3048, 0.9144, 1609.344]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use meter as default unit
        if start_unit is "Unit":
            start_unit = "m"
            self.ids.Unit_select.text = "m"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,10)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnint, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnint: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnint, "Conversion"))
        return finalVal

class WeightWindow(Screen):
    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["kg", "g", "mg", "ton", "ton-US", "ton-UK", "lb", "oz"],
             'Conversion': [1, 0.001, 0.000001, 1000, 0907.18474, 1016.04691, 0.4535924, 0.0311035]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use meter as default unit
        if start_unit is "Unit":
            start_unit = "kg"
            self.ids.Unit_select.text = "kg"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue  # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,10)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnit, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnit: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnit, "Conversion"))
        return finalVal

class TimeWindow(Screen):
    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["second", "ms", "minute", "hour", "day", "week", "month", "year"],
             'Conversion': [1, 10 ** (-3), 60, 3600, 86400, 604800, 2592000, 31560000]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use second as default unit
        if start_unit is "Unit":
            start_unit = "second"
            self.ids.Unit_select.text = "second"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,10)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnit, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnit: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnit, "Conversion"))
        return finalVal

class SpeedWindow(Screen):
    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["m/s", "km/s", "km/h", "mps", "mph", "knot", "mach", "c"],
             'Conversion': [1, 1000, 0.2777778, 1609.34398, 0.44704, 0.5144444, 340, 343]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use meter as default unit
        if start_unit is "Unit":
            start_unit = "m/s"
            self.ids.Unit_select.text = "m/s"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue  # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,6)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnit, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnit: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnit, "Conversion"))
        return finalVal

class VolumeWindow(Screen):

    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["l", "ml", "m³", "gallon(US)", "gallon(UK)", "fl.oz(US)", "fl.oz(UK)", "bbl(barrel)"],
             'Conversion': [1, 10 ** (-3), 1000, 3.7854, 4.54609, 0.02957344, 0.02841306, 158.9873]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use liter as default unit
        if start_unit is "Unit":
            start_unit = "l"
            self.ids.Unit_select.text = "l"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,10)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnit, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnit: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnit, "Conversion"))
        return finalVal

class DataWindow(Screen):

    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["MB", "bit", "B", "KB", "GB", "TB", "kbit/s", "Mbit/s", "Gbit/s"],
             'Conversion': [1, 1/1024 ** 2/8, 1/1024 ** 2, 1/1024, 1024, 1024**2, 1/8388.608, 1/8.388608, 1/0.0083886]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use meter as default unit
        if start_unit is "Unit":
            start_unit = "MB"
            self.ids.Unit_select.text = "MB"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,10)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnint, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnint: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnint, "Conversion"))
        return finalVal

class TemperatureWindow(Screen):
    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["°C", "K", "°F"],
             'Conversion': [1, 1, 1.8],
             'Offset': [0, 273.15, 32]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        conTable = {"K":{"°C":"{}-273.15",
                         "°F":"({}*1.8-459.67)",
                         "K":"{}"},
                    "°C":{"°C":"{}",
                          "°F":"{} * 1.8 + 32",
                          "K":"{}+273.15"},
                    "°F":{"°C":"({}-32)/1.8",
                          "°F":"{}",
                          "K":"({}+459.67)/1.8"}}

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use meter as default unit
        if start_unit is "Unit":
            start_unit = "°C"
            self.ids.Unit_select.text = "°C"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            first_char = element.text[0]
            # skip negative sign
            if first_char is '-':
                first_char = element.text[1]
            is_number = first_char.isnumeric()
            if is_number:
                element.text = str(last_result)
                continue  # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnit, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnit: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """
        val = float(val)
        equation = conTable[StartUnit][ConUnit]
        finalVal = eval(equation.format(val))

        return finalVal

class AreaWindow(Screen):

    def do_conversion(self):
        """ Converts user input via conversion table into different units"""

        # Setup conversion table in pandas
        d = {'Unit': ["m²", "mm²", "cm²", "a", "ha", "km²", "in²", "yd²", "ft²"],
             'Conversion': [1, 10 ** (-6), 10 ** (-4), 10 ** 2,10 ** 4, 10 ** 6, 1/1550.0031, 1/1.19599,  1/10.7639104]}
        conTable = pd.DataFrame(data=d)
        conTable.index = conTable["Unit"]
        del conTable["Unit"]

        # Check if user input is a number
        input_number = self.ids.calc_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False

        # Get start unit from unit spinner
        start_unit = self.ids.Unit_select.text
        # Use meter as default unit
        if start_unit is "Unit":
            start_unit = "m²"
            self.ids.Unit_select.text = "m²"

        # Temporary variable for later label assignment
        last_result = None

        for element in self.children[0].children:

            # Skip elements that are not type label
            if type(element) is not kivy.uix.label.Label:
                continue

            # Check if first index is a number and thus the label is a number label
            is_number = element.text[0].isnumeric()
            if is_number:
                element.text = str(last_result)
                continue # skip number lables

            # Only unit labels will be present here
            # Therefore the element text must be the unit of the conversion
            con_unit = element.text
            # Remove label description. E.g. "m (meter)"
            if " " in con_unit:
                con_unit = con_unit[:con_unit.index(" ")]

            last_result = self.convert(input_number, start_unit, con_unit, conTable)
            last_result = round(last_result,10)
            print(f"Results: {last_result} {con_unit}")

    def convert(self, val, StartUnit, ConUnint, conTable):
        """
        Converts the value from the starting unit to the destination unit using the conversion table
        :param val: value as float
        :param StartUnit: string of starting unit
        :param ConUnint: string of destination unit
        :param conTable: pandas dataframe conversion table
        :return:
        """

        siVal = val * float(conTable._get_value(StartUnit, "Conversion"))
        finalVal = siVal / float(conTable._get_value(ConUnint, "Conversion"))
        return finalVal

class CurrenciesWindow(Screen):
    def converter(self):
        exchange_from = self.ids.input_1.text
        exchange_to = self.ids.input_2.text
        self.ids.curr_output.text = self.ids.input_2.text
        input_number = self.ids.curr_input.text
        input_number = input_number.replace(",", ".")
        try:
            input_number = float(input_number)
        except:
            print("Input is not a number")
            return False
        c = CurrencyRates
        input_1 = exchange_from
        input_2 = exchange_to
        amount = float(input_number)
        c = CurrencyRates()
        currency = c.get_rate(input_1, input_2)
        value = float(currency) * amount
        value = round(value, 2)
        self.ids.value_1.text = str(value)
        print(value)

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

class MyMainApp(App):
    def build(self):
        Window.size = (720, 800)
        Window.clearcolor = (0.06222222, 0.13333333, 0.26666666, 0.7)
        kv = Builder.load_file("my.kv")
        return kv

if __name__ == "__main__":
    MyMainApp().run()