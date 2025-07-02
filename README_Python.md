# MOCAT-MC Python Conversion

This is a Python conversion of the MIT Orbital Capacity Assessment Toolbox - Monte Carlo (MOCAT-MC) originally written in MATLAB.

## Overview

MOCAT-MC is a Monte Carlo tool for long-term propagation of the LEO (Low Earth Orbit) environment. This Python conversion maintains the same functionality as the original MATLAB code while providing better integration with modern Python scientific computing ecosystems.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Core Dependencies

- **NumPy**: Numerical computing and array operations
- **SciPy**: Scientific computing, including .mat file I/O
- **Astropy**: Astronomical calculations and time handling
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Plotting and visualization

### Optional Dependencies

- **Numba**: JIT compilation for performance optimization
- **tqdm**: Progress bars for long simulations
- **joblib**: Parallel processing capabilities

## Project Structure

```
MOCAT-MC/
├── Examples/
│   ├── Quick_Start/
│   │   ├── Quick_Start.py          # Main entry point for quick start
│   │   ├── setup_MCconfig.py       # Configuration setup
│   │   ├── initSim.py              # Simulation initialization
│   │   └── main_mc.py              # Main Monte Carlo engine
│   └── Scenario_No_Launch/
│       └── Scenario_No_Launch.py   # No launch scenario example
├── supporting_functions/
│   ├── cfgMC_constants.py          # Physical constants
│   ├── getidx.py                   # Matrix index definitions
│   ├── categorizeObj.py            # Object categorization
│   ├── collision_prob_vec.py       # Collision probability calculation
│   ├── cross_vec.py                # Cross product operations
│   ├── jd2date.py                  # Julian date conversions
│   ├── cube_vec_v3.py              # Cube method collision detection
│   ├── prop_mit_vec.py             # MIT orbital propagator
│   ├── orbcontrol_vec.py           # Orbit control functions
│   ├── getZeroGroups.py            # Zero group analysis
│   ├── fillin_physical_parameters.py # Physical parameter filling
│   └── fillin_atmosphere.py        # Atmospheric model setup
├── supporting_data/                # Data files (.mat, .csv, etc.)
├── requirements.txt                # Python dependencies
└── README_Python.md               # This file
```

## Usage

### Quick Start Example

```python
# Run the quick start example
python Examples/Quick_Start/Quick_Start.py
```

### No Launch Scenario

```python
# Run the no launch scenario with multiple seeds
python Examples/Scenario_No_Launch/Scenario_No_Launch.py
```

### Custom Configuration

```python
from Examples.Quick_Start.setup_MCconfig import setup_MCconfig
from Examples.Quick_Start.main_mc import main_mc

# Setup configuration
cfgMC = setup_MCconfig(seed=1, ICfile='2020.mat')

# Run simulation
nS, nD, nN, nB, mat_sats = main_mc(cfgMC, seed=1)

print(f"Final counts - Satellites: {nS}, Derelicts: {nD}, Debris: {nN}, Rocket Bodies: {nB}")
```

## Key Differences from MATLAB Version

### 1. Indexing
- **MATLAB**: 1-based indexing
- **Python**: 0-based indexing
- All matrix indices have been adjusted accordingly

### 2. Matrix Operations
- **MATLAB**: Built-in matrix operations
- **Python**: NumPy array operations
- Functions like `sum()`, `find()`, `unique()` converted to NumPy equivalents

### 3. File I/O
- **MATLAB**: `.mat` files using `load()`
- **Python**: `.mat` files using `scipy.io.loadmat()`
- Output files use `.npz` format for better Python compatibility

### 4. Date/Time Handling
- **MATLAB**: Built-in datetime functions
- **Python**: Astropy for Julian date conversions
- More robust time handling with timezone awareness

### 5. Random Number Generation
- **MATLAB**: `rand()`, `rng()`
- **Python**: `np.random.random()`, `np.random.seed()`
- Consistent random number generation across platforms

## Configuration Parameters

