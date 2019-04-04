# Frozen Lake Problem
The Frozen Lake environment is a 4×4 grid which contain four possible areas; Safe (S), Frozen (F), Hole (H) and Goal (G).

The agent in the environment has four possible moves Up, Down, Left and Right. Q-Learning which is a re-informant learning technique, will be used here. This environment will allow the agent to move accordingly. Random movement can occur at anything in any action like the agent is slipping in different directions because it is hard to walk on a frozen surface.

## Manual Inspection
The libraries are imported which will be used. Three libraries are used for this one gym, numpy and matplotlib.pyplot

The function percentage is used to calculate the number of success and fail rate.

Next, to create our environment, I just call gym.make() and pass a string of the name of the environment I want to set up. The environment FrozenLake-v0 used and stored in the variable evn. The number of episodes is initiated as 1000 and success and fail initiated to 0.

Fixed actions are defined for the agent, from the initial step the agent will go Down, Down, Right, Right, Down, Right to reach the frisbee.

A for loop is done for the 1000 episodes for the agent

The environment is reset at the beginning
Fail variable is increment to 1
Another loop is started which runs 6 times, this is the number of steps an agent needs to take to reach the frisbee within a single episode

a. The step is run for the agent and checked if the agent gets the frisbee

b. If the agent gets the frisbee then reward is set to 1

Success variable is increment to 1

Fail variable is decrement to 1

The success and fail are printed and also the percentage of success and fail is printed in the next line

A bar graph is used to represent the success and fail of the agent of getting the frisbee in this total run of episodes.

If the agent takes a fixed path and goes Down, Down, Right, Right, Down, Right always then it has a success rate of 0.7% to get the frisbee.

![Image 1](https://github.com/xerun/python_frozenlake_v0/blob/master/manual.png)

## Chose best path

An array is defined for the direction of the step for the agent for each state.

The function next_step is used to return the next action to take for the current state by calling the action from the step array by passing the position as array index. If the position is 15 that means the agent reached the goal

For loop is run for the number of episodes

The environment is reset to the starting point at the beginning
The done variable is declared to false to check if the episode is finished
Inner loop runs for the number of counts of the step array.

a. The next_step function is called and the returned value is stored in the action variable

b. After the action is chosen it is pass in the step function which returns the new_state, reward for the action we took, if the action we took ended our episode, and some information of the environment.

c. The state value is updated to the state_now value

d. If the reward is 1 then the success value is incremented

e. If done is True then we exit the loop and go to the next episode

#### Conclusion
If we compare the graph of Section 2 and 3, we can see that the success rate in section 3 improves a lot because the agent knows where to go from the state, he is in.

The function is not injective because different position might have same action so it is many to one and it is not surjective because every position does not match with every action.

![Image 2](https://github.com/xerun/python_frozenlake_v0/blob/master/best_path.png)

## Best path from any location

The next_step() and next_set_of_steps() functions are used in section 5 which are defined in section 3 and 4 to find the performance for a range of alpha between 0 and 1.

The probability() function which takes the position of the agent in the lake and the array of range between 0 and 1 for alpha, is used to determine the performance against alpha.

The numpy.random.choice inside the probability function takes a range between 0 and 1, and a probability of alpha and 1-alpha. For each alpha in the range it will take a probability of alpha and 1-alpha, i.e. for 0.2 it will have a probability of 0.2 and 0.8, and for 1 it will have 1 and 0.

If the numpy.random.choice returns value 0 then "next_step()" function will be called which will run each step one by one until it reaches the frisbee or falls in hole.

If it returns 1 then "next_set_of_steps()" function is called which will return the list of steps needed to reach the frisbee from the current position.

The probability function will count the number of success for each 1000 episodes for each alpha between 0 and 1 and which increases by 0.1. Success count of each alpha is stored in the dictionary and returned at the end.

A line graph is created using the data with performance which is the number of success in y-axis and 0.0 to 1.0 for x-axis which is the alpha to present the performance of the probability function.

The performance increases as the alpha value increases, it reaches the maximum number of success (performance) which is 40 for the alpha value 0.8 it again decreases to 27 for alpha 0.9 and finally reaches to 35 at 1.0 alpha. The lowest success is at alpha 0.0 of 3 success.

![Image 3](https://github.com/xerun/python_frozenlake_v0/blob/master/best_location_path.png)
