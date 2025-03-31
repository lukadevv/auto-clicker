import customtkinter as ctk

class SPA(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Single Page Application con CustomTkinter")
        self.geometry("500x400")  # Tamaño de la ventana principal
        
        # Crear los frames para las diferentes "pantallas"
        self.screen1 = self._create_screen1()
        self.screen2 = self._create_screen2()

        # Mostrar la primera pantalla
        self.screen1.place(x=50, y=50, width=400, height=300)  # Tamaño y posición personalizada para esta pantalla

    def _create_screen1(self) -> ctk.CTkFrame:
        """Crea y retorna el frame para la pantalla 1"""
        screen = ctk.CTkFrame(self)
        label = ctk.CTkLabel(screen, text="Pantalla 1")
        label.pack(pady=20)
        
        button_to_screen2 = ctk.CTkButton(screen, text="Ir a Pantalla 2", command=self.show_screen2)
        button_to_screen2.pack(pady=10)
        
        return screen

    def _create_screen2(self) -> ctk.CTkFrame:
        """Crea y retorna el frame para la pantalla 2"""
        screen = ctk.CTkFrame(self)
        label = ctk.CTkLabel(screen, text="Pantalla 2")
        label.pack(pady=20)
        
        button_to_screen1 = ctk.CTkButton(screen, text="Volver a Pantalla 1", command=self.show_screen1)
        button_to_screen1.pack(pady=10)
        
        return screen

    def show_screen1(self) -> None:
        """Muestra la pantalla 1 y oculta la pantalla 2"""
        self.screen2.place_forget()  # Ocultar pantalla 2
        self.screen1.place(x=50, y=50, width=400, height=300)  # Mostrar pantalla 1 con tamaño y posición

    def show_screen2(self) -> None:
        """Muestra la pantalla 2 y oculta la pantalla 1"""
        self.screen1.place_forget()  # Ocultar pantalla 1
        self.screen2.place(x=75, y=75, width=350, height=250)  # Mostrar pantalla 2 con tamaño y posición

if __name__ == "__main__":
    app = SPA()
    app.mainloop()
