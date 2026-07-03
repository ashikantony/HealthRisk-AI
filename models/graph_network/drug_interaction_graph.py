import networkx as nx


class DrugInteractionGraphBuilder:

    def __init__(self):

        self.graph = nx.Graph()

    def add_interaction(
        self,
        drug_a,
        drug_b,
        severity="moderate"
    ):

        self.graph.add_edge(
            drug_a,
            drug_b,
            severity=severity
        )

    def build_from_pairs(
        self,
        interactions
    ):

        for pair in interactions:

            self.add_interaction(
                pair["drug_a"],
                pair["drug_b"],
                pair.get(
                    "severity",
                    "moderate"
                )
            )

        return self.graph

    def get_interactions(
        self,
        drug_name
    ):

        if drug_name not in self.graph:
            return []

        return list(
            self.graph.neighbors(
                drug_name
            )
        )

    def statistics(self):

        return {
            "drugs":
                self.graph.number_of_nodes(),
            "interactions":
                self.graph.number_of_edges()
        }