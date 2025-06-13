from astroquery.simbad import Simbad

def fetch_celestial_object_coordinates(object_name):
    try:
        result_table = Simbad.query_object(object_name)
        if result_table:
            print(f"[DEBUG] SIMBAD returned columns: {result_table.colnames}")
            
            # Ensure RA and DEC exist
            if 'RA' in result_table.colnames and 'DEC' in result_table.colnames:
                ra = result_table['RA'][0]
                dec = result_table['DEC'][0]
                print(f"[DEBUG] Fetched coordinates - RA: {ra}, DEC: {dec}")
                return {"RA": ra, "DEC": dec}
            else:
                print("[ERROR] RA or DEC column missing in SIMBAD response.")
                return None
        else:
            print(f"[ERROR] No result for object '{object_name}'")
            return None
    except Exception as e:
        print(f"[ERROR] Error fetching data from SIMBAD: {e}")
        return None
