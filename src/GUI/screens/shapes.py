import tkinter
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk, ImageGrab
import io
from src.OCR.ocr import take_screenshot


def shapes_screen(content_frame):
    button_frame = ctk.CTkFrame(content_frame, fg_color="lightgray")
    button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    new_screenshot = ctk.CTkButton(button_frame, text="New Screenshot", command=lambda: take_and_display_screenshot(content_frame))
    new_screenshot.grid(row=0, column=0, padx=10, pady=15, sticky="w")

    load_screenshot = ctk.CTkButton(button_frame, text="Load Screenshot", command=lambda: print("Shape Button Clicked"))
    load_screenshot.grid(row=0, column=1, padx=10, pady=15, sticky="w")

    save_shape = ctk.CTkButton(button_frame, text="Save Screenshot", command=lambda: save_selected_area(content_frame))
    save_shape.grid(row=0, column=2, padx=10, pady=15, sticky="w")

    # Object property field
    object_property_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
    object_property_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    object_property_frame.columnconfigure(0, weight=0) # dynamic nav bar
    object_property_frame.columnconfigure(1, weight=1)

    shape_name_label = ctk.CTkLabel(object_property_frame, text="Object Name")
    shape_name_label.grid(row=0, column=0, padx=10, pady=15)

    content_frame.var_shape_name = tk.StringVar()
    shape_name_input = ctk.CTkEntry(object_property_frame, width=200, height=40, textvariable=content_frame.var_shape_name)
    shape_name_input.grid(row=0, column=1, padx=10, pady=15)

    # Status field
    shape_status_label = ctk.CTkLabel(object_property_frame, text="Status:")
    shape_status_label.grid(row=0, column=2, padx=10, pady=15)

    content_frame.shape_status_text = ctk.CTkLabel(object_property_frame, text="ok")
    content_frame.shape_status_text.grid(row=0, column=3, padx=10, pady=15)


def take_and_display_screenshot(content_frame):
    # Take a screenshot
    screenshot = ImageGrab.grab()
    content_frame.original_screenshot = screenshot  # Store the full-res image for cropping

    # Resize for display (calculate aspect ratio)
    display_width = 800
    aspect_ratio = screenshot.height / screenshot.width
    display_height = int(display_width * aspect_ratio)

    screenshot_resized = screenshot.resize((display_width, display_height), Image.LANCZOS)

    # Convert to a format usable by Tkinter
    img = ImageTk.PhotoImage(screenshot_resized)
    content_frame.img = img  # Store reference to avoid garbage collection

    # Display on a Canvas
    canvas = tk.Canvas(content_frame, width=display_width, height=display_height, bg="white")
    canvas.grid(row=3, column=0, columnspan=3, pady=10, padx=10)
    canvas.create_image(0, 0, anchor="nw", image=img)

    # Enable rectangle drawing
    canvas.bind("<ButtonPress-1>", lambda event: start_rectangle(event, canvas))
    canvas.bind("<B1-Motion>", lambda event: draw_rectangle(event, canvas))
    canvas.bind("<ButtonRelease-1>", lambda event: finish_rectangle(event, content_frame, canvas))


def start_rectangle(event, canvas):
    canvas.start_x = event.x
    canvas.start_y = event.y
    canvas.rect_id = None


def draw_rectangle(event, canvas):
    if canvas.rect_id:
        canvas.delete(canvas.rect_id)
    canvas.rect_id = canvas.create_rectangle(canvas.start_x, canvas.start_y, event.x, event.y, outline="red", width=2)


def finish_rectangle(event, content_frame, canvas):
    x1, y1 = canvas.start_x, canvas.start_y
    x2, y2 = event.x, event.y

    # Ensure coordinates are sorted
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))

    # Convert coordinates to the original screenshot scale
    scale_x = content_frame.original_screenshot.width / canvas.winfo_width()
    scale_y = content_frame.original_screenshot.height / canvas.winfo_height()
    x1_original, y1_original = int(x1 * scale_x), int(y1 * scale_y)
    x2_original, y2_original = int(x2 * scale_x), int(y2 * scale_y)

    content_frame.selected_area = (x1_original, y1_original, x2_original, y2_original)
    print(f"Selected Area (original scale): {content_frame.selected_area}")


def save_selected_area(content_frame):
    object_name = content_frame.var_shape_name.get()
    object_file = f"{object_name}.png"

    if object_name:
        if hasattr(content_frame, "selected_area") and hasattr(content_frame, "original_screenshot"):
            x1, y1, x2, y2 = content_frame.selected_area
            screenshot = content_frame.original_screenshot

            # Crop and save the selected area
            cropped = screenshot.crop((x1, y1, x2, y2))
            cropped.save(object_file)

            content_frame.shape_status_text.configure(text=f"Selected area saved as '{object_file}'", text_color="green")
        else:
            content_frame.shape_status_text.configure(text="Error: No area selected or screenshot not available", text_color="red")
    else:
        print("Enter an object name")
        content_frame.shape_status_text.configure(text="Error: Enter an object name", text_color="red")

