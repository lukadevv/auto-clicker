import customtkinter as ctk
import src.gui.frames.frame as Frame

class AutoClickerFrame(Frame.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, "auto_clicker", 400 ,400)
        
        label = ctk.CTkLabel(self, text="Pantalla de Configuración")
        label.pack(pady=20)

        button_to_main = ctk.CTkButton(self, text="Volver a la Pantalla Principal", command=lambda: controller.push("dashboard"))
        button_to_main.pack(pady=10)