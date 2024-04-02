from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def calculate(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            operator = instance.text

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    self.result_label.text = "Error: Divide by zero"
                    return

            self.result_label.text = "Result: " + str(result)
        except ValueError:
            self.result_label.text = "Error: Invalid input"

    def build(self):
        layout = GridLayout(cols=2)

        self.num1_input = TextInput(hint_text="Enter number 1")
        layout.add_widget(self.num1_input)

        self.num2_input = TextInput(hint_text="Enter number 2")
        layout.add_widget(self.num2_input)

        operators = ['+', '-', '*', '/']
        for operator in operators:
            button = Button(text=operator)
            button.bind(on_press=self.calculate)
            layout.add_widget(button)

        self.result_label = Label(text="Result:")
        layout.add_widget(self.result_label)

        return layout


if __name__ == '__main__':
    CalculatorApp().run()