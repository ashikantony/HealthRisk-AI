import networkx as nx


class DiseaseGraphBuilder:

    def __init__(self):

        self.graph = nx.Graph()

    def build_graph(
        self,
        patient_diseases
    ):

        for diseases in patient_diseases:

            diseases = list(
                set(diseases)
            )

            for disease in diseases:
                self.graph.add_node(
                    disease
                )

            for i in range(
                len(diseases)
            ):
                for j in range(
                    i + 1,
                    len(diseases)
                ):

                    disease_a = diseases[i]
                    disease_b = diseases[j]

                    if self.graph.has_edge(
                        disease_a,
                        disease_b
                    ):

                        self.graph[
                            disease_a
                        ][
                            disease_b
                        ][
                            "weight"
                        ] += 1

                    else:

                        self.graph.add_edge(
                            disease_a,
                            disease_b,
                            weight=1
                        )

        return self.graph

    def top_comorbidities(
        self,
        top_n=10
    ):

        edges = sorted(
            self.graph.edges(
                data=True
            ),
            key=lambda x:
                x[2]["weight"],
            reverse=True
        )

        return edges[:top_n]