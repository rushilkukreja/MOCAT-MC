
import pandas as pd
import numpy as np
from pathlib import Path

def load_density_data():
    """
    Load the JB2008 density data from CSV file.
    
    Returns:
        pandas.DataFrame: DataFrame with columns:
            - year: Year (2020-2024)
            - month: Month (1-12)
            - alt_0 to alt_35: Density values for 36 altitude levels
    """
    csv_file = Path(__file__).parent / "dens_jb2008_032020_022224.csv"
    if not csv_file.exists():
        raise FileNotFoundError(f"Density data file not found: {csv_file}")
    
    return pd.read_csv(csv_file)

def get_density_at_altitude_time(year, month, altitude_level):
    """
    Get density value for specific year, month, and altitude level.
    
    Args:
        year (int): Year (2020-2024)
        month (int): Month (1-12)
        altitude_level (int): Altitude level (0-35)
    
    Returns:
        float: Density value in kg/m³
    """
    df = load_density_data()
    mask = (df['year'] == year) & (df['month'] == month)
    if not mask.any():
        raise ValueError(f"No data found for year {year}, month {month}")
    
    col_name = f'alt_{altitude_level}'
    if col_name not in df.columns:
        raise ValueError(f"Altitude level {altitude_level} not found. Available: 0-35")
    
    return df.loc[mask, col_name].iloc[0]

def get_density_profile(year, month):
    """
    Get density profile for all altitude levels at specific time.
    
    Args:
        year (int): Year (2020-2024)
        month (int): Month (1-12)
    
    Returns:
        numpy.ndarray: Array of 36 density values for all altitude levels
    """
    df = load_density_data()
    mask = (df['year'] == year) & (df['month'] == month)
    if not mask.any():
        raise ValueError(f"No data found for year {year}, month {month}")
    
    row = df[mask].iloc[0]
    density_values = []
    for i in range(36):
        density_values.append(row[f'alt_{i}'])
    
    return np.array(density_values)

def get_time_series(altitude_level):
    """
    Get density time series for a specific altitude level.
    
    Args:
        altitude_level (int): Altitude level (0-35)
    
    Returns:
        pandas.Series: Time series of density values
    """
    df = load_density_data()
    col_name = f'alt_{altitude_level}'
    if col_name not in df.columns:
        raise ValueError(f"Altitude level {altitude_level} not found. Available: 0-35")
    
    return df[col_name]

def get_available_times():
    """
    Get list of available time points.
    
    Returns:
        list: List of tuples (year, month)
    """
    df = load_density_data()
    return list(zip(df['year'], df['month']))

def get_altitude_levels():
    """
    Get number of altitude levels.
    
    Returns:
        int: Number of altitude levels (36)
    """
    return 36

# Example usage
if __name__ == "__main__":
    print("JB2008 Density Data Module")
    print("=" * 30)
    
    # Load data
    df = load_density_data()
    print(f"Data shape: {df.shape}")
    print(f"Time range: {df['year'].min()}-{df['year'].max()}")
    print(f"Altitude levels: {get_altitude_levels()}")
    
    # Example: Get density for March 2020 at altitude level 0
    try:
        density = get_density_at_altitude_time(2020, 3, 0)
        print(f"Density for March 2020, altitude level 0: {density:.2e} kg/m³")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example: Get density profile for March 2020
    try:
        profile = get_density_profile(2020, 3)
        print(f"Density profile for March 2020 (first 5 values): {profile[:5]}")
    except Exception as e:
        print(f"Error: {e}") 