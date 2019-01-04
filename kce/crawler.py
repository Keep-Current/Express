import arxiv
from kce.timed_cache import timed_cache

class Fetcher:
    def __init__(self):
        self.categ_ml = [
            "cat:cs.CV",
            "cat:cs.AI",
            "cat:cs.LG",
            "cat:cs.CL",
            "cat:cs.NE",
            "cat:stat.ML",
        ]

        self.categ_bio = [
            "cat:q-bio.BM",
            "cat:q-bio.CB",
            "cat:q-bio.GN",
            "cat:q-bio.MN",
            "cat:q-bio.NC",
            "cat:q-bio.OT",
            "cat:q-bio.PE",
            "cat:q-bio.QM",
            "cat:q-bio.SC",
            "cat:q-bio.TO",
        ]

    @timed_cache(hours=2)
    def arxiv(self, subject="ml"):
        categ = self.categ_bio if subject == "bio" else self.categ_ml
        return arxiv.query(sort_by="lastUpdatedDate", search_query=" OR ".join(categ))

