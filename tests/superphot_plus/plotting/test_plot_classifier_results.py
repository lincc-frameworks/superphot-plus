import os

import numpy as np
import pytest

from superphot_plus.plotting.classifier_results import (
    generate_roc_curve,
    plot_redshifts_abs_mags,
    plot_snr_npoints_vs_accuracy,
    plot_snr_hist,
    compare_mag_distributions,
    plot_chisquared_vs_accuracy,
)


def test_generate_roc_curve(class_probs_csv, tmp_path):
    """Test ROC curve generation."""
    generate_roc_curve(class_probs_csv, tmp_path)
    filepath = os.path.join(tmp_path, "roc_all.pdf")
    assert os.path.exists(filepath)


def test_plot_redshifts_abs_mags(class_probs_snr_csv, tmp_path):
    """Test redshift and abs magnitude plots are being generated."""
    plot_redshifts_abs_mags(class_probs_snr_csv, tmp_path)
    filepath = os.path.join(tmp_path, "abs_mag_hist.pdf")
    assert os.path.exists(filepath)


def test_plot_snr_npoints_vs_accuracy(class_probs_snr_csv, tmp_path):
    """Test whether SNR vs Npoints trends are being plotted."""
    plot_snr_npoints_vs_accuracy(class_probs_snr_csv, tmp_path)
    filepath = os.path.join(tmp_path, "n_vs_accuracy.pdf")
    assert os.path.exists(filepath)


def test_plot_snr_hist(class_probs_snr_csv, tmp_path):
    """Test whether SNR histograms are being plotted."""
    plot_snr_hist(class_probs_snr_csv, tmp_path)
    filepath = os.path.join(tmp_path, "snr_hist.pdf")
    assert os.path.exists(filepath)


def test_compare_mag_distributions(class_probs_snr_csv, tmp_path):
    """Test magnitude comparison plots are generated.
    TODO: add example photometric SNR CSV for proper generation.
    """
    compare_mag_distributions(class_probs_snr_csv, class_probs_snr_csv, tmp_path)
    filepath = os.path.join(tmp_path, "appm_hist_compare.pdf")
    assert os.path.exists(filepath)


def test_plot_chisquared_vs_accuracy(class_probs_csv, tmp_path):
    """Test plot generation showing chisquared histograms overlaid
    over chisquared vs accuracy trend.
    """
    """
    plot_chisquared_vs_accuracy(class_probs_csv, class_probs_csv, tmp_path)
    filepath = os.path.join(tmp_path, "chisq_vs_accuracy.pdf")
    assert os.path.exists(filepath)
    """
    # IN PROGRESS