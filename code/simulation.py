"""Dynamic pricing simulation against Hedge-learning users."""

import os

import numpy as np

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


DEMAND_LEVELS = np.array([1.0, 2.0])
VALUE_LEVELS = np.array([2.0, 1.0])
PRICE_GRID = np.arange(0.2, 2.0 + 1e-9, 0.2)
ETA = 0.1
HORIZON = 200
N_USERS = 1
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def utility(price):
    return VALUE_LEVELS - price * DEMAND_LEVELS


def user_probs(weights):
    return weights / weights.sum()


def update_weights(weights, payoffs, eta=ETA):
    return weights * np.exp(eta * payoffs)


def expected_revenue(price, probs):
    demand = float(np.dot(probs, DEMAND_LEVELS))
    return price * N_USERS * demand


def run_price_sequence(prices, eta=ETA):
    weights = np.ones_like(DEMAND_LEVELS)
    probs_history = np.zeros((len(prices), len(DEMAND_LEVELS)))
    revenue_history = np.zeros(len(prices))
    for t, price in enumerate(prices):
        probs = user_probs(weights)
        probs_history[t] = probs
        revenue_history[t] = expected_revenue(price, probs)
        weights = update_weights(weights, utility(price), eta)
    return probs_history, revenue_history


def rational_demand(price):
    return DEMAND_LEVELS[np.argmax(utility(price))]


def static_stackelberg_price():
    revenues = [price * rational_demand(price) for price in PRICE_GRID]
    return PRICE_GRID[int(np.argmax(revenues))]


def best_grid_price(probs):
    revenues = [expected_revenue(price, probs) for price in PRICE_GRID]
    return PRICE_GRID[int(np.argmax(revenues))]


def myopic_price_sequence(eta=ETA):
    weights = np.ones_like(DEMAND_LEVELS)
    prices = np.zeros(HORIZON)
    for t in range(HORIZON):
        probs = user_probs(weights)
        prices[t] = best_grid_price(probs)
        weights = update_weights(weights, utility(prices[t]), eta)
    return prices


def periodic_price_sequence():
    # Placeholder: alternate between two candidate prices.
    # Replace this with the period recovered from the DP solver.
    cycle = np.array([0.8, 1.4])
    repeats = HORIZON // len(cycle) + 1
    return np.tile(cycle, repeats)[:HORIZON]


def cumulative_revenue(prices):
    _, revenues = run_price_sequence(prices)
    return np.cumsum(revenues)


def plot_comparison(static_prices, myopic_prices, periodic_prices):
    if not HAS_MATPLOTLIB:
        print("matplotlib not available; skipping figure")
        return

    os.makedirs(RESULTS_DIR, exist_ok=True)
    time = np.arange(HORIZON)
    static_cum = cumulative_revenue(static_prices)
    myopic_cum = cumulative_revenue(myopic_prices)
    periodic_cum = cumulative_revenue(periodic_prices)

    fig, axes = plt.subplots(2, 1, figsize=(7, 6), sharex=True)

    axes[0].plot(time[:60], static_prices[:60], label="Static Stackelberg", marker="o", markersize=3)
    axes[0].plot(time[:60], myopic_prices[:60], label="Myopic", marker="s", markersize=3)
    axes[0].plot(time[:60], periodic_prices[:60], label="Periodic heuristic", marker="^", markersize=3)
    axes[0].set_ylabel("Price")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(time, static_cum, label="Static Stackelberg")
    axes[1].plot(time, myopic_cum, label="Myopic")
    axes[1].plot(time, periodic_cum, label="Periodic heuristic")
    axes[1].set_xlabel("Stage t")
    axes[1].set_ylabel("Cumulative revenue")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    figure_path = os.path.join(RESULTS_DIR, "comparison.png")
    fig.savefig(figure_path, dpi=150, bbox_inches="tight")
    print(f"Figure saved: {figure_path}")


def main():
    static_price = static_stackelberg_price()
    static_prices = np.full(HORIZON, static_price)
    myopic_prices = myopic_price_sequence()
    periodic_prices = periodic_price_sequence()

    static_cum = cumulative_revenue(static_prices)
    myopic_cum = cumulative_revenue(myopic_prices)
    periodic_cum = cumulative_revenue(periodic_prices)

    print(f"Static Stackelberg price: {static_price:.2f}")
    print(f"Final cumulative revenue, static: {static_cum[-1]:.3f}")
    print(f"Final cumulative revenue, myopic: {myopic_cum[-1]:.3f}")
    print(f"Final cumulative revenue, periodic heuristic: {periodic_cum[-1]:.3f}")

    plot_comparison(static_prices, myopic_prices, periodic_prices)


if __name__ == "__main__":
    main()
