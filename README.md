# gym_2d
Simple 2D Navigation task environment for meta reinforcement learning research.
Implemented from the paper: [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks
](https://arxiv.org/abs/1703.03400)

## Test

Use this code to test the environment.

```
import gym_2d

env = gym_2d.gym_2d()
observation = env.reset()
print('START:- goal:', env.goal)

for i in range(1000):
    env.render()
    action = env.sample_action()
    observation, reward, done = env.step(action)

    if done:
        print('DONE:- reached:', observation,',within dist:', env.dist, ',in steps:', i)
        break
        observation = env.reset()
        
print('END:- reached:', observation,',within dist:', env.dist, ',in steps:', i)
```

## Render Output

![Render Output](https://github.com/joeljosephjin/gym_2d/blob/master/render.png)
