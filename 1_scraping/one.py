#!/usr/bin/python

import pickle

shared = {"index":0}
fp = open("files/shared.pkl","w")
pickle.dump(shared, fp)
