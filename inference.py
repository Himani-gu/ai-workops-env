import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def run_inference(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

def main():
    task_name = "example-task"
    benchmark = "openenv"
    rewards = []
    steps = 0
    success = False

    print(f"[START] task={task_name} env={benchmark} model={MODEL_NAME}")

    try:
        action = run_inference("Suggest a single action.")
        steps += 1
        reward = 0.00
        rewards.append(reward)
        print(f"[STEP] step={steps} action={action} reward={reward:.2f} done=true error=null")
        success = True
    except Exception as e:
        print(f"[STEP] step={steps + 1} action=none reward=0.00 done=true error={str(e)}")
    finally:
        rewards_str = ",".join(f"{r:.2f}" for r in rewards)
        print(f"[END] success={'true' if success else 'false'} steps={steps} rewards={rewards_str}")

if __name__ == "__main__":
    main()
