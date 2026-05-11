import networkx as nx
import stompx as sx


def test_gillespie_sir_runs():
    G = nx.erdos_renyi_graph(20, 0.2, seed=42)

    model = sx.Gillespie_SIR_Network(
        G,
        beta=0.4,
        gamma=0.3,
        num_initial_infected=1
    )

    model.run_simulation(tmax=5)

    assert hasattr(model, "time")
    assert hasattr(model, "network_history")
    assert len(model.time) == len(model.network_history)
    assert len(model.network_history)  > 0
def test_montecarlo_sir_runs():
    G = nx.erdos_renyi_graph(20, 0.2, seed=42)

    model = sx.Montecarlo_SIR_Network(
        G,
        h=2,
        gamma=0.3,
        num_initial_infected=1
    )

    model.run_simulation(steps=10)

    assert hasattr(model, "time")
    assert hasattr(model, "network_history")
    assert len(model.time) == len(model.network_history)
    assert len(model.network_history) > 0