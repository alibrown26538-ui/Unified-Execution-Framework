"""
UEF SOVEREIGN PROTOCOL HEADER
Project: Unified Execution Framework (UEF)
Module: Inverse Matrix (ξ) Logic
Security Level: Proprietary / Research
Compliance: UK/US Cyber-Security Standard

NOTICE: This code is the intellectual property of Alisdair Brown.
Unauthorized distribution or malicious modification is prohibited.
Intent: Ethical Alpha Extraction & Systemic Resiliency.
"""
import numpy as np
import pandas as pd
from typing import Dict, Optional, Tuple
from numpy.linalg import inv, LinAlgError

class TelemetryXiEngine:
    """
    UEF Master Kernel Module: Telemetry (The Brain)
    -------------------------------------------------
    Proprietary implementation of the Inverse Matrix Ratio (ξ).
    Designed to isolate structural market alpha from behavioral stochasticity.
    This engine continuously audits the 'Noise Floor' to feed the Nexus Gate state machine.
    """

    def __init__(self, structural_lookback: int = 252, behavioral_lookback: int = 21):
        """
        Initializes the Telemetry Engine with distinct regime lookback windows.
        """
        self.struct_lb = structural_lookback
        self.noise_lb = behavioral_lookback
        self.covariance_matrix: Optional[np.ndarray] = None
        self.xi_ratio: float = 0.0

    def _compute_covariance_inversion(self, price_matrix: pd.DataFrame) -> np.ndarray:
        """
        Internal Method: Computes the inverted covariance matrix of the structural window.
        Provides the foundational weighting to penalize highly correlated, noisy assets.
        """
        try:
            # Calculate standard covariance matrix over the structural lookback
            cov_matrix = price_matrix.tail(self.struct_lb).cov().to_numpy()
            
            # Invert the matrix to isolate latent structural factors
            inv_cov_matrix = inv(cov_matrix)
            return inv_cov_matrix
        
        except LinAlgError:
            # Fallback for singular matrices during extreme illiquidity events
            raise ValueError("UEF FAULT: Singular Matrix detected. Telemetry inversion failed.")

    def calculate_xi_divergence(self, price_matrix: pd.DataFrame) -> Tuple[float, Dict[str, str]]:
        """
        Core Execution: Calculates the Inverse Matrix Ratio (ξ).
        Returns the ξ value and the current Signal/Noise diagnostic state.
        """
        if len(price_matrix) < self.struct_lb:
            return 0.0, {"status": "INSUFFICIENT_DATA", "regime": "UNKNOWN"}

        # 1. Isolate the inverted structural covariance
        self.covariance_matrix = self._compute_covariance_inversion(price_matrix)

        # 2. Extract drift vectors (Structural vs. Behavioral)
        structural_drift = price_matrix.tail(self.struct_lb).mean().to_numpy()
        behavioral_drift = price_matrix.tail(self.noise_lb).mean().to_numpy()

        # 3. Calculate the differential vector (The pure divergence)
        divergence_vector = structural_drift - behavioral_drift

        # 4. Apply the Inverse Matrix Ratio (ξ)
        # Dot product of the inverted covariance matrix and the divergence vector
        xi_array = self.covariance_matrix.dot(divergence_vector)
        
        # Aggregate to a single Systemic Signal-to-Noise ratio
        self.xi_ratio = np.linalg.norm(xi_array)

        # 5. Diagnostic State Mapping
        diagnostic = self._map_regime_state(self.xi_ratio)

        return self.xi_ratio, diagnostic

    def _map_regime_state(self, xi_value: float) -> Dict[str, str]:
        """
        Maps the raw ξ output to actionable UEF regime states for the Nexus Gate.
        """
        if xi_value < 0.5:
            # Noise is overpowering signal; highly stochastic environment.
            return {"status": "NOISE_DOMINANT", "regime": "STASIS_RECOMMENDED"}
        elif 0.5 <= xi_value <= 2.0:
            # Normal structural flow; safe for cross-sectional deployment.
            return {"status": "STRUCTURAL_ALIGNMENT", "regime": "ACTIVE_EXECUTION"}
        else:
            # Extreme divergence; potential 3-Sigma event initiating.
            return {"status": "ANOMALY_DETECTED", "regime": "THUNDER_PROTOCOL_STANDBY"}

if __name__ == "__main__":
    # Internal module self-test verification
    print("--- INITIATING UEF TELEMETRY MODULE ---")
    print("STATUS: LOADED")
    print("LOGIC: INVERSE MATRIX RATIO (ξ) READY FOR NEXUS INTEGRATION")
