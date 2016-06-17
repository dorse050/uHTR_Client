#!/usr/bin/python

from   histo_reader import *
from   histo_generator import * 
import argparse
import os
import time

uHTRtool_source_test()

def getHistoResults(crate=41, slot=5, norbits=1000, sepCapID=0, signalOn=0, outDir="joshtest"):

	testResults = {}	
	pathToRoot = generate_histos(crate, slot, n_orbits=norbits, sepCapID=capID, file_out_base="", new_dir=outDir)

	for file in os.listdir(pathToRoot): 

		# Extract slot number from file name
   		temp = file.split('_')
		temp = temp[-1].split('.root')
                slotNum = str(temp[0])

		testResults["slot_%s"%(slotNum)] = getHistoInfo(signal=signalOn, file_in=pathToRoot+"/"+file)
	
	os.removedirs(pathToRoot)
        
        return testResults

def QIE_mapping(slots, master_dict={}, ts):
	return None

def get_sig_histo(results)
        for slot, chip in results.iteritems():
                for chip, histo in slot.iteritems():


