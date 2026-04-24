import threading
import time
import random

# --- UEF MODULE 2: 2v8 ADVERSARIAL SYNC ---
# Logic: Maintaining System Consensus under High-Entropy Disruption
# Agents (8): Truth-Seeking Subroutines
# Adversaries (2): Data Corruptors (Market Volatility / Institutional Noise)

class SurvivorAgent(threading.Thread):
    def __init__(self, agent_id):
        super().__init__()
        self.agent_id = agent_id
        self.progress = 0
        self.is_disrupted = False

    def run(self):
        while self.progress < 100:
            if not self.is_disrupted:
                # Simulate "Fixing the Generator" (Data Processing)
                time.sleep(random.uniform(0.1, 0.4))
                self.progress += random.randint(2, 6)
                if self.progress > 100: self.progress = 100
            else:
                # Node is under attack (Latency/Noise)
                time.sleep(0.5)
                self.is_disrupted = False # Recovering...

class AdversaryKiller(threading.Thread):
    def __init__(self, target_group):
        super().__init__()
        self.target_group = target_group

def run(self):
        while any(a.progress < 100 for a in self.target_group):
            time.sleep(1.5)
            # Safe Strike: Only attack if there are agents left to disrupt
            valid_targets = [a for a in self.target_group if a.progress < 100]
            if valid_targets:
                target = random.choice(valid_targets)
                print(f"[!] ADVERSARY STRIKE: Logic Regression on Agent {target.agent_id}")
                target.progress -= 5
                target.is_disrupted = True

if __name__ == "__main__":
    print("[*] INITIALIZING UEF 2v8 CONCURRENCY ENGINE...")
    
    # Spawn 8 Agents
    agents = [SurvivorAgent(i) for i in range(8)]
    for a in agents: a.start()
    
    # Spawn 2 Adversaries (The 'Messy' Market Variables)
    killers = [AdversaryKiller(agents) for _ in range(2)]
    for k in killers: k.start()

    # Wait for completion
    for a in agents: a.join()
    
    print("\n[SUCCESS] UEF CONSENSUS REACHED: SYSTEM STABILIZED AT 100%")