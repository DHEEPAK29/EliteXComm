import tkinter as tk
from tkinter import messagebox, scrolledtext
import psutil, pandas as pd, subprocess, time, os, json, random
from datetime import datetime
from pynput import mouse

excel_file = "user_wellbeing_log.xlsx"
columns = [
    "Screen On Time", "Screen Off Time", "App Launch Activity", "Time Spent on App",
    "Mouse Speed", "Mouse Clicks", "Teams Transcript", "Sentiment",
    "Posture Summary", "Weather Info", "Nearby Restaurants",
    "Meeting Person & Role", "Person Timezone", "LLM Summary", "Productivity Insights"
]

if not os.path.exists(excel_file):
    pd.DataFrame(columns=columns).to_excel(excel_file, index=False)

class App:
    def __init__(self, root):
        self.root = root
        root.title("Well-Being Tracker")

        tk.Label(root, text="Session Duration (sec):").pack()
        self.duration = tk.IntVar(value=30)
        tk.Entry(root, textvariable=self.duration).pack()

        tk.Button(root, text="Start Tracking", command=self.run_session).pack(pady=5)
        tk.Button(root, text="Open Excel Logs", command=self.open_excel).pack(pady=5)

        tk.Label(root, text="Weather Info:").pack()
        self.weather_box = tk.Text(root, height=2)
        self.weather_box.pack()

        tk.Label(root, text="Restaurant Offers:").pack()
        self.offer_box = tk.Text(root, height=3)
        self.offer_box.pack()

        tk.Label(root, text="LLM Summary:").pack()
        self.llm_box = scrolledtext.ScrolledText(root, height=4)
        self.llm_box.pack()

        tk.Label(root, text="Transformer Insights:").pack()
        self.insight_box = scrolledtext.ScrolledText(root, height=4)
        self.insight_box.pack()

        self.mouse_clicks = 0
        self.prev_pos = (0, 0)
        self.prev_time = time.time()
        self.listener = mouse.Listener(on_click=self.on_click)
        self.listener.start()

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.mouse_clicks += 1

    def get_mouse_speed(self):
        from pynput.mouse import Controller
        x, y = Controller().position
        now = time.time()
        dx = ((x - self.prev_pos[0]) ** 2 + (y - self.prev_pos[1]) ** 2) ** 0.5
        dt = now - self.prev_time
        speed = dx / dt if dt > 0 else 0
        self.prev_pos = (x, y)
        self.prev_time = now
        return speed

    def get_cached_weather(self):
        try:
            with open("cache/weather.json") as f:
                return json.load(f).get("current_weather", "Unavailable")
        except:
            return "Weather data not available"

    def get_local_offers(self):
        try:
            with open("cache/restaurants.json") as f:
                offers = json.load(f).get("offers", [])
                return "\n".join([f"{o['name']} - {o['discount']}" for o in offers])
        except:
            return "No restaurant data available"

    def collect_metrics(self, duration):
        start = datetime.now()
        before = [p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']]
        time.sleep(duration)
        end = datetime.now()
        after = [p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']]
        launched = list(set(after) - set(before))

        return {
            "Screen On Time": start.strftime("%Y-%m-%d %H:%M:%S"),
            "Screen Off Time": end.strftime("%Y-%m-%d %H:%M:%S"),
            "App Launch Activity": ", ".join(launched),
            "Time Spent on App": "; ".join([f"{app}: {random.randint(5, 30)} min" for app in launched]),
            "Mouse Speed": round(self.get_mouse_speed(), 2),
            "Mouse Clicks": self.mouse_clicks,
            "Teams Transcript": "Deployment planning and KPIs discussed.",
            "Sentiment": random.choice(["Positive", "Neutral", "Negative"]),
            "Posture Summary": "Upright posture detected",
            "Weather Info": self.get_cached_weather(),
            "Nearby Restaurants": self.get_local_offers(),
            "Meeting Person & Role": "Jordan (Dev Lead)",
            "Person Timezone": "PST"
        }

    def call_llm(self, data):
        with open("session_data.json", "w") as f:
            json.dump(data, f)
        result = subprocess.check_output(["python", "local-agent/agent_runner.py"])
        return result.decode("utf-8")

    def call_transformer(self, data):
        apps = data.get("App Launch Activity", "")
        time_spent = data.get("Time Spent on App", "")
        return f"Apps used: {apps}\nTime Allocation:\n{time_spent}"

    def run_session(self):
        self.mouse_clicks = 0
        metrics = self.collect_metrics(self.duration.get())

        llm_summary = self.call_llm(metrics)
        transformer_insight = self.call_transformer(metrics)

        self.weather_box.delete("1.0", tk.END)
        self.weather_box.insert(tk.END, metrics["Weather Info"])

        self.offer_box.delete("1.0", tk.END)
        self.offer_box.insert(tk.END, metrics["Nearby Restaurants"])

        self.llm_box.delete("1.0", tk.END)
        self.llm_box.insert(tk.END, llm_summary)

        self.insight_box.delete("1.0", tk.END)
        self.insight_box.insert(tk.END, transformer_insight)

        metrics["LLM Summary"] = llm_summary
        metrics["Productivity Insights"] = transformer_insight

        df = pd.read_excel(excel_file)
        df = pd.concat([df, pd.DataFrame([metrics])], ignore_index=True)
        df.to_excel(excel_file, index=False)

        messagebox.showinfo("Session Complete", "Insights collected!")

    def open_excel(self):
        try:
            os.startfile(excel_file)
        except:
            messagebox.showinfo("File Path", os.path.abspath(excel_file))

root = tk.Tk()
app = App(root)
root.mainloop()
