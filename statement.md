# Antipode Finder – Program Statement

## Problem Statement
Understanding the antipodal point of a given geographical location can be useful in geography, earth science studies, and mapping applications. An antipode is the point on Earth that lies exactly opposite another point. Calculating this manually can be confusing due to coordinate rules and longitude normalization.
This program provides a simple and interactive way to calculate and view the antipode of any latitude and longitude.

## Scope of the Project
- Accepting latitude and longitude inputs from the user.
- Validating the entered coordinates.
- Calculating the antipodal coordinates using geographic rules.
- Displaying the computed results in a user-friendly interface.
- Providing an option to directly view the antipode location on Google Maps.
- Handling incorrect, invalid, or non-numeric inputs gracefully.

## Target Users
- Students learning geography or earth sciences  
- Teachers demonstrating antipodal concepts  
- Developers looking for a simple GUI-based coordinate tool  
- Anyone curious about the opposite point of a given location on Earth  

## High-Level Features
- Tkinter-based GUI: Simple and intuitive interface for entering coordinates.
- Input Validation: Ensures latitude is within –90 to 90 and longitude within –180 to 180.
- Accurate Antipode Calculation: Computes the opposite latitude and normalized longitude.
- Google Maps Integration: Opens the antipodal point directly in the browser.
- Error Handling: User-friendly alerts for invalid or non-numeric input.
