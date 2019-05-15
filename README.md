# data-mining-Apriori
Using apriori algorithm to find frequent pattern in abstracts of essays on arXiv

### Purpose
Given the minimum support, find the frequent patterns in a passage or an article. Ordering the frequent patterns by the number of appearance. 
### Usage
1. Open the jupyter notebook and run the cells.
2. Open anaconda prompt and enter the following command:
```
python frequent_pattern.py in1.txt out1.txt [minimum support]
```
The minimum support is your choice and must be a positive integer. The larger the value, the less frequent patterns.
If there's any trivial word you don't want to take into consideration, put it in stop_words.txt
