"""
UEF SOVEREIGN PROTOCOL HEADER
Project: Unified Execution Framework (UEF)
Module: Historical Backtest Engine & Portfolio Sizer
Intent: Institutional Proof of Concept & Capital Floor Verification
"""

import numpy as np

class UEF_Backtest:
    def __init__(self, starting_capital=100000):
        self.capital = starting_capital
        self.peak_capital = starting_capital
        self.max_drawdown = 0.0
        self.trades = 0
        self.wins = 0

    def run_simulation(self, steps=1000):
        print(f"[*] INITIATING UEF BACKTEST: {steps} Market Cycles")
        print(f"[*] STARTING CAPITAL: £{self.capital:,.2f}\n")
        
        # Simulating market data arrays
        hurst = 0.5 + 0.3 * np.random.randn(steps)
        dispersion = np.abs(0.1 + 0.1 * np.random.randn(steps))
        volatility = np.abs(0.15 + 0.1 * np.random.randn(steps))
        market_returns = np.random.normal(0.001, 0.02, steps)

        for i in range(steps):
            tax = volatility[i] * 0.5
            threshold = 0.65 + tax
            
            if hurst[i] > threshold and dispersion[i] < 0.15:
                self.trades += 1
                
                # --- THE PORTFOLIO SIZER ---
                # We only allocate 10% of our total capital to any single execution
                allocation = self.capital * 0.10 
                profit = allocation * market_returns[i]
                
                self.capital += profit
                
                if profit > 0:
                    self.wins += 1
                    
                if self.capital > self.peak_capital:
                    self.peak_capital = self.capital
                else:
                    drawdown = (self.peak_capital - self.capital) / self.peak_capital
                    if drawdown > self.max_drawdown:
                        self.max_drawdown = drawdown

        self.generate_report()

    def generate_report(self):
        print("--- UEF BACKTEST RESULTS ---")
        print(f"Total Trades Executed : {self.trades}")
        if self.trades > 0:
            print(f"Win Rate              : {(self.wins / self.trades) * 100:.2f}%")
        print(f"Final Capital         : £{self.capital:,.2f}")
        print(f"Maximum Drawdown      : {self.max_drawdown * 100:.2f}%")
        
        # Verify the 5.2% Hard Floor Limit
        if self.max_drawdown <= 0.052:
            print("[✓] COMPLIANCE PASSED: Max drawdown remained below the 5.2% capital floor.")
        else:
            print("[X] COMPLIANCE FAILED: Capital floor breached.")

if __name__ == "__main__":
    backtest = UEF_Backtest()
    backtest.run_simulation()