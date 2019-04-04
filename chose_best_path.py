import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')
episodes=1000
steps = [1,2,1,0,1,0,1,0,2,2,1,0,0,2,2,4]
fail = 0
success = 0

def next_step(position):
  action = steps[position]
  return action

for i_episode in range(episodes):
  state_now = env.reset()
  done = False
  fail+= 1
  for t in steps:    
    action = next_step(state_now)
    state_now, reward, done, info = env.step(action)
    if reward==1:
      success+= 1
      fail-= 1
      break
    if done:
      break

per_success=100 * float(success)/float(episodes)
per_fail=100 * float(fail)/float(episodes)
print('Total success: '+str(success)+', Total fail: '+str(fail))
print('Total success rate: '+str(per_success)+'%, Total fail rate: '+str(per_fail)+'%')
# data to plot
bars = ('Success', 'Fail')
y_pos = np.arange(len(bars))
height = [per_success, per_fail]

plt.bar(0, height[0], color=['red'])
plt.bar(1, height[1], color=['blue'])
plt.xticks(y_pos, bars)
plt.xlabel("Result")
plt.ylabel('Episodes')
plt.title('Result of the Experiment')
plt.legend(bars,bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()
