#!/usr/bin/env python3
"""
Simple test script for MOCAT-MC Python conversion
Tests core functionality with minimal dependencies
"""

import sys
import os

sys.path.append('supporting_functions')

def test_basic_imports():
    """Test basic imports"""
    print("Testing basic imports...")
    
    try:
        import numpy as np
        print("✓ NumPy imported successfully")
    except ImportError as e:
        print(f"✗ NumPy import failed: {e}")
        return False
    
    return True

def test_constants():
    """Test configuration constants"""
    print("\nTesting configuration constants...")
    
    try:
        from cfgMC_constants_simple import get_cfgMC_constants
        cfg = get_cfgMC_constants()
        
        assert cfg['radiusearthkm'] == 6378.137
        assert cfg['mu_const'] == 398600.4418
        assert cfg['DAY2MIN'] == 1440
        
        print("✓ Configuration constants loaded correctly")
        print(f"  Earth radius: {cfg['radiusearthkm']} km")
        print(f"  Earth mu: {cfg['mu_const']} km³/s²")
        print(f"  Days to minutes: {cfg['DAY2MIN']}")
        
    except Exception as e:
        print(f"✗ Constants test failed: {e}")
        return False
    
    return True

def test_indexing():
    """Test indexing functions"""
    print("\nTesting indexing functions...")
    
    try:
        from getidx import idx_a, idx_ecco, idx_inclo, idx_nodeo, idx_argpo, idx_mo
        
        indices = [idx_a, idx_ecco, idx_inclo, idx_nodeo, idx_argpo, idx_mo]
        for i, idx in enumerate(['a', 'e', 'i', 'raan', 'argp', 'm0']):
            assert isinstance(indices[i], int), f"{idx} should be integer"
        
        print("✓ Indexing constants defined correctly")
        print(f"  a: {idx_a}, e: {idx_ecco}, i: {idx_inclo}")
        print(f"  raan: {idx_nodeo}, argp: {idx_argpo}, m0: {idx_mo}")
        
    except Exception as e:
        print(f"✗ Indexing test failed: {e}")
        return False
    
    return True

def test_date_conversion():
    """Test Julian date conversion"""
    print("\nTesting date conversion...")
    
    try:
        from jd2date_simple import jd2date_simple
        
        jd = 2451545.0
        year, month, day = jd2date_simple(jd)
        
        assert year == 2000
        assert month == 1
        assert day == 1
        
        print("✓ Date conversion working correctly")
        print(f"  JD {jd} = {year}-{month:02d}-{day:02d}")
        
    except Exception as e:
        print(f"✗ Date conversion test failed: {e}")
        return False
    
    return True

def test_vector_operations():
    """Test vector operations"""
    print("\nTesting vector operations...")
    
    try:
        import numpy as np
        from cross_vec import cross_vec
        
        a = np.array([[1, 0, 0]])
        b = np.array([[0, 1, 0]])
        c = cross_vec(a, b)
        
        expected = np.array([[0, 0, 1]])
        assert np.allclose(c, expected), f"Cross product failed: {c} != {expected}"
        
        print("✓ Vector operations working correctly")
        print(f"  [1,0,0] × [0,1,0] = {c.flatten()}")
        
    except Exception as e:
        print(f"✗ Vector operations test failed: {e}")
        return False
    
    return True

def test_collision_probability():
    """Test collision probability calculation"""
    print("\nTesting collision probability...")
    
    try:
        import numpy as np
        from collision_prob_vec import collision_prob_vec
        
        p1_radius = np.array([1000])
        p1_v = np.array([[0, 7.5, 0]])
        p2_radius = np.array([1000])
        p2_v = np.array([[0, 7.5, 0]])
        CUBE_RES = 10.0
        
        prob = collision_prob_vec(p1_radius, p1_v, p2_radius, p2_v, CUBE_RES)
        
        assert prob[0] >= 0, f"Collision probability should be non-negative: {prob}"
        
        print("✓ Collision probability calculation working")
        print(f"  Collision probability: {prob[0]:.6f}")
        
    except Exception as e:
        print(f"✗ Collision probability test failed: {e}")
        return False
    
    return True

def test_object_categorization():
    """Test object categorization"""
    print("\nTesting object categorization...")
    
    try:
        import numpy as np
        from categorizeObj import categorizeObj
        
        objint_st = np.array([1, 1, 3, 5])
        cont_st = np.array([1, 0, 0, 0])
        
        nS, nD, nN, nB = categorizeObj(objint_st, cont_st)
        
        assert nS == 1, f"Expected 1 satellite, got {nS}"
        assert nD == 1, f"Expected 1 derelict, got {nD}"
        assert nN == 1, f"Expected 1 debris, got {nN}"
        assert nB == 1, f"Expected 1 rocket body, got {nB}"
        
        print("✓ Object categorization working correctly")
        print(f"  Satellites: {nS}, Derelicts: {nD}, Debris: {nN}, Rocket bodies: {nB}")
        
    except Exception as e:
        print(f"✗ Object categorization test failed: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("MOCAT-MC Python Conversion - Simple Test")
    print("=" * 50)
    
    tests = [
        test_basic_imports,
        test_constants,
        test_indexing,
        test_date_conversion,
        test_vector_operations,
        test_collision_probability,
        test_object_categorization
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n==================================================")
    print(f"Test Results: {passed}/{total} tests passed")
    if passed == total:
        print("✓ All tests passed! Core functionality is working.")
    else:
        print("✗ Some tests failed. Check the output above.")
    
    return passed == total

if __name__ == "__main__":
    main()
