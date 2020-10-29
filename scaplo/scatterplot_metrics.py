# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
from read_write import *
from sentence_bleu import SentenceBleuScorer
from builtins import map, zip
import argparse
import aggregators
from scores import Scores, Score
import significance_tests
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from scipy import stats
from scipy import interpolate

# Initialize the figure
plt.style.use('seaborn-darkgrid')


parser = argparse.ArgumentParser(
    description="""Computes BLEU from a htypotheses file with respect to one or more reference files and compute significant differences using ART (approximate randomization tests).""", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-t', '--hypotheses', type=str, nargs='+',help='Hypotheses files')
parser.add_argument('-r', '--references', type=str, nargs='+', help='Path to all the reference files')
parser.add_argument('-b', '--baselines', type=str, nargs='+', help='Baseline files')
parser.add_argument('-br', '--base-references', type=str, help='Baseline references file',
                    nargs='+', required=False)
parser.add_argument("-l", "--legend", required=False, nargs='+',
                    help="Legend of the data to plot.")
parser.add_argument("-sm", "--smooth", required=False, action='store_true',
                    default=False, help="Legend of the data to plot.")
parser.add_argument("-s", "--size", required=False, type=int, default=30,
                    help="Font size.")
parser.add_argument("-x", "--x-label", required=False, default=None,
                    help="X-axis label")
parser.add_argument("-y", "--y-label", required=False, default=None,
                    help="y-axis label")
parser.add_argument("-tlt", "--title", required=False, default=None,
                    help="Title label")
parser.add_argument("-samples", "--interpolation-samples", required=False, default=10, type=int,
                    help="Title label")

def scatterplot(args, hypothesis, baseline, interpolation_samples=10, alpha=0.4,
                hypothesis_name='Adaptive', baseline_name='Static'):

    fig, ax = plt.subplots()

    # Create data
    x_baseline = np.arange(0, len(baseline))
    ax.scatter(x_baseline, baseline, alpha=alpha, label=str(baseline_name), color='xkcd:red')
    x_baseline = np.linspace(0, len(baseline), num=len(baseline), endpoint=True)
    # Interpolate points
    f = interpolate.interp1d(x_baseline, baseline, kind='cubic')
    x_new = np.linspace(0, len(x_baseline), num=interpolation_samples, endpoint=True)
    ax.plot(x_new, f(x_new), '--',  linewidth=3,color='xkcd:red')

    # Create data
    x_hypothesis = np.arange(0, len(hypothesis))
    ax.scatter(x_hypothesis, hypothesis, alpha=alpha, label=str(hypothesis_name), color='xkcd:azure')
    x_hypothesis = np.linspace(0, len(hypothesis), num=len(hypothesis), endpoint=True)
    # Interpolate points
    f = interpolate.interp1d(x_hypothesis, hypothesis, kind='cubic')
    x_new = np.linspace(0, len(x_hypothesis), num=interpolation_samples, endpoint=True)
    ax.plot(x_new, f(x_new), '--', color='xkcd:azure',  linewidth=3)

    leg = ax.legend()
    for line in leg.get_lines():
        line.set_linewidth(4.0)
    # fully use the given bounding box.
    leg = plt.legend(loc='upper center',
           ncol=2,
           bbox_to_anchor=(0., 1 + float(args.size) * 0.0001, 1., .102),
           shadow=False,
           fontsize=args.size,
           mode="expand",
           borderaxespad=0.)
    # set the linewidth of each legend object
    for legobj in leg.legendHandles:
        legobj.set_linewidth(4.0)
    # Add title
    if args.title is not None:
        ax.set_title(str(args.title), loc='left', fontsize=args.size + 10, fontweight=0)

    if args.x_label is not None:
        ax.set_xlabel(args.x_label, fontsize=args.size)
    if args.y_label is not None:
        ax.set_ylabel(args.y_label, fontsize=args.size)
    plt.tick_params(labelsize=args.size)
    fig.tight_layout()
    plt.show()
    return


def evaluate_from_file(args):
    """
    Evaluate translation hypotheses from a file or a list of files of references.
    :param args: Evaluation parameters
    :return: None
    """
    sentence_bleu_scorer = SentenceBleuScorer('')

    bleus_hypotheses = [] * len(args.hypotheses)
    for n_system, data_filename in list(enumerate(args.hypotheses)):
        hypotheses = file2list(data_filename)
        references = file2list(args.references[n_system])
        bleus = []
        for hyp_line, ref_line in zip(hypotheses, references):
            sentence_bleu_scorer.set_reference(ref_line.split())
            bleu = sentence_bleu_scorer.score(hyp_line.split()) * 100
            bleus.append(bleu)
        bleus_hypotheses.append(bleus)
    bleus_hypotheses = np.asarray(bleus_hypotheses)
    average_bleus = np.transpose(bleus_hypotheses).mean(axis=1)


    bleus_baselines = [] * len(args.baselines)
    for n_system, data_filename in list(enumerate(args.baselines)):
        hypotheses = file2list(data_filename)
        references = file2list(args.base_references[n_system])
        bleus = []
        for hyp_line, ref_line in zip(hypotheses, references):
            sentence_bleu_scorer.set_reference(ref_line.split())
            bleu = sentence_bleu_scorer.score(hyp_line.split()) * 100
            bleus.append(bleu)
        bleus_baselines.append(bleus)
    bleus_baselines = np.asarray(bleus_baselines)
    average_bleu_baselines = np.transpose(bleus_baselines).mean(axis=1)

    return average_bleus, average_bleu_baselines

if __name__ == "__main__":
    args = parser.parse_args()
    assert len(args.hypotheses) == len(args.references), 'Different number of hypotheses and reference files'
    assert len(args.baselines) == len(args.base_references), 'Different number of baseline and baseline reference files'


    system, baseline = evaluate_from_file(args)
    scatterplot(args, system, baseline, interpolation_samples=args.interpolation_samples)
