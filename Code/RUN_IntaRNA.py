#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:14:12 2020

@author: Narjes Rohani
"""
#install subprocess, Pandas, biopython, and IntaRNA packages
import os
import subprocess
import pandas as pd
#Load file of miRNAs sequences that you want to canculate MFE to bind SARS-CoV-2
mRNAMicroRNA=pd.read_csv('miRNAsListFile.csv')
#Load UCS file 
Xs=pd.read_csv('UCR.txt').seq
#Drop dublicate miRNA sequences
mRNAMicroRNA.drop_duplicates(subset='microRNA_name', keep='first', inplace=True)
Ylist=mRNAMicroRNA['microRNA_name']
scoresFinal=[]
names=[]
covSeq=[]
mirs=[]
for Y,name in zip(mRNAMicroRNA['miRNA_seq'],mRNAMicroRNA['microRNA_name']):
 for X in Xs:

    #Call IntaRNA for calculating MFE
    command="IntaRNA -t"+str(X)+' -q '+str(Y)
    output = subprocess.check_output(command, shell=True)
    print(output)
    scoresFinal.append(output)
    names.append(name)
    covSeq.append(X)
    mirs.append(Y)
Data=pd.DataFrame(columns=['Name','energy','UCR','mirRNAseq'])
Data['Name']=names
Data['UCR']=covSeq
Data['mirRNAseq']=mirs
Data['energy']=scoresFinal
Data.to_csv('CalculatedEnergy.csv',index=False)
print(Data.head())