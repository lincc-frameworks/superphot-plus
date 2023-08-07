import numpy as np

from superphot_plus.posterior_samples import PosteriorSamples


def test_create():
    """Create new posterior samples object from some in-memory primitives."""
    single_sample = np.array(
        [[1035.0, 0.005, 13.5, -4.8, 4.0, 23.4, 0.03, 1.1, 1.0, 1.0, 1.0, 0.96, 0.56, 0.87, -5.43]]
    )
    posteriors = PosteriorSamples(single_sample, "nonsense", "dunno")

    assert posteriors.name == "nonsense"
    assert posteriors.sampling_method == "dunno"

    ## With only one sample, the mean == original values.
    sample_mean = posteriors.sample_mean()
    assert np.all(np.isclose(sample_mean, single_sample))


def test_from_file(test_data_dir, single_ztf_sn_id):
    """Test loading our test data eqwt posterior sample files."""
    posteriors = PosteriorSamples.from_file(
        input_dir=test_data_dir, name=single_ztf_sn_id, sampling_method="dynesty"
    )

    assert posteriors.name == single_ztf_sn_id
    assert len(posteriors.samples) == 706
    assert posteriors.sampling_method == "dynesty"

    posteriors = PosteriorSamples.from_file(
        input_dir=test_data_dir, name=single_ztf_sn_id, sampling_method="NUTS"
    )

    assert posteriors.name == single_ztf_sn_id
    assert len(posteriors.samples) == 300
    assert posteriors.sampling_method == "NUTS"

    posteriors = PosteriorSamples.from_file(
        input_dir=test_data_dir, name=single_ztf_sn_id, sampling_method="svi"
    )

    assert posteriors.name == single_ztf_sn_id
    assert len(posteriors.samples) == 100
    assert posteriors.sampling_method == "svi"

    posteriors = PosteriorSamples.from_file(input_dir=test_data_dir, name=single_ztf_sn_id)

    assert posteriors.name == single_ztf_sn_id
    assert len(posteriors.samples) == 706
    assert posteriors.sampling_method is None


def test_sample_mean(test_data_dir, single_ztf_sn_id):
    """Test loading our test data eqwt posterior sample files."""
    posteriors = PosteriorSamples.from_file(
        input_dir=test_data_dir, name=single_ztf_sn_id, sampling_method="dynesty"
    )
    sample_mean = posteriors.sample_mean()

    expected = np.array(
        [
            1.02634431e03,
            5.24005804e-03,
            1.24753632e01,
            -4.90112494e00,
            3.87467564e00,
            2.55498192e01,
            2.74747039e-02,
            1.14927743e00,
            1.04275890e00,
            1.00424340e00,
            9.99992300e-01,
            9.68815494e-01,
            5.75738837e-01,
            8.61389219e-01,
            -5.46663173e00,
        ]
    )

    assert len(expected) == len(sample_mean)
    ## We can expect very close values, because these are coming from a file, not computed on-the-fly.
    assert np.all(np.isclose(sample_mean, expected))


def test_write_and_read(tmp_path):
    """Create a posterior, save it, and reload."""
    single_sample = np.array(
        [[1035.0, 0.005, 13.5, -4.8, 4.0, 23.4, 0.03, 1.1, 1.0, 1.0, 1.0, 0.96, 0.56, 0.87, -5.43]]
    )
    posteriors = PosteriorSamples(single_sample, "nonsense")
    posteriors.save_to_file(tmp_path)

    fresh_posteriors = PosteriorSamples.from_file(input_dir=tmp_path, name="nonsense")

    assert fresh_posteriors.name == "nonsense"
    assert fresh_posteriors.sampling_method is None
