import customtkinter as ctk
import tkinter as tk
import keyboard
import src.gui.frames.frame as Frame

import ctypes


class AutoClickerFrame(Frame.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, "auto_clicker", 300, 275)

        parent.title("Auto Click")

        # Variables
        self.border_windows = []
        self.interval = 5.0
        self.random_interval = 1.0
        self._start = False
        self.border_visible = True


        # Interval
        # -----------------
        self.interval_frame = ctk.CTkFrame(self)
        self.interval_frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(self.interval_frame, text="Interval: ").pack(side="left", padx=5)
        self.interval_value = ctk.CTkLabel(self.interval_frame, text=f"{str(self.interval)}s")
        self.interval_value.pack(side="right", padx=5)
        
        def slider_event(value):
            self.interval = value
            self.interval_value.configure(text=f"{f"{self.interval:.1f}"}s")
        
        self.interval_slider = ctk.CTkSlider(self, from_=0.1, to=30, number_of_steps=155, command=slider_event)
        self.interval_slider.pack(fill="x", padx=10, pady=5)
        self.interval_slider.set(self.interval)

        # Randomize Range Interval
        # -----------------
        self.interval_random = ctk.CTkFrame(self)
        self.interval_random.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(self.interval_random, text="Randomize Range: ").pack(side="left", padx=5)
        self.interval_random_value = ctk.CTkLabel(self.interval_random, text=f"{str(self.random_interval)}s")
        self.interval_random_value.pack(side="right", padx=5)
        
        def slider_event(value):
            self.random_interval = value
            self.interval_random_value.configure(text=f"{f"{self.random_interval:.1f}"}s")
        
        self.interval_random_slider = ctk.CTkSlider(self, from_=0, to=30, number_of_steps=155, command=slider_event)
        self.interval_random_slider.pack(fill="x", padx=10, pady=5)
        self.interval_random_slider.set(self.random_interval)
        # -----------------

        # Border
        # -----------------
        self.border_frame = ctk.CTkFrame(self)
        self.border_frame.pack(fill="x", padx=10, pady=5)

        def toggle_border():
              self.border_visible = not self.border_visible
              self.border_var.set(self.border_visible)  # Actualiza el valor del CheckBox usando la variable asociada

        self.border_var = tk.BooleanVar(value=self.border_visible)  # Crea la variable de control para el CheckBox
        self.border_frame_checkbox = ctk.CTkCheckBox(self.border_frame, text="Border", variable=self.border_var, command=toggle_border)
        self.border_frame_checkbox.pack(fill="x", padx=10, pady=5)        # -----------------

        
        # Footer
        # -----------------
        self.start_button = ctk.CTkButton(self, text="Start [F2]", command=self.startIt)
        self.start_button.pack(side="bottom", pady=10, fill="x", padx=5)
        # -----------------


        # Actions
        # -----------------
        keyboard.add_hotkey('F2', self.startIt)
        # -----------------

    def startIt(self):
        self.start = True if not self.start else False;
    
        if not (self.border_visible):
            return
        
        if self.start:
            if not self.border_windows:
                self.draw_screen_border()
        else:
            for win in self.border_windows:
                win.destroy()
            self.border_windows = []

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        if (value):
            self.interval_slider.configure(state="disabled", cursor="no", progress_color="gray40", button_color="gray30")
            self.interval_random_slider.configure(state="disabled", cursor="no", progress_color="gray40", button_color="gray30")
            self.start_button.configure(text="Stop [F2]", fg_color="#800d0d", hover_color="#570909")
            self.border_frame_checkbox.configure(state="disabled")
        else:
            self.interval_slider.configure(cursor="hand2", state="normal", progress_color=ctk.ThemeManager.theme["CTkSlider"]["progress_color"] , button_color=ctk.ThemeManager.theme["CTkSlider"]["button_color"])
            self.interval_random_slider.configure(cursor="hand2", state="normal", progress_color=ctk.ThemeManager.theme["CTkSlider"]["progress_color"] , button_color=ctk.ThemeManager.theme["CTkSlider"]["button_color"])
            self.start_button.configure(text="Start [F2]", fg_color=ctk.ThemeManager.theme["CTkButton"]["fg_color"], hover_color=ctk.ThemeManager.theme["CTkButton"]["hover_color"])
            self.border_frame_checkbox.configure(state="normal")
        self._start = value

    def draw_screen_border(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        border_thickness = 3
        positions = [
                    (0, 0, screen_width, border_thickness),  # Top
                    (0, screen_height - border_thickness, screen_width, border_thickness),  # Bottom
                    (0, 0, border_thickness, screen_height),  # Left
                    (screen_width - border_thickness, 0, border_thickness, screen_height)  # Right
                ]
                
        for x, y, w, h in positions:
            border_win = tk.Toplevel(self)
            border_win.overrideredirect(1)
            border_win.geometry(f"{w}x{h}+{x}+{y}")
            border_win.configure(bg="red")
            border_win.attributes("-topmost", True)
            border_win.update_idletasks()
            self.border_windows.append(border_win)

            # TODO: Fix error when F2 instead of Click on them