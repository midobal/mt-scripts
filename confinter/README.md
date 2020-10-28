# Bootstrap Resampling
This repository contains software for computing BLEU, TER, WSR and MAR with their confidence interval through bootstrap resampling.

## BLEU and TER
You can compute BLEU and TER with confidence intervals by running:
```
./confidence_intervals.sh -r reference -t hypothesis -n repetitions
```

where `reference` is the reference text, `hypothesis` is the text whose quality you want to assess and `repetitions` are the number of repetitions to do via bootstrapping (e.g., 10000).

## WSR and MAR
You can compute WSR and MAR with confidence intervals by running:
```
./imt_confidence_intervals.sh -t scores -n repetitions
```

where `scores` is a file containing the pre-computed WSR and MAR scores at a sentence (i.e., the document will have a line for each sentence of the hypothesis, and each line will contain the WSR value and the MAR value) level and `repetitions` are the number of repetitions to do via bootstrapping (e.g., 10000).
