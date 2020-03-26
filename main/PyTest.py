import datetime as dt
import os
curr_time = dt.datetime.now().strftime("%a %b %d %Y %H %M")
path = 'D:\\doc\\Amazon Work\\Jenkins\\Testing\\' + curr_time
os.mkdir(path)
