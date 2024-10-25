import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

# Function to generate QR code
def generate_qrcode():
    url = url_entry.get()
    filename = filename_entry.get()

    if not url or not filename:
        messagebox.showerror("Input Error", "Please fill in both fields.")
        return

    # Generate the QR code
    qr = qrcode.QRCode(
        version=15,
        box_size=10,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code image
    filepath = f"{filename}.png"
    img.save(filepath)

    # Display the QR code in the app
    display_qrcode(filepath)

def display_qrcode(filepath):
    # Open the saved QR code image
    img = Image.open(filepath)
    img.thumbnail((200, 200))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)

    # Update the label to show the image
    qr_image_label.config(image=img_tk)
    qr_image_label.image = img_tk  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

icon_image = Image.open(r'C:\Users\hp\Desktop\testPython\hello guys.png')  # Use raw string
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

# Set the size of the window
# Set the desired width and height of the window
window_width = 700
window_height = 650

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window (width x height + x_offset + y_offset)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='#90ee90')

# Input fields for URL and filename
url_label = tk.Label(root, text="Enter URL",fg='blue',bg="#90ee90",font=("Arial", 20))
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=40,highlightbackground="red",font=("Arial", 10))
url_entry.pack(pady=5)

filename_label = tk.Label(root, text="Enter filename (without .png):",fg='blue',bg="#90ee90",font=("Arial", 20))
filename_label.pack(pady=10)
filename_entry = tk.Entry(root, width=40,font=("Arial", 10))
filename_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode,activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="blue",
                   cursor="hand2",
                   disabledforeground="blue",
                   fg="black",
                   font=("Arial", 10),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
submit_button.pack(pady=20)

# Frame to hold the QR code image
image_frame = tk.Frame(root)
image_frame.pack(pady=10)
qr_image_label = tk.Label(image_frame,bg="#90ee90")
qr_image_label.pack()

# Run the app
root.mainloop()
