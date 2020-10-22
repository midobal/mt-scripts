# Approximate Randomization Testing
This repository contains a package that allows to perform two-sided paired
approximate randomization tests to assess the statistical significance of the
difference in performance between two systems.

## Usage
you can perform a test by running the following command:

```
python approximate_randomization.py system1 system2 {repetitions}
```

where `system1` and `system2` are the scores achieved by each systems (see [input format](#input-format) for details about the format) and `repetitions` is the number of trials to compute (default: 10000).

## Input Format
We assume that we want to check the statistical significance of the
difference in score between two systems S and T on the same corpus C. To
compute the score over the whole corpus, we compute for each document all
scores needed to compute the final score, and then aggregate the above values
 over the whole corpus to compute an aggregated score.

Hence, we assume that the input files contain in the i-th line

```
score_1 score_2 ... score_n
```

for the i-th document in the corpus. That is, a list of numbers divided by
space.

## Examples
So far, three aggregation functions are implemented: average, dividing sums
(suitable for precision and recall) and F1 score. All these are implemented in
`aggregators.py`. We now briefly describe each such function and the expected
input format for the `ApproximateRandomizationTest` object.

### Average
Aggregation function `average`. Expected input is a file containing one
number per line. The function just computes the average of all the numbers.

### Dividing sums
Aggregations function `enum_sum_div_by_denom_sum`. Expected input is a file
containing two numbers per line. The first number is interpreted as the
enumerator, the second number as the demoninator. The aggregated score is
computed by summing over each and then dividing. One use-case of this
aggregation function is to compute recall or precision.

### F1
Aggregations function `f_1`. Expected input is a file containing four numbers
per line. The first two numbers are interpreted as enumerator and denominator
for recall, the third and fourth number accordingly for precision. The
aggregated score is aggregating recall and precision individually, by dividing
sums, and then computing the F1 score.

## Converting CoNLL Coreference Score Files
This repository also contains a module to create the required input from the
output of the CoNLL coreference scorer
(http://code.google.com/p/reference-coreference-scorers/).

First, score the output of a system using the scorer, for one metric, as in

```
$ perl scorer.pl muc key response > conll_score_file
```

Then employ `get_numerators_and_denominators` from `transform_conll_score` to
transform the file into an object which can be used for scoring:

```python
from art import aggregators
from art import scores
from art import significance_tests
from art import transform_conll_score_file as transform


transformed_system1 = transform.get_numerators_and_denominators(
                        open('conll_score_file'))
transformed_system2 = transform.get_numerators_and_denominators(
                        open('another_conll_score_file'))

test = significance_tests.ApproximateRandomizationTest(
    scores.Scores(transformed_system1),
    scores.Scores(transformed_system2),
    aggregators.f_1)
test.run()
```
