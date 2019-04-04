import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make('FrozenLake-v0')
episodes=1000
steps = [1,2,1,0,1,-1,1,-1,2,2,1,-1,-1,2,2,4]
fail = 0
success = 0

def next_step(position):
  action = steps[position]
  return action

def next_set_of_steps(position):
  next_steps = []
  action = steps[position]
  next_steps.append(action)
  for i in range(16):
    if position == 14:
      break
    elif action == 0:
      position = position-1
      action = steps[position]
      next_steps.append(action)
    elif action == 1:
      position = position+4
      action = steps[position]
      next_steps.append(action)
    elif action == 2:
      position = position+1
      action = steps[position]
      next_steps.append(action)
    elif action == 3:
      position = position-4
      action = steps[position]
      next_steps.append(action)
  return next_steps

def probability(position,alpha): 
  mydict = dict()  
  for _alpha_ in alpha:
    success=0
    for i_episode in range(episodes):      
      done = False
      state_now = env.reset()
      decision = np.random.choice(np.arange(0,2), p=[_alpha_, 1 - _alpha_])
      if decision == 0:
        for t in steps:
          action = next_step(state_now)
          #print (action)          
          state_now, reward, done, info = env.step(action)
          
          if reward==1:
            success+= 1
            break
          if done:
            break
      else:
        steps_list = next_set_of_steps(state_now)
        #print (steps_list)
        for s in steps_list:
          state_now, reward, done, info = env.step(s)
          if reward==1:
            success+= 1
            #print (reward)
            break
          if done:
            break
    mydict[round(_alpha_,1)]=success
  return mydict

state_now = env.reset()
alpha = np.arange(0, 1.1, 0.1)
piecewise = probability(state_now,alpha)

for key, value in piecewise.items():
  print (key,value)
    
t = []
s = []
for key, value in piecewise.items():
  t.append(key)
  s.append(value)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Alpha', ylabel='Performance (no. of Success))',
       title='Performance of k for alpha')
ax.grid()

plt.show()
