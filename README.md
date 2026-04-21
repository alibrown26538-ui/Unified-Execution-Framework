# **Unified Execution Framework (UEF)**
**Author:** Alisdair Brown 
**Status:** Out-of-Sample Verified (WorldQuant BRAIN - Bronze Tier)

## **Executive Summary**
The UEF is a proprietary quantitative architecture designed to identify and extract asymmetric yield from structural market inefficiencies. Moving beyond standard price-action retail indicators, this framework utilizes a multi-regime approach, dynamically weighting **Institutional Sentiment Divergence**, Volumetric Momentum, and Price Action to pinpoint high-probability institutional entry vectors.

## **Core Architecture: The Uniform Trifecta**
The logic engine operates on three synchronized pillars:
1.  **Sentiment Divergence:** Identifying mathematical discrepancies between retail panic/euphoria and institutional capital flow.
2.  **Volumetric Shielding:** Executing strictly when volume data confirms the presence of institutional tier liquidity.
3.  **Fundamental Arbitrage (Active Integration):** Currently integrating localized balance sheet efficiencies (Sales/Assets Ranking models) for statistical arbitrage deployment.

## **Risk Management & Telemetry**
Absolute capital preservation is the primary directive of this framework.
* **Dynamic Volatility Bleed Prevention:** Automated widening of execution timeframes during high-frequency market noise (Algorithmic Quantitative Easing).
* **Zero-Trust Failsafes:** Hard-coded server-side killswitches ("Flatten and Disconnect" protocols) to sever API connections during anomalous drawdown events or extreme latency spikes.
* **Max Drawdown Tolerance:** Strictly capped at **5.2%**.

## **Verification**
Core logic and Out-of-Sample stability parameters have been mathematically verified via the **WorldQuant BRAIN Institutional Network** (Achieved Bronze Tier status, 2026).

*Note: The full mathematical weights and proprietary generation logic are abstracted in this public repository to protect the Alpha. The core_execution.py file demonstrates the structural flow and risk parameters.*
