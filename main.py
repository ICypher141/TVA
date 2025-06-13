import speech_recognition as sr
from utils.nlp_utils import parse_command
from utils.simbad_utils import fetch_celestial_object_coordinates
from utils.conversion_utils import convert_ra_dec_to_degrees
from utils.astro_calculations import calculate_lst, calculate_hour_angle, calculate_alt_az
from datetime import datetime, timezone

# Global dictionary to store coordinates
celestial_coordinates = {}

def listen_and_recognize():
    recognizer = sr.Recognizer()

    print("[INFO] Preparing microphone...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("[INFO] Listening for your command (max 5s)...")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("[INFO] Recognizing speech...")
            command = recognizer.recognize_google(audio)
            print(f"[RESULT] You said: '{command}'")

            # NLP Parsing
            print("[INFO] Parsing intent and object...")
            intent, object_name = parse_command(command)
            print(f"[DEBUG] Intent: {intent}, Object: {object_name}")

            if object_name:
                print(f"[INFO] Querying SIMBAD for '{object_name}'...")
                coords = fetch_celestial_object_coordinates(object_name)

                if coords:
                    print(f"[DEBUG] SIMBAD RA: {coords['RA']}, Dec: {coords['DEC']}")
                    ra_deg, dec_deg = convert_ra_dec_to_degrees(coords['RA'], coords['DEC'])
                    celestial_coordinates["RA_deg"] = ra_deg
                    celestial_coordinates["Dec_deg"] = dec_deg

                    print(f"[RESULT] {object_name} → RA: {ra_deg:.4f}°, Dec: {dec_deg:.4f}°")

                    # Alt-Az Conversion
                    print("[INFO] Calculating Altitude and Azimuth...")
                    latitude = 18.5204
                    longitude = 73.8567
                    now = datetime.now(timezone.utc)

                    lst = calculate_lst(longitude, now)
                    ha = calculate_hour_angle(lst, ra_deg)
                    alt, az = calculate_alt_az(latitude, dec_deg, ha)

                    print(f"[RESULT] Altitude: {alt:.2f}°, Azimuth: {az:.2f}°")

                else:
                    print(f"[ERROR] '{object_name}' not found in SIMBAD.")
            else:
                print("[ERROR] Could not understand the object or intent.")

        except sr.WaitTimeoutError:
            print("[ERROR] Listening timed out — no speech detected.")
        except sr.UnknownValueError:
            print("[ERROR] Could not understand the audio.")
        except sr.RequestError as e:
            print(f"[ERROR] Google Speech Recognition failed: {e}")
        except Exception as e:
            print(f"[ERROR] Unexpected failure: {e}")

if __name__ == "__main__":
    print("[INFO] Starting Celestial Object Assistant...")
    listen_and_recognize()
