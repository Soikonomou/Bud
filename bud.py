"""
The purpose of this project was to write a generator for data augmentation of transaction data.
The augmentation I used covered two features, namely: the ‘date’ and the ‘amount’.
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime
import time
pd.options.mode.chained_assignment = None  # ignore warnings about chained assignment
# import the data into a dataframe
df = pd.read_csv('Data_Science_Data.csv')


class Generator:
    # We create a function (like a flip of a biased or unbiased coin) to give us the probability that the next
    # draw from the dataset will give us Augmented (A) or Non-Augmented (NA) data.
    # For that reason we will use random.random() which returns a uniformly distributed
    # pseudo-random floating point number in the range [0, 1). This number would be less than
    # a given number p in the range [0,1) with probability p.
    def flip(p):
        return 'A' if random.random() < p else 'NA'

    # This is the function for the first augmentation a.
    def augment_a(data_a, i):
        # We alter slighly the 'amount' feature by adding or substracting 40% of the real value.
        data_a['amount'].iloc[i] = data_a['amount'].iloc[i] + \
            round(
                random.uniform(-0.4*data_a['amount'].iloc[i], 0.4*data_a['amount'].iloc[i]), 2)
        return(data_a)

    # This is the function for the second augmentation b.
    def augment_b(data_b, i):
        # We change the string 'date' of the original data to a datatime object and then a timestamp object.
        timestamp = time.mktime(datetime.strptime(
            data_b['date'].iloc[i], "%Y-%m-%d").timetuple())
        # We apply small transformation to the timestamp.
        timestamp = timestamp+random.randint(-1000000, 1000000)
        # We return the timestamp to the integer form.
        new_datetime = datetime.fromtimestamp(timestamp)
        new_date = new_datetime.strftime("%Y-%m-%d")
        # We replace the previous 'date' with the altered one.
        data_b['date'].iloc[i] = new_date
        # We include the augmented row to our dataframe.
        return(data_b)

    # The generator function takes as arguments the dataframe with the data,
    # the probability p of choosing if we will augment the original data or not with
    # each augmentation technique and the batch of data to return.

    def generator(data, p, batch_size):
        # We use 'try' and 'while' in order to overcome the 'StopIteration'
        # error the generator objects encounter after they finish iterating through the data.
        try:
            while True:
                data = data.sample(frac=1)  # shuffle the dataset between different batches
                # We use sample function from Pandas to randomly select rows from a pandas dataframe.
                data_sample = pd.DataFrame(data.sample(n=batch_size, replace=False))
                for i in range(len(data_sample)):
                    # We use the flip function to determine if we will use the first augmentation technique.
                    prob = Generator.flip(p)
                    if prob == 'A':
                        Generator.augment_a(data_sample, i)
                    # We use the flip function to determine if we will use the second augmentation technique.
                    prob = Generator.flip(p)
                    if prob == 'A':
                        Generator.augment_b(data_sample, i)
                yield(data_sample)
        except StopIteration:
            pass
