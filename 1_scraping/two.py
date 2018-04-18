#!/usr/bin/python

import pickle

fp = open("files/shared.pkl")
shared = pickle.load(fp)
print shared["index"]
