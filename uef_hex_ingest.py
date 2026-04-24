import binascii

# --- UEF MODULE 3: HEXADECIMAL INGEST ---
# Logic: Translating Raw Telemetry into Logical Vectors
# Purpose: Bridging the gap between 'The Mist' (Raw Data) and 'The Truth' (The Kernel)

class HexIngest:
    def __init__(self):
        self.registry = []

    def process_telemetry(self, raw_hex):
        """Converts raw hex strings into normalized float values."""
        try:
            # Remove '0x' prefix if present
            clean_hex = raw_hex.replace('0x', '')
            
            # Convert hex to integer
            value = int(clean_hex, 16)
            
            # Normalize to a 0.0 - 1.0 range (Simple scaling for simulation)
            normalized = (value % 1000) / 1000.0
            return normalized
        except ValueError:
            print(f"[!] CORRUPT DATA DETECTED: {raw_hex}")
            return None

if __name__ == "__main__":
    ingest = HexIngest()
    
    # Simulated Raw Hex Stream (The kind we see in your telemetry screenshots)
    raw_stream = ["0x1A4F", "0x2B9D", "0xFF3A", "INVALID_DATA", "0x4C12"]
    
    print("[*] UEF INITIATING HEXADECIMAL INGEST...")
    
    for packet in raw_stream:
        signal = ingest.process_telemetry(packet)
        if signal is not None:
            print(f"[>] Packet: {packet} | Signal: {signal:.4f}")