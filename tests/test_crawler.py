from kce.crawler import Fetcher

def test_fetcher():
    f = Fetcher()
    papers = f.arxiv()
    if papers is None:
        raise AssertionError("papers is null")