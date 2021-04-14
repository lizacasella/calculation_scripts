#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:43:51 2021

@author: caselll1
"""

# inhibitor molar mass in g/mol
bosutinib = 530.45 
erlotinib = 429.90
gefitinib = 446.9
axitinib = 386.469
bosutinib_isomer = 530.46
neratinib = 557
ponatinib = 532.56
vandetanib = 475.354

drugs = ["bosutinib", "erlotinib", "gefitinib","axitinib","bosutinib_isomer","neratinib","ponatinib","vandetanib"]

DMSO = 1.1 # g/mL

# input the name of the kinase inhibitor

print("What is the name of the ligand? Choose from:")
print(*drugs, sep="\n")


inhibitor = input("Name: ")
mol = float(input("What is the molarity of your solution in mM? "))

# set molar mass of inhibitor 
if inhibitor == "bosutinib":
    inhibitor = 530.45
if inhibitor == "gefitinib":
    inhibitor = 446.9
if inhibitor == "axitinib":
    inhibitor = 386.469
if inhibitor == "bosutinib_isomer":
    inhibitor = 530.46
if inhibitor == "neratinib":
    inhibitor = 532.56
if inhibitor == "vandetanib":
    inhibitor = 475.354
elif inhibitor == "erlotinib":
    inhibitor = 429.90
    
# calculate concentration in g/mg in DMSO

conc = (mol * 10E-4 * inhibitor) / DMSO

# mass = (inhibitor * 10E-3) / DMSO

print("Your concentration is %.4f mg/g" %(conc))