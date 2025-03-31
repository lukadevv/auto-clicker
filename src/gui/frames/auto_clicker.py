import customtkinter as ctk

class AutoClickerFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(width=350, height=250)
        
        label = ctk.CTkLabel(self, text="Pantalla de Configuración")
        label.pack(pady=20)

        button_to_main = ctk.CTkButton(self, text="Volver a la Pantalla Principal", command=self.show_main)
        button_to_main.pack(pady=10)

    def show_main(self):
        self.controller.show_main_frame()