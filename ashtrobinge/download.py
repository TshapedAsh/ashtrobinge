"""
ashtrobinge.download
--------------------
Professional yet slightly meme-flavored data downloaders for astronomy bingers.

Currently supports Gaia. Extendable for more surveys. Code so clean, even your PI would binge it.
"""

from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
import astropy.units as u

def download_gaia(target='M31', radius=0.2):
    """
    Download Gaia sources around a target using a cone search.

    Parameters
    ----------
    target : str or tuple(float, float)
        Name of the target object (e.g., 'M31'), or (RA, Dec) in degrees.
    radius : float
        Search radius in degrees. More radius = more stars = more binging.

    Returns
    -------
    result : astropy.table.Table
        Table of Gaia sources found. Data worth losing sleep over.
    """
    # Convert target to coordinates: supports names or (RA, Dec) input
    if isinstance(target, str):
        coord = SkyCoord.from_name(target)
    elif isinstance(target, (tuple, list)) and len(target) == 2:
        coord = SkyCoord(ra=target[0], dec=target[1], unit=(u.deg, u.deg))
    else:
        raise ValueError(
            "target must be an object name (str) or (RA, Dec) tuple in degrees. "
            "Don't make it weird, bro."
        )

    # Search Gaia using a cone search
    print(f"[Ashtrobinge] Binging Gaia data for {target} within {radius}° ...")
    job = Gaia.cone_search_async(coord, radius * u.deg)
    result = job.get_results()
    print(f"[Ashtrobinge] Downloaded {len(result)} Gaia sources near {target}. That's a lotta stars!")

    return result
