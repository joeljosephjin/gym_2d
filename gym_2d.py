import numpy as np
import matplotlib.pyplot as plt

class gym_2d():
    def __init__(self, mean=0, dev=0.2):
        self.tau = 1
        self.goal = (np.random.sample(2) - 0.5)*dev + mean
        self.traj = []
        self.done = False
    
    def reset(self):
        self.pos = np.random.sample(2) - 0.5   # start position from [-0.5, 0.5]
        return self.pos
    
    def sample_action(self):
        return np.random.sample(2)*0.2 - 0.1
    
    def step(self, act):
        self.traj.append(self.pos)
        self.pos = self.pos + act*self.tau
        self.dist = np.sum((self.pos-self.goal)**2)
        rew = -1*self.dist
        if self.dist < 0.01:
            self.done = True
        return self.pos, rew, self.done
    
    def render(self):
        plt.plot([arr[0] for arr in self.traj], [arr[1] for arr in self.traj])