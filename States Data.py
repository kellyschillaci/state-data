# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:14:26 2019

@author: kdoyl
"""

import csv

infile = 'states_data.tsv'


statesList = []

with open(infile, 'rU') as csvfile:

    stateReader = csv.reader(csvfile,  dialect='excel', delimiter='\t')

    for line in stateReader:

      if line[0] == '' or line[0].startswith('Data') or line[0].startswith('*'):

          continue

      else:

          state = {}

          state['name'] = line[0]

          state['abbrev'] = line[1]

          state['code'] = line[2]

          state['area'] = int(line[3].replace(',',''))

          state['pop'] = int(line[4].replace(',',''))

  
          statesList.append(state)

    
csvfile.close()

print ("Read", len(statesList), "state data")

for state in statesList:

    print ('State:', state['name'], ' Abrv: ', state['abbrev'], ' Population: ', state['pop'])

