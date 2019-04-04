import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')
episodes=1000
fail = 0
success = 0
steps_taken = [1,1,2,2,1,2]
for i_episode in range(episodes):
  state_now = env.reset()
  fail+= 1
  #ia=0
  for t in steps_taken:
    state_now, reward, done, info = env.step(t)
    if reward==1:
      success+= 1
      fail-= 1
      break
    #if(ia>=5):
      #ia=0
    #else:  
      #ia+=1

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
