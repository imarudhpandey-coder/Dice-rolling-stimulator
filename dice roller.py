import tkinter as tk
import random
import time

# ------------------ MAIN WINDOW ------------------
root = tk.Tk()
root.title("🎲 Dice Rolling Simulator")
root.geometry("500x450")
root.config(bg="#F2F4F6")

# ------------------ VARIABLES ------------------
dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# ------------------ FUNCTIONS ------------------
def roll_dice_animation():
    """Dice rolling animation"""
    roll_button.config(state="disabled")
    result_label.config(text="Rolling...", fg="#616A6B")
    root.update()

    for _ in range(10):  # show random faces quickly
        face = random.choice(dice_faces)
        dice_label.config(text=face, fg="#1A5276")
        root.update()
        time.sleep(0.1)

    show_result()

def show_result():
    """Show final dice roll result"""
    final_face = random.choice(dice_faces)
    dice_label.config(text=final_face, fg="#154360")
    result_label.config(text=f"You rolled a {dice_faces.index(final_face)+1}!", fg="#117A65")
    roll_button.config(state="normal")

def reset_game():
    """Reset screen"""
    dice_label.config(text="🎲", fg="#154360")
    result_label.config(text="Click ROLL to roll the dice!", fg="#424949")

# ------------------ UI DESIGN ------------------
title_label = tk.Label(
    root, text="🎲 DICE ROLLING SIMULATOR 🎲",
    font=("Comic Sans MS", 20, "bold"), bg="#F2F4F6", fg="#1A5276"
)
title_label.pack(pady=20)

dice_label = tk.Label(
    root, text="🎲", font=("Arial", 100), bg="#F2F4F6", fg="#1A5276"
)
dice_label.pack(pady=30)

result_label = tk.Label(
    root, text="Click ROLL to roll the dice!", font=("Comic Sans MS", 14),
    bg="#F2F4F6", fg="#424949"
)
result_label.pack(pady=10)

# ------------------ BUTTONS ------------------
button_frame = tk.Frame(root, bg="#F2F4F6")
button_frame.pack(pady=30)

roll_button = tk.Button(
    button_frame, text="🎯 ROLL", font=("Arial", 14, "bold"),
    bg="#3498DB", fg="white", width=12, height=1, relief="flat",
    command=roll_dice_animation
)
roll_button.grid(row=0, column=0, padx=15)

reset_button = tk.Button(
    button_frame, text="🔁 RESET", font=("Arial", 14, "bold"),
    bg="#17A589", fg="white", width=12, height=1, relief="flat",
    command=reset_game
)
reset_button.grid(row=0, column=1, padx=15)

exit_button = tk.Button(
    root, text="🚪 EXIT", font=("Arial", 12, "bold"),
    bg="#E74C3C", fg="white", width=10, relief="flat",
    command=root.destroy
)
exit_button.pack(pady=20)

# ------------------ FOOTER ------------------
footer_label = tk.Label(
    root, text="🐍 Made with Python | Designed by Varun 💎",
    font=("Comic Sans MS", 10), bg="#F2F4F6", fg="#5D6D7E"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
