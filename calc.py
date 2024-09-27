import math
import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("480x624+20+20")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

        def iExit():
            iExit = tk.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
            if iExit>0:
                self.window.destroy()
            return
        
        def destroy():
            button1.destroy()
            button2.destroy()
            button3.destroy()
            button4.destroy()
            button5.destroy()
            button6.destroy()
            button7.destroy()
            button8.destroy()
            button9.destroy()
            button0.destroy()
        def Scientific():
            self.window.resizable(width=False, height=False)
            self.window.geometry("990x624+20+20")
            self.create_mod_button()
            self.create_cos_button()
            self.create_sin_button()
            self.create_tan_button()
            self.create_e_button()
            self.create_pi_button()
            self.create_neg_button()
            self.create_inv_button()
            self.create_log_button()
            self.create_loge_button()
            self.create_clear_button()
            self.create_equals_button()
            self.create_square_button()
            self.create_sqrt_button()

        def Standard():
            self.window.resizable(width=False, height=False)
            self.window.geometry("480x624+20+20")
            self.create_clear_button()
            self.create_equals_button()
            self.create_square_button()
            self.create_sqrt_button()
            destroy()


        menubar = tk.Menu()
        self.window.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "File", menu=filemenu)
        filemenu.add_command(label = "Standard", command =Standard)

        filemenu.add_command(label = "Scientific", command = Scientific)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = iExit)
        

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()


    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_total_label()
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_total_label()
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def log(self):
        self.current_expression = str(eval(f"math.log10({self.current_expression})"))
        self.update_total_label()
        self.update_label()
    def create_log_button(self):
        global button1 
        button1= tk.Button(self.buttons_frame, text="log", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.log)
        button1.grid(row=0, column=5, sticky=tk.NSEW)

    def loge(self):
        self.current_expression = str(eval(f"math.log({self.current_expression})"))
        self.update_total_label()
        self.update_label()
    def create_loge_button(self):
        global button2
        button2 = tk.Button(self.buttons_frame, text="ln", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.loge)
        button2.grid(row=1, column=5, sticky=tk.NSEW)

    def inv(self):
        self.current_expression = str(eval(f"1/{self.current_expression}"))
        self.update_total_label()
        self.update_label()
    def create_inv_button(self):
        global button3
        button3 = tk.Button(self.buttons_frame, text="inv", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.inv)
        button3.grid(row=2, column=5, sticky=tk.NSEW)

    def mod(self):
        self.current_expression = str(eval(f"abs({self.current_expression})"))
        self.update_total_label()
        self.update_label()
    def create_mod_button(self):
        global button4
        button4 = tk.Button(self.buttons_frame, text="| |", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.mod)
        button4.grid(row=3, column=5, sticky=tk.NSEW)

    def negate(self):
        self.current_expression = str(eval(f"-{self.current_expression}"))
        self.update_total_label()
        self.update_label()
    def create_neg_button(self):
        global button5
        button5 = tk.Button(self.buttons_frame, text="±", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.negate)
        button5.grid(row=4, column=5, sticky=tk.NSEW)

    def sin(self):
        value = str(eval(f"round(math.sin({self.current_expression}),4)"))
        self.current_expression = str(value)
        self.update_total_label()
        self.update_label()
    def create_sin_button(self):
        global button6
        button6 = tk.Button(self.buttons_frame, text="sin", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.sin)
        button6.grid(row=0, column=6, sticky=tk.NSEW)

    def cos(self):
        value = str(eval(f"round(math.cos({self.current_expression}),4)"))
        self.current_expression = str(value)
        self.update_total_label()
        self.update_label()
    def create_cos_button(self):
        global button7
        button7 = tk.Button(self.buttons_frame, text="cos", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.cos)
        button7.grid(row=1, column=6, sticky=tk.NSEW)
    
    def tan(self):
        value = str(eval(f"round(math.tan({self.current_expression}),4)"))
        self.current_expression = str(value)
        self.update_total_label()
        self.update_label()
    def create_tan_button(self):
        global button8
        button8= tk.Button(self.buttons_frame, text="tan", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.tan)
        button8.grid(row=2, column=6, sticky=tk.NSEW)

    def e(self):
        self.current_expression += str(math.e)
        self.update_total_label()
        self.update_label()
    def create_e_button(self):
        global button9
        button9 = tk.Button(self.buttons_frame, text="𝑒", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.e)
        button9.grid(row=3, column=6, sticky=tk.NSEW)

    def pi(self):
        self.current_expression += str(math.pi)
        self.update_total_label()
        self.update_label()
    def create_pi_button(self):
        global button0
        button0 = tk.Button(self.buttons_frame, text="π", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,padx=24,
                           borderwidth=0, command=self.pi)
        button0.grid(row=4, column=6, sticky=tk.NSEW)

    
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
