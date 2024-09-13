# INTERNET-SPEED-TEST-APP

Here is the documentation for your internet speed test app code:

---

**Internet Speed Test Application Code Documentation**

### 1. **Imports**:
```python
import tkinter as tk
import speedtest
```
- `tkinter`: Used for creating the graphical user interface (GUI) for the application.
- `speedtest`: Python library used to test internet speed (download, upload, and ping).

### 2. **Speed_Test Class**:
```python
class Speed_Test:
```
- This class is responsible for handling the logic of the internet speed test, including downloading, uploading, and ping speed.
  
- **Methods**:
    - `download_speed`: 
        - Initiates the speedtest object.
        - Retrieves the download speed and converts it from bits per second to Megabits per second (Mbps).
        - Returns the download speed.
    
    - `upload_speed`: 
        - Retrieves the upload speed and converts it from bits per second to Megabits per second (Mbps).
        - Returns the upload speed.
    
    - `ping`: 
        - Retrieves the ping time in milliseconds.
        - Returns the ping result.

### 3. **TASK_BAR_IMAGE Class**:
```python
class TASK_BAR_IMAGE(Speed_Test):
```
- Inherits from `Speed_Test`. This class creates the taskbar image, displays download, upload, and ping results, and performs the speed test when triggered.

- **Attributes**:
    - `boximg`: Loads and displays an image as the taskbar background.
    - `ping_`, `download`, `upload`: Labels for displaying the ping, download, and upload speeds.
  
- **Methods**:
    - `speed_check`: 
        - Triggers the download speed calculation and updates the respective labels.
        - Calls `get_upload_and_ping` after a short delay to get the upload speed and ping.
    
    - `get_upload_and_ping`: 
        - Updates the upload speed and ping in the UI labels.

### 4. **BOX_IMAGE Class**:
```python
class BOX_IMAGE():
```
- Creates the background image and displays a label showing either the download or upload speed, along with a label to indicate whether it's showing the download or upload.

- **Attributes**:
    - `task_img`: Image of the blue box background.
    - `speed_show`: Label to show the current download/upload speed.
    - `download_label`: Label indicating whether the current speed being shown is the "Download" or "Upload" speed.

### 5. **BLUE_BUTTON Class**:
```python
class BLUE_BUTTON:
```
- Creates a button that triggers the speed test when clicked.

- **Attributes**:
    - `button_img`: Loads an image of a blue button.
    - `button`: The button that calls `speed_check` from the `TASK_BAR_IMAGE` instance when clicked.

### 6. **APP Class (Main Application)**:
```python
class APP(tk.Tk):
```
- This is the main application class that initializes and manages the GUI.
  
- **Attributes**:
    - `app_photo`: Instance of `BOX_IMAGE` class for displaying the background box and speed labels.
    - `task_image`: Instance of `TASK_BAR_IMAGE` class for handling speed test functionality and taskbar image.
    - `button`: Instance of `BLUE_BUTTON` class for the button that initiates the speed test.

### 7. **Execution**:
```python
a = APP()
```
- Instantiates the `APP` class to run the application.

---

This documentation should provide a clear understanding of the structure and functionality of the code.