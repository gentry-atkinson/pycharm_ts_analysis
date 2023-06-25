import os
import numpy as np
import pandas as pd

DATA_PATH = 'data/'

if __name__ == '__main__':
   train_file = pd.read_csv(os.path.join(DATA_PATH, 'DailyDelhiClimateTest.csv'))
   print(train_file['meantemp'])
