# Data Setup Guide

## Full Dataset

The complete MedQuAD dataset (16,000+ Q&A pairs) is not included due to size.

### To get the full data:

1. Clone the original MedQuAD dataset:
```bash
   git clone https://github.com/abachaa/MedQuAD.git
```

2. Run the data processing notebook `01_data_exploration.ipynb`

This generates `medquad_clean.csv` with ~16,000 cleaned Q&A pairs.

## Sample Data

A sample of 1,000 Q&A pairs is included as `medquad_sample_1000.csv` 
for quick testing.

## Dataset Info
- Source: National Institutes of Health (NIH)
- Original: 47,457 Q&A pairs
- Cleaned: ~16,000 pairs
- 12 medical sources
