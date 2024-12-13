import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

from src.GUI.screens.shapes import shapes_screen
from src.OCR.ocr import take_screenshot


def start_screen(app):
    # Setting up grids
    configure_grid(app)

    # Navigation bar - left
    create_navigation_grid(app)

    # Content frame
    create_content_grid(app)

    # UI elements
    # button1 = ctk.CTkButton(app, text="Take a screenshot", command=lambda: screenshot(app))
    # button1.pack()

    # app.button = ctk.CTkButton(app, command=button_click)
    # app.button.grid(row=0, column=0, padx=20, pady=10)

    # title.configure(text_color="red")


def create_navigation_grid(app):
    app.nav_frame = ctk.CTkFrame(app, fg_color="lightgreen")
    app.nav_frame.grid(row=0, column=0, sticky="nsew")

    label1 = ctk.CTkLabel(app.nav_frame, text="Menu")
    label1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Align to the left

    start = ctk.CTkButton(app.nav_frame, text="Start", command=lambda: create_content_grid(app))
    start.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    processes = ctk.CTkButton(app.nav_frame, text="Processes", command=lambda: load_processes_screen(app.content_frame))
    processes.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    shapes = ctk.CTkButton(app.nav_frame, text="Shapes", command=lambda: load_shapes_screen(app.content_frame))
    shapes.grid(row=3, column=0, padx=10, pady=5, sticky="w")


def create_content_grid(app):
    app.content_frame = ctk.CTkFrame(app, fg_color="lightblue")
    app.content_frame.grid(row=0, column=1, sticky="nsew")

    label = ctk.CTkLabel(app.content_frame, text="Main Content Area")
    label.pack(padx=20, pady=20)


def configure_grid(app):
    app.columnconfigure(0, weight=0) # dynamic nav bar
    app.columnconfigure(1, weight=1) # content space
    app.rowconfigure(0, weight=1)


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def load_shapes_screen(content_frame):
    clear_frame(content_frame)
    shapes_screen(content_frame)


def load_processes_screen(content_frame):
    clear_frame(content_frame)

