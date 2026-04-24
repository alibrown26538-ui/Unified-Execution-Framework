"""
UEF SOVEREIGN PROTOCOL HEADER
Project: Unified Execution Framework (UEF)
Module: Trinity Audit Simulation (Hurst, Dispersion, Liquidity)
Intent: Institutional Portfolio Visualization
"""

import matplotlib.pyplot as plt
import numpy as np

def run_trinity_simulation():
    # 1. Setup Time-Series (Market Micro-steps)
    steps = 200
    x = np.arange(steps)
    
    # 2. Simulate Hurst (Trend Confidence)
    h_values = 0.5 + 0.35 * np.sin(x / 15)
    
    # 3. Simulate Fractal Dispersion (The 'Chaos' Factor)
    dispersion = 0.05 + 0.25 * np.random.normal(0, 0.05, steps).cumsum()
    dispersion = np.clip(np.abs(dispersion), 0.02, 0.3) 
    
    # 4. Simulate Volatility (The Risk Tax / Boyle Filter)
    volatility = 0.1 + 0.5 * (np.sin(x / 30) > 0.5) 
    thresholds = 0.65 + (volatility * 0.5)
    
    # 5. THE TRINITY LOGIC GATE: 
    # Must have High Hurst, Low Dispersion, and Clear Risk Floor
    gate_open = (h_values > thresholds) & (dispersion < 0.15)

    # 6. RENDER THE FORTRESS STATE
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Plot 1: Trend vs. Risk Tax
    ax1.plot(x, h_values, label='UEF Signal (Hurst)', color='cyan', lw=2)
    ax1.plot(x, thresholds, label='Boyle Risk Floor', color='red', ls='--')
    ax1.fill_between(x, 0.4, 1.0, where=gate_open, color='lime', alpha=0.3, label='ACTIVE EXECUTION')
    ax1.set_title("UEF Phase 5: Risk-Adjusted Execution Layer")
    ax1.legend(loc='upper right')
    ax1.grid(alpha=0.2)

    # Plot 2: Fractal Dispersion (Chaos Audit)
    ax2.plot(x, dispersion, label='Fractal Dispersion (Chaos)', color='magenta', lw=1.5)
    ax2.axhline(0.15, color='orange', ls=':', label='Chaos Limit (Rejection Threshold)')
    ax2.set_ylabel("Chaos Index")
    ax2.set_xlabel("Market Micro-Steps")
    ax2.legend(loc='upper right')
    ax2.grid(alpha=0.2)
    
    plt.tight_layout()
    print("[*] SIMULATION COMPLETE: Saving 'uef_trinity_audit.png' to disk.")
    plt.savefig('uef_trinity_audit.png')
    plt.show()

if __name__ == "__main__":
    run_trinity_simulation()