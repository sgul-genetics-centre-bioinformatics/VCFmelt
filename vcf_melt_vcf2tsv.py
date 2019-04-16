#!/usr/bin/env python
"""
Genetics Centre Bioinformatics - St George's University of London - 2019
########################################################################
Melt a VCF file into a tab delimited set of calls, one per line

This script reads vcf on stdin and writes all calls to stdout in a more
easily readable tab delimited format with one call per line.
"""

import sys
import csv
import vcf

out = csv.writer(sys.stdout, delimiter='\t')
if len(sys.argv) > 1:
    inp = file(sys.argv[1])
else:
    inp = sys.stdin
reader = vcf.VCFReader(inp)

formats = ["GT","AD","DP","GQ","PL"]
infos = reader.infos.keys()
samples=reader.samples

header = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER'] + ['info.' + x for x in infos] + ["FORMAT"] + samples

out.writerow(header)

def flatten(x):
    if type(x) == type([]):
        x = ','.join(map(str, x))
    return x

for record in reader:
    info_row = [flatten(record.INFO.get(x, None)) for x in infos]
    fixed = [record.CHROM, record.POS, record.ID, record.REF, record.ALT, record.QUAL, record.FILTER]
    row = fixed
    row += info_row
    row += [":".join(formats)]
    for sample in record.samples:
        # Format fields not present will simply end up "blank"
        # in the output
        samatt = [flatten(getattr(sample.data, x, ".")) for x in formats]
        samatt = [str(x) for x in samatt]
        samatt = ["." if x=="None" or x==None or x=="" else x for x in samatt]
        row+=[":".join(samatt)]

    row = ["." if x=="None" or x==None or x=="" else x for x in row]
    row = ["PASS" if x == [] else x for x in row]
    out.writerow(row)


