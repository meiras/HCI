#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:34:49 2018

@author: meira
"""


import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import networkx as nx

import pylab as PL

# import random as RD

from random import random


####FOR MONTE CARLO
import numpy
import matplotlib.pyplot as plt
import pandas




def initialize():
    global g, nextg, time
    time = 0 
    g = nx.Graph()
    g.pos = nx.spring_layout(g)
    
   
   # g.add_nodes_from([1,2,3], bipartite=0) #perceivers, top nodes
    # Add the node attribute "bipartite" - Targets = 1
   # g.add_nodes_from(['a','b','c'], bipartite=1)
    g.add_nodes_from([1,2,3,4,5,6, 7,'a','b','c', 'd', 'e', 'f', 'g'])
    g.add_edges_from([(1,'a'), (2,'b'), (3,'c'),(4,'d'),(5,'e'),(6,'f'),(7,'g')])

    g.node['a']['A.type'] = 'computer'
    g.node['b']['A.type'] = 'computer'
    g.node['c']['A.type'] = 'computer'
    g.node['d']['A.type'] = 'computer'
    g.node['e']['A.type'] = 'computer'
    g.node['f']['A.type'] = 'computer'
    g.node['g']['A.type'] = 'computer'
    
    g.node[1]['A.type'] = 'person'
    g.node[2]['A.type'] = 'person'
    g.node[3]['A.type'] = 'person'
    g.node[4]['A.type'] = 'person'
    g.node[5]['A.type'] = 'person'
    g.node[6]['A.type'] = 'person'
    g.node[7]['A.type'] = 'person'
    
    
    g.node[1]['expectation.1'] = 1
    g.node[2]['expectation.1'] = 1 
    g.node[3]['expectation.1'] = 1
    g.node[4]['expectation.1'] = 1
    g.node[5]['expectation.1'] = 1
    g.node[6]['expectation.1'] = 1
    g.node[7]['expectation.1'] = 1


    g.node['a']['performance.1'] = 0.1
    g.node['b']['performance.1'] = 0.1
    g.node['c']['performance.1'] = 0.1
    g.node['d']['performance.1'] = 0.1
    g.node['e']['performance.1'] = 0.1
    g.node['f']['performance.1'] = 0.1
    g.node['g']['performance.1'] = 0.1
    

    # #give them both performance and expectation, otherwise deadling with empty keys in dictionary.

    g.node[1]['performance.1'] = 2
    g.node[2]['performance.1'] = 2 
    g.node[3]['performance.1'] = 2
    g.node[4]['performance.1'] = 2
    g.node[5]['performance.1'] = 2 
    g.node[6]['performance.1'] = 2
    g.node[7]['performance.1'] = 2


    g.node['a']['expectation.1'] = 2
    g.node['b']['expectation.1'] = 2
    g.node['c']['expectation.1'] = 2
    g.node['d']['expectation.1'] = 2
    g.node['e']['expectation.1'] = 2
    g.node['f']['expectation.1'] = 2
    g.node['g']['expectation.1'] = 2
    
    g.pos = nx.spring_layout(g)

#    B.pos = nx.spring_layout(B)
#    for i in B.nodes():
        # set performance randomly to .7 or .3. there is nothing meaningful to this implementation
#        B.node[i]['performance.1'] = .7 if random() < .5 else .3
    
#    for i in g.nodes():
#            g.node[i]['performance.1'] = 0.1 if random() < .5 else 0.3
   
    nextg = g.copy()
    nextg.pos = g.pos.copy()
        
    
    

def observe():
    global g, nextg, time
    cla()
    # print( "=" * 30)
    # pprint( g.__dict__ )
    labels = nx.get_node_attributes(g, 'A.type')
 #   labels=dict((n,d['A.type']) for n,d in g.nodes(data=True))
 #   nx.draw(g, vmin = 0, vmax = 1, labels = labels, 
 #           node_color = [g.node[i]['expectation.1'] for i in g.nodes()],
 #           cmap=plt.cm.Reds, pos = g.pos)
 #   nx.draw(g, vmin = 0, vmax = 1, labels = labels, nodelist=[1,2,3],
 #           node_color = [g.node[i]['expectation.1'] for i in g.nodes()],
 ##           cmap=plt.cm.Reds, pos = g.pos)
 #   nx.draw(g, vmin = 0, vmax = 1, labels = labels, nodelist=['a','b','c'],
 #           node_color = [g.node[i]['expectation.1'] for i in g.nodes()],
 #           cmap=plt.cm.Blues, pos = g.pos)
 
    nx.draw(g, vmin = 0, vmax = 1, labels = labels, cmap=plt.cm.Reds,
            node_color = [g.node[i]['expectation.1'] for i in g.nodes() if [g.node[i]['expectation.1'] <2]], 
            #node_size = [int(g.node[j]['performance.1']*1000) for j in g.nodes() if [g.node[j]['performance.1'] <1.9]],
            pos = g.pos)

 
#    nx.draw(g, vmin = 0, vmax = 1, labels = labels, cmap=plt.cm.Reds,
#            node_color = [g.node[i]['expectation.1'] for i in g.nodes() if [g.node[i]['expectation.1'] <2]], 
#            pos = g.pos)


#Dt = 0.01 # Delta t

def update():
    global g, nextg, time
    time += 1
    
    #this code assumes constant performance and also assumes constant interaction
 
    if time == 0:
        g.node[1]['expectation.1'] = 1
        g.node[2]['expectation.1'] = 1
        g.node[3]['expectation.1'] = 1
        g.node[4]['expectation.1'] = 1
        g.node[5]['expectation.1'] = 1
        g.node[6]['expectation.1'] = 1
        g.node[7]['expectation.1'] = 1
    if time == 1:
        g.node[1]['expectation.1'] = 0.9
        g.node[2]['expectation.1'] = 0.9
        g.node[3]['expectation.1'] = 0.7
        g.node[4]['expectation.1'] = 0.1
        g.node[5]['expectation.1'] = 0.9
        g.node[6]['expectation.1'] = 0.7
        g.node[7]['expectation.1'] = 0.7
    elif time == 2:
        g.node[1]['expectation.1'] = 0.9
        g.node[2]['expectation.1'] = 0.7
        g.node[3]['expectation.1'] = 0.4
        g.node[4]['expectation.1'] = 0.3
        g.node[5]['expectation.1'] = 0.7
        g.node[6]['expectation.1'] = 0.5
        g.node[7]['expectation.1'] = 0.4

    elif time == 3:
        g.node[1]['expectation.1'] = 0.9
        g.node[2]['expectation.1'] = 0.9
        g.node[3]['expectation.1'] = 0.4
        g.node[4]['expectation.1'] = 0.9
        g.node[5]['expectation.1'] = 1
        g.node[6]['expectation.1'] = 0.3
        g.node[7]['expectation.1'] = 0.9
  
    elif time == 4:
        g.node[1]['expectation.1'] = 0.9
        g.node[2]['expectation.1'] = 0.5
        g.node[3]['expectation.1'] = 1.0
        g.node[4]['expectation.1'] = 0.4
        g.node[5]['expectation.1'] = 0.2
        g.node[6]['expectation.1'] = 0.1
        g.node[7]['expectation.1'] = 0.2
 
    elif time == 5:
        g.node[1]['expectation.1'] = 0.9
        g.node[2]['expectation.1'] = 0.4
        g.node[3]['expectation.1'] = 1
        g.node[4]['expectation.1'] = 0.2
        g.node[5]['expectation.1'] = 0.5
        g.node[6]['expectation.1'] = 0.7
        g.node[7]['expectation.1'] = 0.5
        
    else:
        g.node[1]['expectation.1'] = 0.9
        g.node[2]['expectation.1'] = 0.9
        g.node[3]['expectation.1'] = 0.7
        g.node[4]['expectation.1'] = 0.4
        g.node[5]['expectation.1'] = 0.9
        g.node[6]['expectation.1'] = 0.7
        g.node[7]['expectation.1'] = 0.7



   
#    if time > 100:
#        g.node['a']['performance.1'] = 1 if random() < .5 else .3
#        g.node['b']['performance.1'] = 1 if random() < .5 else .1
#        g.node['c']['performance.1'] = 1 if random() < .5 else .5
#        for i in g.nodes(): 
#            for j in g.neighbors(i):
#                if (g.node[i]['performance.1'] >= 0) and (g.node[i]['performance.1'] <= 1):
#                #if the target's performance is what perceiver expected, keep expectation what it was
#                    if g.node[i]['performance.1'] == g.node[j]['expectation.1'] :
#                        nextg.node[j]['expectation.1'] = g.node[j]['expectation.1'] # nextB.node[i]['state'] = 100 #FIXME placeholder value
#                    if ((g.node[i]['performance.1'])-(g.node[j]['expectation.1'])) > 0 : #if the difference is that performance is greater, keep expectation to simplify
#                        nextg.node[j]['expectation.1'] = g.node[j]['expectation.1']+0.02
#                    if ((g.node[i]['performance.1'])-(g.node[j]['expectation.1'])) < 0 : #if the difference is that expecttion is greater, bring expectation down
#                        nextg.node[j]['expectation.1'] = g.node[j]['expectation.1']-0.02 #take the expectation down by bringing it closer to performance --arbitrary method
#                #if RD.random() < PoorVAProb:
#                  #  nextB.node[i]['expectation.1'] = .5 #reset some 
#                           # break
#                else: # adaptive link cutting behavior
#                    nextg.node[i]['performance.1'] = 1 
#    else:
#        for i in g.nodes(): 
#            for j in g.neighbors(i):
#                if (g.node[i]['performance.1'] >= 0) and (g.node[i]['performance.1'] <= 1):
#                #if the target's performance is what perceiver expected, keep expectation what it was
#                    if g.node[i]['performance.1'] == g.node[j]['expectation.1'] :
#                        nextg.node[j]['expectation.1'] = g.node[j]['expectation.1'] # nextB.node[i]['state'] = 100 #FIXME placeholder value
#                    if ((g.node[i]['performance.1'])-(g.node[j]['expectation.1'])) > 0 : #if the difference is that performance is greater, keep expectation to simplify
#                        nextg.node[j]['expectation.1'] = g.node[j]['expectation.1']+0.02
#                    if ((g.node[i]['performance.1'])-(g.node[j]['expectation.1'])) < 0 : #if the difference is that expecttion is greater, bring expectation down
#                        nextg.node[j]['expectation.1'] = g.node[j]['expectation.1']-0.02 #take the expectation down by bringing it closer to performance --arbitrary method
#                #if RD.random() < PoorVAProb:
#                  #  nextB.node[i]['expectation.1'] = .5 #reset some 
#                           # break
#                else: # adaptive link cutting behavior
#                    nextg.node[i]['performance.1'] = 0
#                #nextg.node[i]['performance.1'] = 0
#                #nextg.node[j]['expectation.1'] = 0
#                #nextg.node[j]['expectation.1'] =  ((g.node[1]['expectation.1'])+(g.node[2]['expectation.1'])+(g.node[3]['expectation.1']))/3
#                #nextg.node[j]['expectation.1'] = ((g.node[1]['expectation.1'])+(g.node[2]['expectation.1'])+(g.node[3]['expectation.1']))/3
#      
    g, nextg = nextg, g
#    
# #   del g
# #   g = nextg.copy()
# #   g.pos = nextg.pos.copy()

import pycxsimulator
pycxsimulator.GUI().start(func=[initialize, observe, update])

#plt.plot([0.2,0.4,0.6,0.8,1.0])
#plt.ylabel('expectation')
#plot.show()
