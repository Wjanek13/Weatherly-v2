import tkinter as tk
from tkintermapview import TkinterMapView
from pyowm import OWM
from PIL import Image, ImageTk

# --- SETUP ---
API_KEY = "903c7b602f35c53a208eac1477998b99"
owm = OWM(API_KEY)

root = tk.Tk()
bg_color = "#42a5f5"
root.configure(bg=bg_color)
root.attributes("-fullscreen", True)
root.title("Weatherly")

# --- FUNCTIONS ---

def show_map():
    menu_frame.pack_forget()
    map_frame.pack(fill="both", expand=True)

def show_menu():
    map_frame.pack_forget()
    menu_frame.pack(fill="both", expand=True)

# --- MENU SCREEN ---

menu_frame = tk.Frame(root, bg=bg_color)
menu_frame.pack(fill="both", expand=True)

# Load and display the logo inside the menu_frame
logo_image = Image.open(r"Images/Logo.png")
width, height = logo_image.size
new_width = int(width * 0.6)
new_height = int(height * 0.6)
tk_img = ImageTk.PhotoImage(logo_image.resize((new_width, new_height)))

# We set the parent to menu_frame and removed the fixed width/height 
# to let the image define the label size naturally
image_label = tk.Label(menu_frame, image=tk_img, bg=bg_color)
image_label.image = tk_img 
image_label.pack()
image_label.place(anchor="center", relx=0.5, rely=0.35)
# --- MAP SCREEN ---

map_frame = tk.Frame(root)

map_widget = TkinterMapView(map_frame, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_position(51.5074, -0.1278)
map_widget.set_zoom(5)

root.mainloop()