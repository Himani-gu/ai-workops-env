import requests

# Replace with your Hugging Face Space URL
BASE = "https://himani2--ai-workops-env.hf.space"

# 1️⃣ Test root
try:
    r = requests.get(f"{BASE}/")
    print("Root:", r.json())
except Exception as e:
    print("Root endpoint error:", e)

# 2️⃣ Health check
try:
    r = requests.get(f"{BASE}/health")
    print("Health:", r.json())
except Exception as e:
    print("Health endpoint error:", e)

# 3️⃣ Reset environment
try:
    r = requests.post(f"{BASE}/reset", json={})
    print("Reset:", r.json())
except Exception as e:
    print("Reset endpoint error:", e)

# 4️⃣ Perform step action
try:
    r = requests.post(f"{BASE}/step", json={"action": 1})
    print("Step action 1:", r.json())

    r = requests.post(f"{BASE}/step", json={"action": 5})
    print("Step action 5:", r.json())
except Exception as e:
    print("Step endpoint error:", e)
