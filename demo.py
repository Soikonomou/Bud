"""
This script is a demonstration of the generator I built.
It generates 5 augmented data from the dataset using
both augmentation techniques.
"""
from bud import *
print('Initialize the generator...')
gen = Generator.generator(df, 1, 5)  # Here p=1 so only augmented data
print('generator initialized')
print('Here is a batch of 5 augmented data points:')
augmented_data = next(gen)
print(augmented_data)
print('You can use next(gen) to obtain another batch!')