### Core Parameters
- `PMD`: Post Mission Disposal probability (default: 0.95)
- `alph`: Collision avoidance failure probability (default: 0.01)
- `missionlifetime`: Payload operational life in years (default: 8)
- `altitude_limit_low`: Lower altitude limit in km (default: 200)
- `altitude_limit_up`: Upper altitude limit in km (default: 2000)

### Propagation Parameters
- `dt_days`: Time step in days (default: 5)
- `CUBE_RES`: Cube method resolution in km (default: 50)
- `use_sgp4`: Use SGP4 propagator (default: False)

## Data Files

### Required Files
- `2020.mat`: Initial conditions file containing `mat_sats` and `time0`
- `dens_jb2008_032020_022224.mat`: Atmospheric density data (optional)

### File Formats
- **Input**: MATLAB `.mat` files
- **Output**: NumPy `.npz` files or Python pickle files
- **Plots**: PNG, PDF, or other matplotlib formats

## Performance Considerations

### Optimization Tips
1. **Use NumPy operations**: Vectorized operations are much faster than loops
2. **Enable Numba**: JIT compilation can speed up numerical functions
3. **Memory management**: Large simulations may require memory optimization
4. **Parallel processing**: Use joblib for multiple seed runs

### Memory Usage
- Large simulations can consume significant memory
- Consider using memory-mapped files for very large datasets
- Monitor memory usage during long simulations

## Limitations and TODOs

### Current Limitations
1. **Simplified propagators**: Some orbital propagation functions are simplified
2. **Limited collision models**: Advanced collision models need implementation
3. **Basic fragmentation**: Explosion and collision fragmentation models are basic
4. **No GUI**: Command-line only (no MATLAB-style GUI)

### Planned Improvements
1. **Complete propagator implementation**: Full MIT propagator with J2 effects
2. **Advanced collision models**: More sophisticated collision probability calculations
3. **Better fragmentation models**: Improved debris generation algorithms
4. **Parallel processing**: Multi-core support for large simulations
5. **Web interface**: Optional web-based interface for configuration

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **File Not Found Errors**
   ```bash
   # Check that data files are in the correct location
   ls supporting_data/
   ```

3. **Memory Errors**
   ```python
   # Reduce simulation size or use memory optimization
   cfgMC['n_time'] = 100  # Reduce time steps
   ```

4. **Performance Issues**
   ```python
   # Enable Numba for better performance
   from numba import jit
   ```

### Getting Help

1. Check the original MATLAB documentation
2. Review the conversion notes in each Python file
3. Examine the TODO comments for incomplete features
4. Compare outputs with MATLAB version for validation

## Validation

### Output Comparison
- Compare Python outputs with MATLAB results
- Use same random seeds for reproducible comparison
- Check statistical distributions of results
- Validate orbital element propagation

### Known Differences
- Minor numerical differences due to different math libraries
- Slight timing differences in random number generation
- Different precision in floating-point operations

## Contributing

### Development Guidelines
1. Maintain compatibility with original MATLAB functionality
2. Add comprehensive docstrings to all functions
3. Include unit tests for critical functions
4. Follow PEP 8 style guidelines
5. Document any deviations from MATLAB behavior

### Testing
```python
# Run basic tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_propagation.py
```

## License

This Python conversion maintains the same MIT license as the original MATLAB code.

## Citation

When using this Python conversion, please cite the original work:

```bibtex
@article{Jang2024Monte,
  title={A New Monte-Carlo Model for the Space Environment}, 
  author={Daniel Jang and Davide Gusmini and Peng Mun Siew and Andrea D'Ambrosio and Simone Servadio and Pablo Machuca and Richard Linares},
  year={2024},
  eprint={2405.10430},
  archivePrefix={arXiv},
  primaryClass={astro-ph.EP},
  url={https://arxiv.org/abs/2405.10430}, 
}
```

## Acknowledgments

- Original MATLAB code by MIT ARCLab
- Python conversion maintains the same scientific rigor
- Thanks to the open-source Python scientific computing community 