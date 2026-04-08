from env.environment import AIWorkOpsEnv, Action

env = AIWorkOpsEnv()
obs = env.reset()

done = False

while not done:
    action = Action(action="correct")
    obs, reward, done, _ = env.step(action)

print("Final Reward:", reward)
