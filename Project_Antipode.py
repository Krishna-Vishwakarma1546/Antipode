import tkinter as tk
from tkinter import messagebox
import webbrowser
def anti(lat, lon):
    a_lat = -lat
    if lon >= 0:
        a_lon = lon - 180
    else:
        a_lon = lon + 180

    if a_lon > 180:
        a_lon -= 360
    elif a_lon < -180:
        a_lon += 360

    return round(a_lat, 6), round(a_lon, 6)
def open_map(lat, lon):
    link = f"https://www.google.com/maps/@{lat},{lon},5z"
    webbrowser.open(link)
def calc():
    try:
        lat = float(lat_in.get())
        lon = float(lon_in.get())
        if not -90 <= lat <= 90:
            messagebox.showerror("Error", "Latitude must be -90 to 90.")
            return
        if not -180 <= lon <= 180:
            messagebox.showerror("Error", "Longitude must be -180 to 180.")
            return

        a_lat, a_lon = anti(lat, lon)
        out1.config(text=f"Lat : {a_lat}")
        out2.config(text=f"Lon : {a_lon}")
        map_btn.config(command=lambda: open_map(a_lat, a_lon))
        map_btn.pack(pady=5)
    except:
        messagebox.showerror("Error", "Enter numbers only.")
root = tk.Tk()
root.title("Antipode Finder")
root.geometry("300x300")
tk.Label(root, text="Latitude (-90 to 90):").pack()
lat_in = tk.Entry(root)
lat_in.pack(pady=5)
tk.Label(root, text="Longitude (-180 to 180):").pack()
lon_in = tk.Entry(root)
lon_in.pack(pady=5)
tk.Button(root, text="Find", command=calc).pack(pady=10)
tk.Label(root, text="Result:").pack()
out1 = tk.Label(root, text="Lat : --")
out1.pack()
out2 = tk.Label(root, text="Lon : --")
out2.pack()
map_btn = tk.Button(root, text="Open in Google Maps")
root.mainloop()
