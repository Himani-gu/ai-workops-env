# inference.py
import os
from openai import OpenAI

# Environment variables with defaults
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def main():
    print(f"[START] task=example-task env=openenv model={MODEL_NAME}")
    rewards = []
    steps = 0
    success = False

    try:
        # Step 1
        action = run_inference("Suggest one action.")
        steps += 1
        reward = 0.00
        rewards.append(reward)
        print(f"[STEP] step={steps} action={action} reward={reward:.2f} done=true error=null")
        success = True
    except Exception as e:
        # Step error reporting
        print(f"[STEP] step={steps + 1} action=none reward=0.00 done=true error={str(e)}")
    finally:
        # END line always printed
        rewards_str = ",".join(f"{r:.2f}" for r in rewards)
        print(f"[END] success={'true' if success else 'false'} steps={steps} rewards={rewards_str}")

if __name__ == "__main__":
    main()
