"""
UEF SOVEREIGN PROTOCOL HEADER
Project: Unified Execution Framework (UEF)
Module: [Telemetry Ingest Bridge]
Security Level: Proprietary / Research
Compliance: UK/US Cyber-Security Standard

NOTICE: This code is the intellectual property of Alisdair Brown.
Unauthorized distribution or malicious modification is prohibited.
Intent: Ethical Alpha Extraction & Systemic Resiliency.
"""
import yfinance as yf
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - UEF INGEST - %(message)s')

class TelemetryIngest:
    """
    UEF Infrastructure Module: Telemetry Ingest
    -------------------------------------------
    Automates the acquisition, cleaning, and normalization of 
    historical market data for the xi (ξ) Telemetry engine.
    """

    def __init__(self, ticker: str):
        self.ticker = ticker
        self.raw_data = None
        self.clean_data = None

    def fetch_historical(self, period: str = "2y", interval: str = "1d"):
        """Fetches data from Yahoo Finance API."""
        logging.info(f"Ingesting historical data for {self.ticker}...")
        self.raw_data = yf.download(self.ticker, period=period, interval=interval)
        return self.raw_data

    def cleanse_telemetry(self):
        """Removes NaN values and normalizes for covariance analysis."""
        if self.raw_data is None:
            return None
        
        # Calculate Log Returns for non-linear stochastic analysis
        df = self.raw_data.copy()
        df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
        
        # Calculate Volatility (Standard Deviation of Returns)
        df['Volatility'] = df['Log_Return'].rolling(window=20).std()
        
        self.clean_data = df.dropna()
        logging.info(f"Cleansing complete. {len(self.clean_data)} telemetry nodes ready.")
        return self.clean_data

if __name__ == "__main__":
    # Internal module self-test
    ingestor = TelemetryIngest("GBPUSD=X") # Testing with the Pound
    raw = ingestor.fetch_historical()
    clean = ingestor.clean_cleansing()
    print(clean.head())
