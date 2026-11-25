from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, UnidentifiedImageError


input_file = None


def convert_webp_to_png(input_path, output_path):
    with Image.open(input_path) as image:
        image.save(output_path, "PNG")


def select_file():
    global input_file
    selected = filedialog.askopenfilename(
        title="Select a WebP image",
        filetypes=[("WebP files", "*.webp")],
    )
    if selected:
        input_file = Path(selected)
        selected_file_label.config(text=input_file.name)


def convert():
    if input_file is None:
        messagebox.showwarning("No file selected", "Please select a WebP image first.")
        return

    output_folder = Path.home() / "Downloads"
    output_file = output_folder / f"{input_file.stem}.png"

    try:
        output_folder.mkdir(parents=True, exist_ok=True)
        if output_file.is_file() and not messagebox.askyesno(
            "Replace existing PNG?",
            f"A PNG already exists at:\n{output_file}\n\nReplace it?",
            default=messagebox.NO,
        ):
            return
        convert_webp_to_png(input_file, output_file)
    except (OSError, UnidentifiedImageError) as error:
        messagebox.showerror("Conversion failed", str(error))
        return

    messagebox.showinfo(
        "Conversion complete",
        f"Saved the converted image to:\n{output_file}",
    )


window = tk.Tk()
window.title("WebP to PNG Converter")

prompt_label = tk.Label(window, text="Please select a .webp file:")
prompt_label.pack()

file_button = tk.Button(window, text="Select File", command=select_file)
file_button.pack()

selected_file_label = tk.Label(window, text="No file selected")
selected_file_label.pack()

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

window.mainloop()
