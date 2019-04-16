#!/usr/bin/env python
"""
Genetics Centre Bioinformatics - St George's University of London - 2019
Dionysios Grigoriadis & Alan Pittman

#################################################################
Melt a VCF file into a tab delimited set of calls, one per line.


This script reads vcf on stdin and conerts it to TSV file. One call per line.
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

formats = reader.formats.keys()
infos = reader.infos.keys()

header = ["SAMPLE"] + formats + ['FILTER', 'CHROM', 'POS', 'REF', 'ALT', 'ID'] \
        + ['info.' + x for x in infos]


out.writerow(header)


def flatten(x):
    if type(x) == type([]):
        x = ','.join(map(str, x))
    return x

for record in reader:
    info_row = [flatten(record.INFO.get(x, None)) for x in infos]
    fixed = [record.CHROM, record.POS, record.REF, record.ALT, record.ID]

    for sample in record.samples:
        row = [sample.sample]
        # Format fields not present will simply end up "blank"
        # in the output
        row += [flatten(getattr(sample.data, x, None)) for x in formats]
        row += [record.FILTER or '.']
        row += fixed
        row += info_row
        out.writerow(row)