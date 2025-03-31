import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(width=400, height=300)
        
        label = ctk.CTkLabel(self, text="Pantalla Principal")
        label.pack(pady=20)

        button_to_settings = ctk.CTkButton(self, text="Ir a Configuración", command=self.show_settings)
        button_to_settings.pack(pady=10)

    def show_settings(self):
        self.controller.show_settings_frame()