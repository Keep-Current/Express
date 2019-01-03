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
        papers = arxiv.query(sort_by="lastUpdatedDate", search_query=" OR ".join(categ))

        return papers

