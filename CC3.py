import tkinter as tk
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.prompt = "The quick brown fox jumps over the lazy dog."
        self.user_input = ""
        self.start_time = 0

        self.prompt_label = tk.Label(root, text=self.prompt)
        self.prompt_label.pack()

        self.user_input_entry = tk.Entry(root)
        self.user_input_entry.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def start_test(self):
        self.user_input = ""
        self.start_time = time.time()
        self.user_input_entry.delete(0, tk.END)
        self.user_input_entry.config(state=tk.NORMAL)
        self.user_input_entry.focus()
        self.start_button.config(state=tk.DISABLED)
        self.root.bind("<Return>", self.submit_input)

    def submit_input(self, event):
        self.user_input = self.user_input_entry.get()
        self.user_input_entry.config(state=tk.DISABLED)
        self.calculate_result()

    def calculate_result(self):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        words = self.prompt.split()
        user_words = self.user_input.split()

        correct_words = sum(1 for uw, w in zip(user_words, words) if uw == w)
        accuracy = (correct_words / len(words)) * 100
        wpm = (len(user_words) / elapsed_time) * 60

        result_text = f"Time taken: {round(elapsed_time, 2)} seconds\n"
        result_text += f"Words per minute (WPM): {round(wpm, 2)}\n"
        result_text += f"Accuracy: {round(accuracy, 2)}%"
        self.result_label.config(text=result_text)

        self.start_button.config(state=tk.NORMAL)
        self.root.unbind("<Return>")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()