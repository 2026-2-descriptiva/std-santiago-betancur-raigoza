from pathlib import Path


def test_01():
    submission = Path(__file__).resolve().parents[1] / "submission"
    assert (submission / "authors_frequency.csv").is_file()
    assert (submission / "country_clusters.txt").is_file()
    assert (submission / "country_collab_network.html").is_file()
    assert (submission / "country_cooc_heatmap.html").is_file()
    assert (submission / "country_cooc_matrix.csv").is_file()
    assert (submission / "country_frequency.csv").is_file()
    assert (submission / "country_frequency_plot.html").is_file()
    assert (submission / "documents_by_year.html").is_file()
    assert (submission / "keywords_clusters.txt").is_file()
    assert (submission / "keywords_cooc_matrix.csv").is_file()
    assert (submission / "keywords_cooc_network.html").is_file()
    assert (submission / "keywords_frequency.csv").is_file()
    assert (submission / "scopus.csv.gz").is_file()
    assert (submission / "source_frequency.csv").is_file()
    assert (submission / "world_map.html").is_file()
