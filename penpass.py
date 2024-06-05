import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

class ballSlider(tk.Canvas):
    def __init__(self, parent, from_=8, to=20, **kwargs):
        super().__init__(parent, **kwargs)
        self.from_ = from_
        self.to = to
        self.value = from_
        self.radius = 10
        self.width = 300
        self.height = 100

        self.config(width=self.width, height=self.height)

        self.line = self.create_line(20, self.height // 2, self.width - 20, self.height // 2, fill="#BD93F9", width=2)
        self.circle = self.create_oval(20 - self.radius, (self.height // 2) - self.radius, 20 + self.radius, (self.height // 2) + self.radius, fill="#50FA7B", outline="#50FA7B")
        self.value_text = self.create_text(20, self.height // 2 - 20, text=str(self.from_), fill="#F8F8F2", font=("Open Sans Semibold", 12))

        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<Button-1>", self.on_click)

    def on_drag(self, event):
        self.update_slider(event.x)

    def on_click(self, event):
        self.update_slider(event.x)

    def update_slider(self, x):
        x = max(20, min(x, self.width - 20))
        self.coords(self.circle, x - self.radius, (self.height // 2) - self.radius, x + self.radius, (self.height // 2) + self.radius)
        self.value = self.from_ + (x - 20) / (self.width - 40) * (self.to - self.from_)
        self.coords(self.value_text, x, self.height // 2 - 20)
        self.itemconfig(self.value_text, text=str(int(self.value)))

    def get_value(self):
        return int(self.value)

class checkBox(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.upperVar = tk.BooleanVar()
        self.lowerVar = tk.BooleanVar()
        self.specialVar = tk.BooleanVar()
        self.numbersVar = tk.BooleanVar()

        self.upperCheck = ttk.Checkbutton(self, text="Uppercase Letters 'A-Z'", variable=self.upperVar, style="Custom.TCheckbutton")
        self.lowerCheck = ttk.Checkbutton(self, text="Lowercase Letters 'a-z'", variable=self.lowerVar, style="Custom.TCheckbutton")
        self.specialCheck = ttk.Checkbutton(self, text="Special Characters '@-$'", variable=self.specialVar, style="Custom.TCheckbutton")
        self.numbersCheck = ttk.Checkbutton(self, text="Numbers '0-9'", variable=self.numbersVar, style="Custom.TCheckbutton")

        self.upperCheck.pack(padx=10, pady=5, anchor="w")
        self.lowerCheck.pack(padx=10, pady=5, anchor="w")
        self.specialCheck.pack(padx=10, pady=5, anchor="w")
        self.numbersCheck.pack(padx=10, pady=5, anchor="w")

def generate_password(length, use_upper, use_lower, use_special, use_numbers):
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_special:
        special_characters = "!@#$%^&*()"
        character_pool += special_characters
    if use_numbers:
        character_pool += string.digits

    if not character_pool:
        return None  # Return None if no character type is selected

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def copy_to_clipboard(text_widget):
    win.clipboard_clear()
    win.clipboard_append(text_widget.get("1.0", "end-1c"))
    win.update()

def ui():
    global win
    win = tk.Tk()
    win.title("PenPass Secure")
    win.geometry("400x600")
    win.config(bg="#282A36")

    style = ttk.Style()
    style.configure('TLabel', background="#282A36", foreground="#F8F8F2", font=("Open Sans Bold", 20))
    style.configure('TButton', background="#8BE9FD", foreground="#282A36")
    style.configure('Custom.TCheckbutton', background="#282A36", foreground="#F8F8F2")
    style.configure('TFrame', background="#282A36")
    style.map('Custom.TCheckbutton',
              background=[('active', '#282A36'), ('selected', '#282A36')],
              foreground=[('active', '#F8F8F2'), ('selected', '#F8F8F2')],
              indicatorcolor=[('selected', '#50FA7B')])
    style.map('TButton', background=[('active', '#50FA7B')], foreground=[('active', '#282A36')])

    win_label = ttk.Label(win, text="Password Options", style='TLabel')
    win_label2 = ttk.Label(win, text="Please Select at Least One", style='TLabel', font=("Open Sans", 12))
    win_label.pack(padx=10, pady=10)
    win_label2.pack(padx=10, pady=10)

    checkbox_frame = checkBox(win, bg="#282A36")
    checkbox_frame.pack(padx=10, pady=10)

    slide_label = ttk.Label(win, text="Password Length", style='TLabel', background="#282A36", foreground="#F8F8F2", font=("Open Sans", 16))
    slide_label.pack(padx=10, pady=10)

    custom_slider = ballSlider(win, from_=8, to=20, bg="#282A36", highlightthickness=0)
    custom_slider.pack(padx=10, pady=10)

    def on_generate():
        length = custom_slider.get_value()
        use_upper = checkbox_frame.upperVar.get()
        use_lower = checkbox_frame.lowerVar.get()
        use_special = checkbox_frame.specialVar.get()
        use_numbers = checkbox_frame.numbersVar.get()

        if not (use_upper or use_lower or use_special or use_numbers):
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = generate_password(length, use_upper, use_lower, use_special, use_numbers)
        password_box.delete("1.0", tk.END)
        if password:
            password_box.insert(tk.END, password)

    button = ttk.Button(win, text="Generate", style='TButton', command=on_generate)
    button.pack(padx=10, pady=10)

    password_frame = ttk.Frame(win, style="TFrame")
    password_frame.pack(padx=10, pady=10, fill='x')

    password_box = tk.Text(password_frame, height=1, width=30, font=("Open Sans", 12), bg="#282A36", fg="#F1FA8C", highlightthickness=0)
    password_box.pack(side='left', padx=(0, 5), pady=10, fill='x', expand=True)

    copy_button = ttk.Button(password_frame, text="Copy", style='TButton', command=lambda: copy_to_clipboard(password_box))
    copy_button.pack(side='left', padx=(5, 0), pady=10)

    trademark_label = ttk.Label(win, text="Created by Joshua Duane", style='TLabel', background="#282A36", foreground="#44475A", font=("Open Sans", 8))
    trademark_label.pack(side='bottom', pady=10)

    win.mainloop()

if __name__ == "__main__":
    ui()
