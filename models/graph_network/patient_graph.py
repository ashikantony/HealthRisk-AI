import networkx as nx
import pandas as pd


class PatientGraphBuilder:

    def __init__(self):
        self.graph = nx.Graph()

    def build_graph(
        self,
        dataframe,
        patient_id_col="patient_id",
        diagnosis_col="diagnosis"
    ):

        patients = dataframe[
            patient_id_col
        ].unique()

        for patient in patients:
            self.graph.add_node(patient)

        grouped = dataframe.groupby(
            diagnosis_col
        )

        for _, group in grouped:

            patient_ids = group[
                patient_id_col
            ].tolist()

            for i in range(
                len(patient_ids)
            ):
                for j in range(
                    i + 1,
                    len(patient_ids)
                ):

                    self.graph.add_edge(
                        patient_ids[i],
                        patient_ids[j]
                    )

        return self.graph

    def statistics(self):

        return {
            "nodes":
                self.graph.number_of_nodes(),
            "edges":
                self.graph.number_of_edges(),
            "density":
                nx.density(self.graph)
        }