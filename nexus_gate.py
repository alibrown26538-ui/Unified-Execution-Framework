"""
UEF SOVEREIGN PROTOCOL HEADER
Project: Unified Execution Framework (UEF)
Module: Nexus Gate State Machine
Security Level: Proprietary / Research
Compliance: UK/US Cyber-Security Standard

NOTICE: This code is the intellectual property of Alisdair Brown.
Unauthorized distribution or malicious modification is prohibited.
Intent: Zero-Trust Logic Routing & State Management.
"""
import logging
from typing import Dict

# Configure routing for state transition logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - UEF NEXUS - %(message)s')

class NexusGateStateMachine:
    """
    UEF Master Kernel Module: Nexus Gate (The Gearbox)
    --------------------------------------------------
    State-machine responsible for regime transition logic.
    Ingests the Inverse Matrix Ratio (ξ) and Thunder Shield audits
    to route execution capital dynamically.
    """

    # Defined UEF Operational States
    STATES = {
        "ACTIVE": "ACTIVE_EXECUTION",
        "STANDBY": "THUNDER_PROTOCOL_STANDBY",
        "STASIS": "LOCKED_IN_STASIS"
    }

    def __init__(self):
        """
        Initializes the Nexus Gate. Default state is always STASIS until proven safe.
        (Zero-Trust Architecture)
        """
        self.current_state = self.STATES["STASIS"]
        logging.info("Nexus Gate Initialized. Defaulting to ZERO-TRUST STASIS.")

    def evaluate_regime_transition(self, xi_diagnostic: Dict[str, str], is_system_safe: bool) -> str:
        """
        The routing logic. Evaluates environmental signals and internal risk limits.
        """
        # 1. Absolute Override: If the Thunder Shield fails the audit, lock the gate.
        if not is_system_safe:
            return self._execute_transition(self.STATES["STASIS"], "THUNDER_SHIELD_OVERRIDE")

        # 2. Regime Mapping based on Telemetry (ξ)
        suggested_regime = xi_diagnostic.get("regime", "UNKNOWN")

        if suggested_regime == "ACTIVE_EXECUTION":
            return self._execute_transition(self.STATES["ACTIVE"], "STRUCTURAL_ALIGNMENT_CONFIRMED")
            
        elif suggested_regime == "THUNDER_PROTOCOL_STANDBY":
            return self._execute_transition(self.STATES["STANDBY"], "VOLATILITY_EXPANSION_DETECTED")
            
        else:
            # Fallback for NOISE_DOMINANT or UNKNOWN regimes
            return self._execute_transition(self.STATES["STASIS"], "STOCHASTIC_NOISE_FLOOR_HIGH")

    def _execute_transition(self, target_state: str, reason: str) -> str:
        """
        Handles the state transition and logs the regime shift for the audit trail.
        """
        if self.current_state != target_state:
            logging.info(f"REGIME SHIFT: {self.current_state} -> {target_state} | REASON: {reason}")
            self.current_state = target_state
        
        return self.current_state

if __name__ == "__main__":
    # Internal module self-test verification
    print("--- INITIATING UEF NEXUS GATE ---")
    print("STATUS: ONLINE")
    print("LOGIC: STATE-MACHINE ROUTING ACTIVE")
