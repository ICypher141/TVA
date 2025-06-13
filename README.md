🛰️ Voice-Controlled Celestial Object Locator
📋 Overview
This project is a voice-driven astronomical assistant that interprets user commands to identify celestial objects and calculate their real-time altitude and azimuth coordinates based on the user's location. The tool uses natural language processing, SIMBAD database queries, and astrophysical calculations. It features both a CLI-based Python interface and a modern Streamlit web interface for user interaction.

🧠 Key Features
🎙️ Voice Input Recognition
Captures user voice commands using speech_recognition and transcribes them to text.

🌌 Named Entity Recognition (NER)
A custom spaCy model is used to extract celestial object names from natural language input.

🔭 SIMBAD Query Integration
Automatically fetches Right Ascension (RA) and Declination (DEC) data for objects using the astroquery.simbad interface.

🧮 RA/DEC to Alt/Az Conversion
Calculates current Altitude and Azimuth of the object from:

RA / DEC

Local time

Observer’s geolocation

💡 Streamlit Interface
A user-friendly web app to input commands and view object coordinates interactively.

🧱 Architecture Overview
bash
Copy
Edit
astro_app/
├── app.py                         # Streamlit interface
├── main.py                        # CLI interface with live microphone input
├── utils/
│   ├── nlp_utils.py               # NLP and NER parsing
│   ├── simbad_utils.py            # SIMBAD query logic
│   ├── conversion_utils.py        # RA/DEC to degrees
│   └── astro_calculations.py      # Sidereal time & Alt/Az conversion
├── custom_celestial_ner/          # Custom spaCy NER model
├── requirements.txt
🔧 Technologies Used
speech_recognition – Voice command capture

spaCy – Natural Language Processing and NER

astroquery – Celestial data from SIMBAD

astropy – Coordinate conversions and time handling

streamlit – Web app interface

Python standard libraries: datetime, math

🌍 User Location Assumed
The calculations are made assuming observer's location is:

Latitude: 18.5204° N (Pune, India)

Longitude: 73.8567° E

Elevation: 560 meters

This can be adjusted for real-world applications using GPS or manual input.

🚀 How to Run
CLI Version:
bash
Copy
Edit
python main.py
Streamlit Web App:
bash
Copy
Edit
streamlit run app.py
✅ Future Improvements
Integrate real-time telescope control via GPIO or serial interfaces

Add interactive star map visualization

Enable live microphone input in browser (when supported)

Improve multi-language or context-based parsing for complex commands
