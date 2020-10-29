# Scatter Plotting Metrics
Computes BLEU from a hypothesis file with respect to one or more reference files and computes significant differences using ART (Approximate Randomization Tests).

## Requirements
You can install the requirements by doing:
```
pip install tables scipy
```

## Usage
```
python scatterplot_metrics.py [-h] [-t HYPOTHESES [HYPOTHESES ...]]
                              [-r REFERENCES [REFERENCES ...]]
                              [-b BASELINES [BASELINES ...]]
                              [-br BASE_REFERENCES [BASE_REFERENCES ...]]
                              [-l LEGEND [LEGEND ...]] [-sm] [-s SIZE]
                              [-x X_LABEL] [-y Y_LABEL] [-tlt TITLE]
                              [-samples INTERPOLATION_SAMPLES]

optional arguments:
  -h, --help            show this help message and exit
  -t HYPOTHESES [HYPOTHESES ...], --hypotheses HYPOTHESES [HYPOTHESES ...]
                        Hypotheses files
  -r REFERENCES [REFERENCES ...], --references REFERENCES [REFERENCES ...]
                        Path to all the reference files
  -b BASELINES [BASELINES ...], --baselines BASELINES [BASELINES ...]
                        Baseline files
  -br BASE_REFERENCES [BASE_REFERENCES ...], --base-references BASE_REFERENCES [BASE_REFERENCES ...]
                        Baseline references file
  -l LEGEND [LEGEND ...], --legend LEGEND [LEGEND ...]
                        Legend of the data to plot.
  -sm, --smooth         Legend of the data to plot.
  -s SIZE, --size SIZE  Font size.
  -x X_LABEL, --x-label X_LABEL
                        X-axis label
  -y Y_LABEL, --y-label Y_LABEL
                        y-axis label
  -tlt TITLE, --title TITLE
                        Title label
  -samples INTERPOLATION_SAMPLES, --interpolation-samples INTERPOLATION_SAMPLES
                        Title label

```

## Example
```
python scatterplot_metrics.py --hypotheses hypothesis1 --references reference1 \
--baselines hypothesis2 --base-references reference2  -samples 10 \
--x-label "# Sentences" --y-label "hBLEU"
```
