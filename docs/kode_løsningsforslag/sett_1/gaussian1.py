import numpy as np

# varibles:
m = 0
s = 2
x = 1

# parenthesis hell, calculating the gaussian value.
f = (1.0/(np.sqrt(2*np.pi)*s))*np.exp((-1.0/2)*(((x)-(m))/s)**2)
print("Gaussian value = %g" % f)

# running example:
"""$ python3 gaussian1.py
Gaussian value = 0.176033"""
# calculator gives the same result (as does WolframAlpha).
