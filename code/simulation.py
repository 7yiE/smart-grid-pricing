"""Minimal simulation skeleton for dynamic pricing against Hedge-learning users."""

import numpy as np


def hedge_update(weights, payoffs, eta):
    """Update Hedge weights and return normalized probabilities."""
    weights = weights * np.exp(eta * payoffs)
    return weights / weights.sum()


def expected_demand(probs, demand_levels):
    """Expected demand of one user."""
    return float(np.dot(probs, demand_levels))


def revenue(price, total_demand):
    """Aggregator revenue at one stage."""
    return price * total_demand


def main():
    # Placeholder example: two demand levels, one user, two prices.
    demand_levels = np.array([1.0, 2.0])
    eta = 0.1
    weights = np.ones_like(demand_levels)

    for price in [1.0, 2.0]:
        payoffs = np.array([2.0 - price, 1.0 - 0.5 * price])
        probs = hedge_update(weights, payoffs, eta)
        weights = probs
        print(f"price={price}, probs={probs}, demand={expected_demand(probs, demand_levels):.3f}")


if __name__ == "__main__":
    main()
