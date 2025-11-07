# 🎲 Dice Rolling Simulator — Python Tkinter Project

An interactive dice-rolling simulator built using **Python** and **Tkinter**, providing realistic dice animation, random outcomes, and a smooth user experience.

---

## 🧠 Overview

The **Dice Rolling Simulator** visually imitates the action of rolling dice.  
When the user clicks on **ROLL**, the dice face animates through random values before stopping at a final result between 1 and 6.

This project demonstrates how to use **Tkinter’s event loop**, **non-blocking animations**, and **random number generation** to build a clean, responsive GUI.

---

## 💡 Features

✅ Real-time dice animation using `root.after()`  
✅ Beautiful dark theme with vibrant color highlights  
✅ Customizable fonts, colors, and animation speed  
✅ Reset and Exit functionality for user control  
✅ Beginner-friendly and well-commented code  

---

## 🛠️ Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python 3.x |
| **GUI Library** | Tkinter |
| **Random Module** | For generating random dice values |
| **Animation Delay** | Controlled by `root.after()` |
| **Fonts** | Helvetica Neue / Helvetica |

---

## 📂 Project Structure

```
Dice-Rolling-Simulator/
│
├── dice_simulator.py       # Main project file
├── README.md               # Project documentation
└── assets/ (optional)      # Folder for future icons or images
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dice-rolling-simulator.git
   ```

2. Navigate to the project folder:
   ```bash
   cd dice-rolling-simulator
   ```

3. Run the Python script:
   ```bash
   python dice_simulator.py
   ```

✅ The dice window will open — click **ROLL** to start rolling the dice!

---

## 🎨 UI Overview

- **ROLL** — starts the dice animation  
- **RESET** — resets the interface to the default state  
- **EXIT** — closes the application  
- **Result Label** — displays the rolled number (1–6)  
- **Footer** — credits and Python mention  

---

## 📜 Code Explanation

### 🎲 1. Main Code

```python
import tkinter as tk
import random
# Removed 'time' module as time.sleep is replaced by root.after

# ------------------ ANIMATION GLOBALS (for procedural structure) ------------------
animation_frames_count = 0
MAX_ANIMATION_FRAMES = 12
ANIMATION_DELAY_MS = 75

root = tk.Tk()
root.title("🎲 Professional Dice Rolling Simulator")
root.geometry("550x450")
root.config(bg="#1E1E1E")
root.resizable(False, False)

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
MAIN_FONT = ("Helvetica Neue", 22, "bold")
RESULT_FONT = ("Helvetica Neue", 16)
DICE_FONT = ("Helvetica", 120)

def do_animation_frame():
    global animation_frames_count
    if animation_frames_count < MAX_ANIMATION_FRAMES:
        face = random.choice(dice_faces)
        dice_label.config(text=face, fg="#3498DB")
        animation_frames_count += 1
        root.after(ANIMATION_DELAY_MS, do_animation_frame)
    else:
        show_result()

def roll_dice_animation():
    global animation_frames_count
    roll_button.config(state="disabled")
    result_label.config(text="Rolling...", fg="#B2BABB")
    animation_frames_count = 0
    do_animation_frame()

def show_result():
    final_face = random.choice(dice_faces)
    final_number = dice_faces.index(final_face) + 1
    dice_label.config(text=final_face, fg="#DCDCDC")
    result_label.config(text=f"You rolled a {final_number}!", fg="#2ECC71")
    roll_button.config(state="normal")

def reset_game():
    dice_label.config(text="🎲", fg="#DCDCDC")
    result_label.config(text="Click ROLL to roll the dice!", fg="#7F8C8D")

title_label = tk.Label(root, text="🎲 DICE ROLLING SIMULATOR 🎲", font=MAIN_FONT, bg="#1E1E1E", fg="#3498DB")
title_label.pack(pady=20)

dice_label = tk.Label(root, text="🎲", font=DICE_FONT, bg="#1E1E1E", fg="#DCDCDC")
dice_label.pack(pady=10)

result_label = tk.Label(root, text="Click ROLL to roll the dice!", font=RESULT_FONT, bg="#1E1E1E", fg="#7F8C8D")
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1E1E1E")
button_frame.pack(pady=20)

roll_button = tk.Button(button_frame, text="ROLL", font=("Helvetica Neue", 14, "bold"), bg="#27AE60", fg="white", width=12, height=1, command=roll_dice_animation, activebackground="#2ECC71", activeforeground="white", bd=0, relief="flat", highlightthickness=0)
roll_button.grid(row=0, column=0, padx=15, ipady=5)

reset_button = tk.Button(button_frame, text="RESET", font=("Helvetica Neue", 14, "bold"), bg="#F39C12", fg="white", width=12, height=1, command=reset_game, activebackground="#E67E22", activeforeground="white", bd=0, relief="flat", highlightthickness=0)
reset_button.grid(row=0, column=1, padx=15, ipady=5)

exit_button = tk.Button(root, text="EXIT", font=("Helvetica Neue", 12, "bold"), bg="#C0392B", fg="white", width=10, command=root.destroy, activebackground="#E74C3C", activeforeground="white", bd=0, relief="flat", highlightthickness=0)
exit_button.pack(pady=20)

footer_label = tk.Label(root, text="🐍 Made with Python & Tkinter | Professional Edition 💎", font=("Helvetica Neue", 10), bg="#1E1E1E", fg="#7F8C8D")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
```

---

## 📷 Output Example

```
🎲 DICE ROLLING SIMULATOR 🎲
You rolled a 6!
🐍 Made with Python & Tkinter | Professional Edition 💎
```

---

## 🔮 Future Enhancements

- Add sound effects for dice roll  
- Include 3D dice graphics using `pygame` or `OpenGL`  
- Implement multiple dice rolls (2–6 dice at once)  
- Add statistics or probability tracking  

---

## 🤝 Contributing

Contributions are welcome!  
If you have ideas for improvement or want to enhance the UI/UX, feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source under the **MIT License**.

---

## 👨‍💻 Author

**Arudh Pandey**  
🎓 MCA Student, Chandigarh University  
💡 Passionate about Python, GUI Design, and Simulation Projects  
📧 [25MCA20112@cuchd.in]
