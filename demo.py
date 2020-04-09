"""
This script is a demostration of the generator I built.
"""
from bud import *
print('Initialize the generator...')
gen = generator(df, 1, 5)  # Here p=1 so only augmented data
print('generator initialized')
print('Here is a batch of 5 data points, all augmented:')
augmented_data = next(gen)
print(augmented_data)
print('you can use next(gen) to obtain another batch')
