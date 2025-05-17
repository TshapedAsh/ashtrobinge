"""
Ashtrobinge: A meme-powered, ultra-fast astro data wrangling toolkit.
Built by Ash, powered by caffeine and questionable decisions.
"""

__version__ = "0.1.0"
__author__ = "Ash"

def hello_binge():
    print("🚀 Welcome to Ashtrobinge! Ready to binge the cosmos and roast your data? Let’s goon.")

def download(survey='Gaia', target=None, coords=None, radius=1.0):
    """
    Download data from Gaia using astroquery (universal version).
    """
    try:
        from astroquery.gaia import Gaia
        from astropy.coordinates import SkyCoord
    except ImportError:
        print("astroquery/astropy not installed. Please pip install astroquery astropy.")
        return None

    if survey.lower() == 'gaia':
        if target:
            print(f"[Ashtrobinge] Binging Gaia stars around '{target}' (radius: {radius} deg)...")
            coord = SkyCoord.from_name(target)
            coord_string = f"{coord.ra.deg} {coord.dec.deg}"
        elif coords:
            ra, dec = coords
            coord_string = f"{ra} {dec}"
            print(f"[Ashtrobinge] Binging Gaia stars at RA={ra}, Dec={dec} (radius: {radius} deg)...")
        else:
            print("Please provide a target name or coordinates.")
            return None

        job = Gaia.cone_search_async(coord_string, radius)
        result = job.get_results()
        print(f"[Ashtrobinge] Downloaded {len(result)} stars. Data secured.")
        return result
    else:
        print("Currently only Gaia is supported in this demo.")
        return None

# --- Rest of your code (clean, plot, meme_log) unchanged! ---

def clean(data, dropna=True):
    try:
        import pandas as pd
    except ImportError:
        print("pandas not installed. Please pip install pandas.")
        return data

    print("[Ashtrobinge] Cleaning data... Don’t let those NaNs ruin your binge.")
    if hasattr(data, "to_pandas"):
        df = data.to_pandas()
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        print("Input must be astropy Table or pandas DataFrame.")
        return data

    if dropna:
        df = df.dropna()
    return df

def plot(plot_type, data, x=None, y=None):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed. Please pip install matplotlib.")
        return

    if plot_type.lower() == 'cmd':
        if 'bp_rp' in data and 'phot_g_mean_mag' in data:
            print("[Ashtrobinge] Plotting your CMD... Art, but make it science.")
            plt.figure(figsize=(6,8))
            plt.scatter(data['bp_rp'], data['phot_g_mean_mag'], s=1, alpha=0.5, color='blue')
            plt.gca().invert_yaxis()
            plt.xlabel('BP - RP')
            plt.ylabel('G mag')
            plt.title('Color-Magnitude Diagram (CMD)')
            plt.show()
        else:
            print("Data must have 'bp_rp' and 'phot_g_mean_mag' columns for CMD.")
    elif plot_type.lower() == 'scatter' and x and y:
        print(f"[Ashtrobinge] Plotting scatter: {x} vs {y}. Yeet those points!")
        plt.figure(figsize=(6,4))
        plt.scatter(data[x], data[y], s=5, alpha=0.6, color='navy')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"{x} vs {y}")
        plt.show()
    else:
        print("Plot type not recognized or insufficient data/arguments.")

def meme_log(level='info'):
    import random
    messages = {
        'info': [
            "Still binging, still winning.",
            "Science is pain, but you like it.",
            "Achievement unlocked: Data hoarder.",
            "If this crashes, it's probably your fault (JK)."
        ],
        'success': [
            "You did it. Nobel soon?",
            "Science flex complete.",
            "Big W for the goon squad.",
            "Your ancestors are proud."
        ],
        'fail': [
            "Bruh. Try again.",
            "404: Science not found.",
            "Data left the chat.",
            "This ain't it, chief."
        ]
    }
    print(random.choice(messages.get(level, messages['info'])))
