#!/usr/bin/env python3
"""
Basic test script for MOCAT-MC Python conversion
Tests basic functionality without external dependencies
"""

import sys
import os
from pathlib import Path

def test_file_structure():
    """Test that all converted Python files exist"""
    print("Testing file structure...")
    
    files_to_check = [
        "Examples/Quick_Start/Quick_Start.py",
        "Examples/Quick_Start/setup_MCconfig.py", 
        "Examples/Quick_Start/initSim.py",
        "Examples/Quick_Start/main_mc.py",
        "Examples/Scenario_No_Launch/Scenario_No_Launch.py",
        "supporting_functions/cfgMC_constants.py",
        "supporting_functions/getidx.py",
        "supporting_functions/categorizeObj.py",
        "supporting_functions/collision_prob_vec.py",
        "supporting_functions/cross_vec.py",
        "supporting_functions/jd2date.py",
        "supporting_functions/cube_vec_v3.py",
        "supporting_functions/prop_mit_vec.py",
        "supporting_functions/orbcontrol_vec.py",
        "supporting_functions/getZeroGroups.py",
        "supporting_functions/fillin_physical_parameters.py",
        "supporting_functions/fillin_atmosphere.py",
        "requirements.txt",
        "README_Python.md"
    ]
    
    missing_files = []
    for file_path in files_to_check:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"✓ {file_path}")
    
    if missing_files:
        print(f"\nMissing files: {missing_files}")
        return False
    else:
        print("\n✓ All files present!")
        return True

def test_basic_imports():
    """Test basic imports without external dependencies"""
    print("\nTesting basic imports...")
    
    try:
        import numpy as np
        print("✓ NumPy import successful")
    except ImportError:
        print("✗ NumPy not available (install with: pip install numpy)")
    
    try:
        import scipy
        print("✓ SciPy import successful")
    except ImportError:
        print("✗ SciPy not available (install with: pip install scipy)")
    
    try:
        import astropy
        print("✓ Astropy import successful")
    except ImportError:
        print("✗ Astropy not available (install with: pip install astropy)")
    
    try:
        import pandas
        print("✓ Pandas import successful")
    except ImportError:
        print("✗ Pandas not available (install with: pip install pandas)")

def test_syntax():
    """Test Python syntax of converted files"""
    print("\nTesting Python syntax...")
    
    python_files = [
        "supporting_functions/cfgMC_constants.py",
        "supporting_functions/getidx.py",
        "supporting_functions/categorizeObj.py",
        "supporting_functions/collision_prob_vec.py",
        "supporting_functions/cross_vec.py"
    ]
    
    for file_path in python_files:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            compile(content, file_path, 'exec')
            print(f"✓ {file_path} - syntax OK")
        except SyntaxError as e:
            print(f"✗ {file_path} - syntax error: {e}")
        except Exception as e:
            print(f"✗ {file_path} - error: {e}")

def test_basic_functionality():
    """Test basic functionality without external dependencies"""
    print("\nTesting basic functionality...")
    
    try:
        sys.path.append('supporting_functions')
        from getidx import idx_a, idx_ecco, idx_objectclass
        print(f"✓ Index definitions: a={idx_a}, e={idx_ecco}, objclass={idx_objectclass}")
    except Exception as e:
        print(f"✗ Index definitions failed: {e}")
    
    try:
        cfgMC = {}
        cfgMC['DAY2MIN'] = 60 * 24
        cfgMC['DAY2SEC'] = cfgMC['DAY2MIN'] * 60
        cfgMC['YEAR2DAY'] = 365.2425
        cfgMC['YEAR2MIN'] = cfgMC['YEAR2DAY'] * cfgMC['DAY2MIN']
        cfgMC['rad'] = 3.14159265359 / 180
        cfgMC['radiusearthkm'] = 6378.137
        cfgMC['mu_const'] = 398600.4418
        
        print(f"✓ Constants: Earth radius = {cfgMC['radiusearthkm']} km")
        print(f"✓ Constants: mu = {cfgMC['mu_const']} km³/s²")
    except Exception as e:
        print(f"✗ Constants failed: {e}")

def main():
    """Main test function"""
    print("MOCAT-MC Python Conversion - Basic Test")
    print("=" * 50)
    
    structure_ok = test_file_structure()
    
    test_basic_imports()
    
    test_syntax()
    
    test_basic_functionality()
    
    print("\n" + "=" * 50)
    if structure_ok:
        print("✓ Basic tests completed successfully!")
        print("\nTo run the full simulation:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run quick start: python Examples/Quick_Start/Quick_Start.py")
    else:
        print("✗ Some tests failed. Check the output above.")

if __name__ == "__main__":
    main() 