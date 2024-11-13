import numpy as np
import time

mu, sigma = 7, 2 # mean and standard deviation (minutes)
s = np.random.normal(mu, sigma, 1)
delay = s[0]
time.sleep(delay * 60)

