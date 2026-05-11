import networkx as nx
import stompx as sx


def test_compute_max_statistics_returns_expected_keys():
    G = nx.erdos_renyi_graph(20, 0.2, seed=42)

    model = sx.Gillespie_SIR_Network(
        G,
        beta=0.4,
        gamma=0.3,
        num_initial_infected=1
    )

    stats = sx.compute_max_statistics(
        model=model,
        n_sim=5,
        tmax=5,
        gillespie=True
    )

    expected_keys = {
        "I_max_values",
        "I_max_mean",
        "I_max_std",
        "extinction_prob",
        "extinction_time_values",
        "mean_extinction_time",
        "std_extincion_time"
    }

    assert expected_keys.issubset(stats.keys())
    assert len(stats["I_max_values"]) == 5