from datetime import datetime

import arxiv
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

    def arxiv(self, subject="ml"):
        categ = self.categ_bio if subject == "bio" else self.categ_ml
        invalidate_cache = False

        if self._cache_date[categ]:
            cache_delta = self._cache_date[categ] - datetime.today()
            invalidate_cache = True if cache_delta.days > 1 else False

        if not self._cache[categ] or invalidate_cache:
            self._cache[categ] = arxiv.query(sort_by="lastUpdatedDate", search_query=" OR ".join(categ))
            self._cache_date[categ] = datetime.today()

        return self._cache[categ]

