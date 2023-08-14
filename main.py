import tkinter as tk
from tkinter import ttk
import threading
import time
import keyboard
import ctypes

# ctypes for faster clicking
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010

def fast_click(button):
    if button == 'left':
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    elif button == 'right':
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

class ZeroClicker:

    def __init__(self, root):
        self.clicking = False
        self.cps_count = 0
        self.setup_gui(root)

    def setup_gui(self, root):
        ttk.Label(root, text="Mouse Button:").grid(row=0, column=0, padx=5, pady=5)
        self.mouse_var = tk.StringVar(value='left')
        ttk.Combobox(root, textvariable=self.mouse_var, values=['left', 'right', 'middle']).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Interval (ms):").grid(row=1, column=0, padx=5, pady=5)
        self.time_var = tk.DoubleVar(value=1000)
        time_entry = ttk.Entry(root, textvariable=self.time_var)
        time_entry.grid(row=1, column=1, padx=5, pady=5)
        time_entry.bind('<Return>', self.update_interval)

        ttk.Label(root, text="Hotkey (Start/Stop):").grid(row=2, column=0, padx=5, pady=5)
        self.hotkey_var = tk.StringVar(value='l')
        hotkey_entry = ttk.Entry(root, textvariable=self.hotkey_var)
        hotkey_entry.grid(row=2, column=1, padx=5, pady=5)
        hotkey_entry.bind('<Return>', self.set_hotkey)

        self.info_var = tk.StringVar(value="Press the hotkey to start/stop!")
        ttk.Label(root, textvariable=self.info_var).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.cps_var = tk.StringVar(value="CPS: 0")
        ttk.Label(root, textvariable=self.cps_var).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.hotkey = keyboard.add_hotkey(self.hotkey_var.get(), self.toggle_clicking)

    def update_interval(self, event=None):
        try:
            value = max(0, float(self.time_var.get()))
            self.time_var.set(value)
        except ValueError:
            self.time_var.set(1000)

    def set_hotkey(self, event=None):
        keyboard.remove_hotkey(self.hotkey)
        self.hotkey = keyboard.add_hotkey(self.hotkey_var.get(), self.toggle_clicking)

    def click_mouse(self):
        while self.clicking:
            fast_click(self.mouse_var.get())
            self.cps_count += 1
            if self.time_var.get() > 0:
                time.sleep(self.time_var.get() / 1000)

    def toggle_clicking(self):
        if self.clicking:
            self.stop_clicking()
        else:
            self.start_clicking()

    def start_clicking(self):
        self.clicking = True
        threading.Thread(target=self.click_mouse, daemon=True).start()
        self.info_var.set("Clicking... Press the hotkey to stop.")
        root.after(1000, self.update_cps_label)

    def stop_clicking(self):
        self.clicking = False
        self.info_var.set("Press the hotkey to start clicking!")

    def update_cps_label(self):
        if self.clicking:
            self.cps_var.set(f"CPS: {self.cps_count}")
            self.cps_count = 0
            root.after(1000, self.update_cps_label)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Zero Clicker')
    root.iconbitmap('Icon.ico')
    ZeroClicker(root)
    root.mainloop()
