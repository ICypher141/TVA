import streamlit as st
from utils.nlp_utils import parse_command
from utils.simbad_utils import fetch_celestial_object_coordinates
from utils.conversion_utils import convert_ra_dec_to_degrees
from utils.astro_calculations import calculate_lst, calculate_hour_angle, calculate_alt_az
from datetime import datetime, timezone

st.title("🔭 Celestial Object Locator")

# Optional: Allow user to type or speak a command
command = st.text_input("Enter a voice-like command (e.g., 'Show me Sirius')")

if command:
    st.write(f"🔎 You said: `{command}`")

    intent, object_name = parse_command(command)
    if object_name:
        st.write(f"🪐 Parsed Object: `{object_name}`")

        coords = fetch_celestial_object_coordinates(object_name)
        if coords:
            st.success(f"SIMBAD found: RA = {coords['RA']}, DEC = {coords['DEC']}")

            ra_deg, dec_deg = convert_ra_dec_to_degrees(coords['RA'], coords['DEC'])

            latitude = 18.5204
            longitude = 73.8567
            now = datetime.now(timezone.utc)

            lst = calculate_lst(longitude, now)
            ha = calculate_hour_angle(lst, ra_deg)
            alt, az = calculate_alt_az(latitude, dec_deg, ha)

            st.write(f"📌 Coordinates in degrees: RA = {ra_deg:.2f}°, DEC = {dec_deg:.2f}°")
            st.write(f"🧭 Altitude: {alt:.2f}°, Azimuth: {az:.2f}°")
        else:
            st.error(f"Could not find `{object_name}` in SIMBAD.")
    else:
        st.warning("Could not understand the celestial object in the command.")
