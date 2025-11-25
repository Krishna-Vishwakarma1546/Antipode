# 🌍 Antipode Finder

## 📖 Overview of the Project
The **Antipode Finder** is a Python application with a simple Tkinter-based GUI that calculates the **antipodal point** of a given latitude and longitude.  
An antipode is the point on Earth directly opposite to another point.  
This tool also provides an option to open the calculated location in **Google Maps** for instant visualization.

---

## ✨ Features
- Simple and clean GUI built using Tkinter  
- Validates input before processing  
- Calculates accurate antipodal latitude and longitude  
- “Open in Google Maps” button for quick view  
- Error handling for invalid or non-numeric inputs  
- Lightweight and runs on any system with Python installed  

---

## 🛠 Technologies / Tools Used
- **Python 3.x**  
- **Tkinter** (built-in GUI framework)  
- **webbrowser** module  
- **messagebox** module  

---

## ⚙️ Steps to Install & Run the Project
1. **Clone the repository (or download ZIP)**  
   ```bash
   git clone https://github.com/your-username/antipode-finder.git

2. **Navigate to the project folder**

    cd antipode-finder

3. **Run the Python script**

   python antipode_finder.py

**Make sure Python 3.x is installed on your system.**

🧪 **Instructions for Testing**

    You can test the application by entering different latitude and longitude values:

**✔ Valid Inputs**

Latitude must be between -90 to 90

Longitude must be between -180 to 180

**✔ Example Test Cases**

Input Latitude

Input Longitude

Expected Antipode

20, 70 → (-20, -110)
-45, 120 → (45, -60)
0, -180 → (0, 0)

**✔ Error Handling**

Enter text instead of numbers → should show an error

Enter values out of range → should show an error

**✔ Maps Testing**

After a successful calculation, click Open in Google Maps

Your browser should open the antipode location instantly
