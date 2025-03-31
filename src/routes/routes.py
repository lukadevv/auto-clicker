import customtkinter as ctk

from src.gui.frames.dashboard import DashboardFrame
from src.gui.frames.auto_clicker import AutoClickerFrame

class Routes(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplicación Modular con CustomTkinter")
        self.geometry("500x400")
        
        # Crear los frames
        self.main_frame = DashboardFrame(self, self)
        self.settings_frame = AutoClickerFrame(self, self)

        # Mostrar la pantalla principal por defecto
        self.main_frame.pack(fill="both", expand=True)

    def show_main_frame(self):
        """Mostrar el frame principal y ocultar el de configuraciones"""
        self.settings_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def show_settings_frame(self):
        """Mostrar el frame de configuraciones y ocultar el principal"""
        self.main_frame.pack_forget()
        self.settings_frame.pack(fill="both", expand=True)
