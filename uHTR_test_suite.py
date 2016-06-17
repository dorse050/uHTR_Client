from uHTR_test_functions import *

master_dict={}

def getQIE(Jslot, register, master_dict=master_dict):
	key="({0},{1})".format(Jslot, register)
	return master_dict[key]


