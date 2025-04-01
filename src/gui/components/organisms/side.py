import customtkinter as ctk
from PIL import Image


class SideBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=200, height=500, corner_radius=10)

        def createButton(sidebar, text, image):
            ctk.CTkButton(sidebar, 
                      text=text, 
                      font=("Arial", 16, "bold"), 
                      width=180, 
                      anchor="nw", 
                      image=image,
                      compound="left",
                      ).pack(pady=5)
            
        self.pack_propagate(False)
        self.pack(side="left", fill="y", padx=10, pady=10)

        icon_image = ctk.CTkImage(light_image=Image.open("src/assets/icons/home_fill.png"), size=(24, 24))
        
        createButton(self, "Dashboard", icon_image)