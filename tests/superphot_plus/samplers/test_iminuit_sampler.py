import numpy as np

from superphot_plus.samplers.iminuit_sampler import IminuitSampler


def test_iminuit_single_file(
    test_ztf_photometry,
    ztf_priors,
    test_sampler_result
):
    """Just test that we generated a new file with fits"""
    sampler = IminuitSampler(
        priors=ztf_priors, random_state=np.random.default_rng(9876)
    )
    sampler.fit_photometry(test_ztf_photometry)
    sample_mean = np.mean(sampler.result.fit_parameters, axis=0)
    assert sampler.result.fit_parameters.shape == (100, 14)

    # Check that the same means the same order of magnitude (within 50% relative value).
    # Despite setting the the random seed, we still need to account (so far) unexplained
    # additional variations.
    expected_mean = np.mean(test_sampler_result.fit_parameters, axis=0)
    assert len(expected_mean) == len(sample_mean)
    assert np.all(np.isclose(sample_mean, expected_mean, rtol=0.5, atol=0.2))
