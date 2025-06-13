from math import sin, cos, asin, radians, degrees, atan2 , tan
from datetime import datetime, timezone

def calculate_lst(longitude, current_time):
    JD = (current_time - datetime(2000, 1, 1, 12, tzinfo=timezone.utc)).total_seconds() / 86400 + 2451545.0
    T = (JD - 2451545.0) / 36525.0
    GMST = 280.46061837 + 360.98564736629 * (JD - 2451545.0) + T**2 * (0.000387933 - T / 38710000.0)
    GMST = GMST % 360.0
    return (GMST + longitude) % 360.0

def calculate_hour_angle(lst, ra):
    ha = (lst - ra) % 360.0
    return ha if ha <= 180 else ha - 360

def calculate_alt_az(latitude, declination, ha):
    lat_rad = radians(latitude)
    dec_rad = radians(declination)
    ha_rad = radians(ha)

    alt_rad = asin(sin(lat_rad) * sin(dec_rad) + cos(lat_rad) * cos(dec_rad) * cos(ha_rad))
    alt = degrees(alt_rad)

    y = -sin(ha_rad)
    x = tan(dec_rad) * cos(lat_rad) - sin(lat_rad) * cos(ha_rad)
    az = (degrees(atan2(y, x)) + 360) % 360

    return alt, az
