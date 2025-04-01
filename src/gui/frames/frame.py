import customtkinter as ctk

class Frame(ctk.CTkFrame):
    def __init__(self, parent, id, width=None, height=None):
        super().__init__(parent)

        self.id = id
        self.geometry = parent.geometry
        self.width = width
        self.height = height
        
        if (type(id) == None):
            raise ValueError("Frame \"id\" not exists!")
        
        if width and height:
            self.configure(width=width, height=height)
        

    def hide(self):
        self.pack_forget()

    def show(self): 
        self.pack(fill="both", expand=True)
        self.geometry(f"{self.width}x{self.height}")