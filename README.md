# VCFmelt
**Python2 scripts to convert VCF (Variant Calling Format) files to easily readable tab-delimited files (tsv).**

**vcf_melt.py**: Melt a VCF file into a tab delimited set of calls, one per sample per line.-
- VCF files have all the calls from different samples on one line.  This script reads vcf on stdin and writes all calls to stdout in tab delimited format with one call in one sample per line.  This makes it easy to find a given sample's genotype with, say, grep.
  
  Usage: python vcf_melt.py input.vcf > output.txt
  
**vcf_melt_vcf2tsv.py**: Melt a VCF file into a tab delimited set of calls, one per line.
- This script reads vcf on stdin and writes all calls to stdout in a more easily readable tab delimited format with one call per          line.
  
  Usage: python vcf_melt_vcf2tsv.py input.vcf > output.txt
  
**DEPENDENCIES**
- Python: These scripts have been developed and tested in Python2.7. Feel free to update them.
- [PyVCF 0.6.8](https://pypi.org/project/PyVCF/)
