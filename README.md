

# DisCoVering potential candidates of RNAi-based therapy for SARS-CoV-2 using computational methods

Herein, we conducted four independent analyses on RNA interference (RNAi)-based therapy with computational and bioinformatic methods in order to target the evolutionarily conserved regions in SARS-CoV-2 genome, resulting in down-regulation or silencing its RNA. miRNAs are denoted to play a role in the resistance of some species to viral infections. A comprehensive analysis on the miRNAs available in the body of human, as wells as the miRNAs in bats and other species, were done to find efficient candidates with low side-effects in the human body. Moreover, the evolutionarily conserved regions in SARS-CoV-2 genome were considered for designing novel significant siRNA with high specificity. Multiple miRNAs and two siRNA were suggested as the possible efficient candidates with a high affinity to SARS-CoV-2 genome and low side effects. The suggested candidates are promising therapeutics for the experimental evaluations and may speed up the procedure of treatment design.
The preprint version is available in 

## Analysis schema
<p align="center">
  <img src="https://github.com/nrohani/SARS-CoV-2/blob/master/schema.jpg?raw=true" alt="Analysis overview"/>
</p>

In this research project, we addressed these questions using computational methods:

### Analysis1: Can human miRNAs be helpful in the treatment of SARS-CoV-2?
See results in [Analysis1.xlsx](https://github.com/nrohani/SARS-CoV-2/blob/master/Result%20and%20Data/Analysis1.xlsx).
### Analysis2: Can bat miRNAs be helpful in the treatment of SARS-CoV-2?
See results in [Analysis2.xlsx](https://github.com/nrohani/SARS-CoV-2/blob/master/Result%20and%20Data/Analysis2.xlsx).
### Analysis3: Can miRNAs of other species be helpful in the treatment of SARS-CoV-2?
See results in [Analysis3.xlsx](https://github.com/nrohani/SARS-CoV-2/blob/master/Result%20and%20Data/Analysis3.xlsx).
### Analysis4: Suggesting efficient siRNA for the treatment of SARS-CoV-2
See results in Result and Data folder.

### Prerequisites and Installing packages

1. Install Python 3.x
2. Install biopython
3. Install IntaRNA
4. Install subprocess
5. Install Pandas
```
pip install biopython

conda install -c conda-forge -c bioconda intarna

pip install subprocess.run

pip install pandas
```
Alternatively, you can use [IntaRNA WebTool](http://rna.informatik.uni-freiburg.de/CopraRNA/Input.jsp) for calculating MFE.  
1. Finding UCRs: Candidate UCRs are calculated using codes in [this repository]( https://github.com/DasLab/SARSCoV2_Secstruct_Cons).
2. Computing MFE : You can compute MFE with IntaRNA.py (address path of miRNA sequences and UCR files, then run the code) or use IntaRNA WebTool.
3. Investigating possible side-effects: For finding probable targets for candidate miRNA/ siRNA, we used [mirDB WebTool](http://mirdb.org/custom.html). The top possible target is enriched on [UniProt](https://www.uniprot.org/) and [Reactome](https://reactome.org/).
4. Suggesting siRNAs:  [siDirect WebTool](http://sidirect2.rnai.jp/) is used for designing potential siRNAs.
You can find all results and data in Results and dataset folder in this repository.
### Materials
The complete genome sequence of SARS-CoV-2 was obtained with accession No. NC045512.2
from the [GeneBank database](https://www.ncbi.nlm.nih.gov/genbank/sars-cov-2-seqs/). The complete genome of betacoronavirus sequences from the NCBI database and sequences compiled by [Ceraolo and Giorgi](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7166773/) were considered for finding evolutionarily conserved regions.
Besides, the sequences of known miRNAs in human and other species were downloaded from
the miRNA registry, [MirBase](http://www.mirbase.org/). 
We obtained the sequences of bat-specific miRNAs from the previously published paper by [Huang et al.](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-3227-8).
Also, the miRNA-mRNA interaction data, as well as the free binding energy of interactions and
the sequences of miRNAs and mRNAs involving in the interactions were collected from [CLASH](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3650559/).


## Authors
###
* **Narjes Rohani**, **Fatemeh Ahmadi Moughari**  and **Changiz Eslahchi**
Please do not hesitate to contact us if you have any question:
Mail: n.rohani@mail.sbu.ac.ir


Please cite the paper if you find this study helpful.
