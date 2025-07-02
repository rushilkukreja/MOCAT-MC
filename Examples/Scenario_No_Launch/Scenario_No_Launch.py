#!/usr/bin/env python3
"""
Scenario No Launch
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_data'))
sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_functions'))
sys.path.append(str(Path(__file__).parent.parent / 'Quick_Start'))

from setup_MCconfig import setup_MCconfig
from main_mc import main_mc

def scenario_no_launch():
    """Main Scenario No Launch function"""
    print("Scenario No Launch")
    
    ICfile = str(Path(__file__).parent.parent.parent / 'supporting_data' / 'TLEhistoric' / '2020.mat')
    
    t = np.arange(1, 362, 5)
    deorbit_list_m = np.zeros((3, 730))
    
    for idx in range(3):
        seed = idx + 1
        
        print('MC configuration starting...')
        cfgMC = setup_MCconfig(seed, ICfile)
        print(f'Seed {seed}')
        
        print(f'Initial Population: {cfgMC["mat_sats"].shape[0]} sats')
        print(f'Launches per year: {cfgMC["repeatLaunches"].shape[0] if cfgMC["repeatLaunches"].size > 0 else 0}')
        print('Starting main_mc...')
        
        nS, nD, nN, nB, deorbitlist_r = main_mc(cfgMC, seed)
        deorbit_list_m[idx, :] = deorbitlist_r
    
    plt.figure(figsize=(10, 6))
    time_years = np.linspace(2020, 2030, 730)
    
    plt.plot(time_years, deorbit_list_m[0, :], linewidth=2, label="Seed 1")
    plt.plot(time_years, deorbit_list_m[1, :], linewidth=2, label="Seed 2")
    plt.plot(time_years, deorbit_list_m[2, :], linewidth=2, label="Seed 3")
    
    plt.legend()
    plt.xlabel("Time (Year)")
    plt.ylabel("Decayed Objects")
    plt.title("Population Evolution")
    plt.xlim([2020, 2030])
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('population_evolution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("Scenario No Launch completed!")

if __name__ == "__main__":
    scenario_no_launch() 