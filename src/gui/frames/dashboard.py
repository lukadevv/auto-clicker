import customtkinter as ctk
import src.gui.frames.frame as Frame

import src.gui.components.organisms.side as SideBarComponent


class DashboardFrame(Frame.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, "dashboard", 800, 500)
        
        self.sidebar = SideBarComponent.SideBar(self)
    
