import customtkinter as ctk
import os

from src.gui.frames.dashboard import DashboardFrame
from src.gui.frames.auto_clicker import AutoClickerFrame

class Routes(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up
        ctk.set_appearance_mode("dark")

        self.frames = [
            AutoClickerFrame(self, self), # TODO: Remove this
            # DashboardFrame(self, self),
        ]

        self.current_frame = self.frames[0]
        self.current_frame.show()
        self.iconbitmap(os.path.abspath("./src/assets/favicon.ico"))

    def push(self, frame_id):
        next_frame = next((f for f in self.frames if f.id == frame_id), None)
        
        if next_frame and next_frame != self.current_frame:
            self.current_frame.hide()
            self.current_frame = next_frame
            self.current_frame.show()
