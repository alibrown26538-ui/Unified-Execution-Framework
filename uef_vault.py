"""
UEF SOVEREIGN PROTOCOL HEADER
Project: Unified Execution Framework (UEF)
Module: Sovereign Vault w/ Fractal Dispersion Audit
"""

import sqlite3
import time

class UEF_Vault:
    def __init__(self, db_name="uef_institutional.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_vault()

    def _initialize_vault(self):
        # We add 'fractal_dispersion' to the schema
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alpha_signals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                hurst_exponent REAL,
                fractal_dispersion REAL,
                liquidity_tax REAL,
                status TEXT
            )
        ''')
        self.conn.commit()

    def record_signal(self, h, dispersion, vol_index):
        """
        The 'Trinity Audit':
        1. Hurst (Trend Strength)
        2. Dispersion (Trend Stability)
        3. Liquidity (Exit Probability)
        """
        liq_tax = vol_index * 0.5
        # Rule: We reject if Dispersion > 0.15 (Trend is too chaotic)
        is_stable = dispersion < 0.15
        is_strong = h > (0.65 + liq_tax)
        
        status = "EXECUTED" if (is_strong and is_stable) else "REJECTED_FRACTAL_CHAOS"
        if not is_strong and is_stable: status = "REJECTED_LIQUIDITY_TRAP"

        print(f"[!] AUDIT: H={h:.2f} | Dispersion={dispersion:.2f} | Tax={liq_tax:.2f}")

        self.cursor.execute('''
            INSERT INTO alpha_signals (timestamp, hurst_exponent, fractal_dispersion, liquidity_tax, status)
            VALUES (?, ?, ?, ?, ?)
        ''', (time.ctime(), h, dispersion, liq_tax, status))
        self.conn.commit()
        print(f"[*] VAULT: Status -> {status}")

if __name__ == "__main__":
    vault = UEF_Vault()
    print("--- INITIATING FRACTAL DISPERSION VAULT ---")
    
    # Scenario: High Alpha (0.80) but High Dispersion (0.25) -> Chaos
    vault.record_signal(0.80, 0.25, 0.10)
    
    # Scenario: Solid Alpha (0.75) and Low Dispersion (0.05) -> Pure Alpha
    vault.record_signal(0.75, 0.05, 0.05)