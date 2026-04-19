# Python Password Generator
### Desktop Application (Tkinter)

## 📌 Project Overview
This is a basic password generator with a simple GUI genrating random passwords based on the user selections such as the length of the password.

## ✨ Key Features
* **Custom Entropy Logic:** Guarantees character variety based on user selection.
* **Real-time Strength Evaluation:** Visual feedback (Weak/Moderate/Strong) based on length and complexity.
* **User-Centric UI:** Built with Tkinter for a clean, distraction-free experience.
* **Clipboard Integration:** One-click copy functionality for seamless use.

## 🛠️ Technical Stack
* **Language:** Python 3.12+
* **Libraries:** `tkinter`, `random`, `string`
* **Architecture:** Event-driven GUI

## 🚀 Usage & Installation

### **For Users (Standalone App)**
If you are on Windows and wish to use the application without installing Python, simply download `PassGenerator.exe` and it is ready to run. No setup required.

### **For Developers (Running from Source)**
To run the script manually or modify the code:
1. Download the `PassGenerator.py` file.
2. Open your terminal or command prompt in that folder.
3. In your terminal, run the following command: `python PassGenerator.py`.

### 🎨 Customization: Adding a Personal Icon
The current version uses the default system icon to ensure compatibility across all environments. If you would like to add a custom `.ico` file:

 * **In the Code:** Add the following line in the GUI Setup section:
    ```python
    root.iconbitmap("your_icon.ico")
    ```
