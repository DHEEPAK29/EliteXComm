# EliteXComm


<img width="872" height="779" alt="image" src="https://github.com/user-attachments/assets/2965e84e-eb51-49d9-bb18-d1b145458b84" />

<img width="869" height="779" alt="image" src="https://github.com/user-attachments/assets/9402d94a-2743-4c70-8dd8-9d1692556670" />


AI Inference (Local)  
llama-cpp-python: Lightweight Python bindings for running GGUF-format LLMs  
GGUF Model File (e.g., Mistral-7B-Instruct): Stored and loaded from disk for summarization  
session_data.json: Serialized metrics passed from GUI to LLM agent  
local-agent/agent_runner.py: Script that invokes the local LLM and returns a summary  

Productivity Insights (Offline Logic)  
Tabular transformer logic embedded in the app (or externally via AutoGluon if expanded)  
Provides structured insights into app usage without external inference  

Core Language & Execution  
Python: Primary programming language for all scripts and interface logic  
Tkinter: Built-in Python GUI library for local desktop applications  

System Monitoring & Input Tracking  
psutil: Detects running processes and monitors system-level app activity  
pynput: Tracks mouse movement and click behavior on-device  
datetime: Handles session timing and timestamp management  

Local Data Storage & Processing  
pandas: Creates and manipulates structured session data  
openpyxl: Reads and writes Excel files for persistent logging  
JSON: Stores cached environmental context like weather and restaurant offers  

Environmental Context (Offline)  
weather.json: Local cache file for weather data  
restaurants.json: Local cache file for restaurant offers  



File Management & Workflow  
os.startfile: Opens Excel logs directly from the device  
Excel (.xlsx): Local permanent log of all sessions with structured telemetry  
