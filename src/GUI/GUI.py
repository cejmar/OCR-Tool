import tkinter as tk
import customtkinter as ctk
import screens.start
from PIL import Image, ImageTk


class CustomApp:
    def __init__(self):
        # Root-Fenster erstellen
        self.root = ctk.CTk()
        self.root.title("OCR Sandbox")
        self.root.geometry("1080x720")

        # Setting up start elements
        screens.start.start_screen(self.root)

    # def change_label(self):
    #    self.label.configure(text="Text geändert!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CustomApp()
    app.run()
