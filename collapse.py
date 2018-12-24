# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:55:49 2018

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework to describe and simulate object collapse

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Collapse [Computer software]. Github repository <https://github.com/alanjpan/Collapse>

Note this software's license is GNU GPLv3.
"""

import random

platformA = [100, 100]
sump = 0
for i in platformA:
    sump += i
print('total magnitude before collapse:  ' + str(sump))

def collapse(platform, rate):
    collapsed = []
    segment = rate
    magnitude = 0
    for i in platform:
        segment = random.randrange(rate, rate+6)
        print('magnitude: ' + str(i))
        print('segments: ' + str(segment))
        magnitude = i
        pieces = int(magnitude / segment)
        for j in range(segment):
            collapsed.append(pieces)
    return collapsed

print(platformA)
print('rate of collapse:  random 5 to +6')
print(collapse(platformA, 5))

sump = 0
for i in platformA:
    sump += i
print('total magnitude after collapse:  ' + str(sump)) 
print('(uneven after-collapse suggests rounding error)')
