import customtkinter as ctk

from src.gui.frames.dashboard import DashboardFrame
from src.gui.frames.auto_clicker import AutoClickerFrame

class Routes(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.frames = [
            DashboardFrame(self, self),
            AutoClickerFrame(self, self)
        ]

        self.current_frame = self.frames[0]
        self.current_frame.show()
        
        # self.title("Aplicación Modular con CustomTkinter")
        # self.geometry("1200x1200")
        
        # self.dashboard = DashboardFrame(self, self)
        # self.auto_clicker = AutoClickerFrame(self, self)

        # self.dashboard.pack(fill="both", expand=True)

    def push(self, frame_id):
        next_frame = next((f for f in self.frames if f.id == frame_id), None)
        
        if next_frame and next_frame != self.current_frame:
            self.current_frame.hide()
            self.current_frame = next_frame
            self.current_frame.show()
