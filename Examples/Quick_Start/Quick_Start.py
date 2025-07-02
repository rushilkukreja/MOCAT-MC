import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_data'))
sys.path.append(str(Path(__file__).parent.parent.parent / 'supporting_functions'))

from setup_MCconfig import setup_MCconfig
from main_mc import main_mc

def quick_start():
    """Main Quick Start function"""
    print("Quick Start")
    
    ICfile = str(Path(__file__).parent.parent.parent / 'supporting_data' / 'TLEhistoric' / '2020.mat')
    
    seed = 1
    
    print('MC configuration starting...')
    cfgMC = setup_MCconfig(seed, ICfile)
    print(f'Seed {seed}')
    
    print(f'Initial Population: {cfgMC["mat_sats"].shape[0]} sats')
    print(f'Launches per year: {cfgMC["repeatLaunches"].shape[0] if cfgMC["repeatLaunches"].size > 0 else 0}')
    print('Starting main_mc...')
    
    nS, nD, nN, nB, deorbitlist_r, satellites_over_time, derelicts_over_time, debris_over_time, rocket_bodies_over_time = main_mc(cfgMC, seed)
    
    ratio = nS / (nS + nD + nN + nB)
    print('Quick Start under no launch scenario done!')
    print(f'Satellite ratio in all space objects after evolution: {ratio:.6f}')
    
    plt.figure(figsize=(12, 8))
    
    time_years = np.linspace(2020, 2030, len(satellites_over_time))
    
    plt.subplot(2, 1, 1)
    plt.plot(time_years, satellites_over_time, linewidth=2, color='blue', label='Satellites')
    plt.xlabel("Time (Year)")
    plt.ylabel("Number of Satellites")
    plt.title("Satellite Population Evolution")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(time_years, satellites_over_time, linewidth=2, color='blue', label='Satellites')
    plt.plot(time_years, derelicts_over_time, linewidth=2, color='red', label='Derelicts')
    plt.plot(time_years, debris_over_time, linewidth=2, color='green', label='Debris')
    plt.plot(time_years, rocket_bodies_over_time, linewidth=2, color='orange', label='Rocket Bodies')
    plt.xlabel("Time (Year)")
    plt.ylabel("Number of Objects")
    plt.title("All Object Types Evolution")
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    
    plt.savefig('quick_start_evolution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"Plot saved as 'quick_start_evolution.png'")

if __name__ == "__main__":
    quick_start() 