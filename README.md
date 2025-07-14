# EliteXComm


<img width="872" height="779" alt="image" src="https://github.com/user-attachments/assets/2965e84e-eb51-49d9-bb18-d1b145458b84" />

<img width="869" height="779" alt="image" src="https://github.com/user-attachments/assets/9402d94a-2743-4c70-8dd8-9d1692556670" />

Project Title:  Edge-Based Productivity and Well-being Monitoring App
Problem Statement: (1-2 sentences) 
Modern work environments often lead to prolonged screen time, poor posture, and inefficient work habits, negatively impacting both productivity and well-being. There is a need for an edge-based solution that monitors user activity directly on their device and provides actionable insights to improve health and productivity.
Solution Overview: (2-3 paragraphs)
The proposed app leverages edge computing to monitor user productivity and well-being by tracking various activities directly on their device. It will log active work time, screen scanning, application launches, and tactile information such as button presses and mouse movements locally. During meetings, the app will analyze the user's tone for sentiment analysis and track the number of hours spent in meetings to assess their impact on actual work. Additionally, the app will use the device's camera to analyze posture and provide feedback in real-time. It will also monitor breaks and map productivity before and after breaks.
To enhance user well-being, the app will gather weather information from nearby locations and suggest taking breaks during good weather conditions. It will also recommend nearby restaurants with new offers. Furthermore, the app will map active relationships across time zones to help users manage their work-life balance effectively. All these features are processed on-device, ensuring privacy and reducing latency.
Technical Details: (Technologies, libraries, models used) 
AI Inference (Local)
•	llama-cpp-python: Lightweight Python bindings for running GGUF-format LLMs
•	GGUF Model File (e.g., Mistral-7B-Instruct): Stored and loaded from disk for summarization
•	session_data.json: Serialized metrics passed from GUI to LLM agent
•	local-agent/agent_runner.py: Script that invokes the local LLM and returns a summary
Productivity Insights (Offline Logic)
•	Tabular transformer logic embedded in the app (or externally via AutoGluon if expanded)
•	Provides structured insights into app usage without external inference
Core Language & Execution
•	Python: Primary programming language for all scripts and interface logic
•	Tkinter: Built-in Python GUI library for local desktop applications
System Monitoring & Input Tracking
•	psutil: Detects running processes and monitors system-level app activity
•	pynput: Tracks mouse movement and click behavior on-device
•	datetime: Handles session timing and timestamp management
Local Data Storage & Processing
•	pandas: Creates and manipulates structured session data
•	openpyxl: Reads and writes Excel files for persistent logging
•	JSON: Stores cached environmental context like weather and restaurant offers
Environmental Context (Offline)
•	weather.json: Local cache file for weather data
•	restaurants.json: Local cache file for restaurant offers
File Management & Workflow
•	os.startfile: Opens Excel logs directly from the device
•	Excel (.xlsx): Local permanent log of all sessions with structured telemetry
Impact & Results: 
The app is expected to improve user productivity by providing insights into work habits and suggesting improvements. By monitoring posture and encouraging breaks during good weather, it aims to enhance physical well-being. The sentiment analysis during meetings will help users understand their emotional state and its impact on productivity. Overall, the app will contribute to a healthier and more productive work environment, with all processing done on-device to ensure user privacy and immediate feedback.



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
