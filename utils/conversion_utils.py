from astropy.coordinates import SkyCoord
import astropy.units as u

def convert_ra_dec_to_degrees(ra, dec):
    coord = SkyCoord(ra=ra, dec=dec, unit=(u.hourangle, u.deg))
    return coord.ra.deg, coord.dec.deg
