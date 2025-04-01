import customtkinter as ctk
import src.gui.frames.frame as Frame

class DashboardFrame(Frame.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, "dashboard", 400 ,400)

        label = ctk.CTkLabel(self, text="Pantalla Principal")
        label.pack(pady=20)

        button_to_settings = ctk.CTkButton(self, text="Ir a Configuración", command=lambda: controller.push("auto_clicker"))
        button_to_settings.pack(pady=10)
