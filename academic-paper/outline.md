# Paper Outline

**Working title:** Periodic Optimal Dynamic Pricing against Online-Learning Users in Smart Grid Demand Response

**One-sentence contribution:** When users update demand with the Hedge learning algorithm, the optimal price sequence eventually becomes periodic, and periodic pricing outperforms static Stackelberg pricing.

## 1. Introduction

- Smart grid demand response and dynamic pricing background.
- Users are increasingly algorithm-driven rather than fully rational.
- Related work: Stackelberg pricing with rational users; optimal strategies against Hedge in repeated games.
- Gap: dynamic pricing against learning users.
- Contributions: model, state-transition formulation, periodicity result, efficient algorithm, numerical validation.

## 2. Problem Formulation

- Finite horizon T, one aggregator, N users.
- Price set P, demand action set D.
- User utility: u_i(d, p) = v_i(d) - p*d.
- Hedge update:
  - w_{i,a,t+1} = w_{i,a,t} exp(eta * u_i(a, p_t))
  - x_{i,a,t} = w_{i,a,t} / sum_b w_{i,b,t}
- Aggregator revenue: R_t = p_t * sum_i sum_a x_{i,a,t} * d_a.
- Objective: maximize sum of R_t.
- Assumptions: finite sets, known learning rate, independent users, commensurable state steps.
- Baseline: static Stackelberg pricing.

## 3. State Dynamics and Bellman Equation

- State s_t is the cumulative term in the Hedge weights.
- Transition: s_{t+1} = s_t + Delta(p_t).
- State transition graph similar to STTG.
- Bellman equation:
  - V_t(s) = max_p [ p * D_t(p, s) + V_{t+1}(s + Delta(p, s)) ]
  - Terminal condition V_{T+1}(s) = 0.
- Complexity of direct DP: O(T * |S| * |P|).

## 4. Structural Properties and Algorithm

- Proposition: constant Stackelberg pricing is not globally optimal against Hedge users.
- Numerical observation: optimal price sequence enters a period after a transient.
- Conjecture/theorem: with commensurable state steps, the optimal price sequence is eventually periodic.
- Algorithm: periodic dynamic programming with transient detection.
- Complexity comparison with direct DP.

## 5. Numerical Experiments

- Settings: T = 1000, N = 1/10/50, eta = 0.01/0.1/0.5.
- Baselines: static Stackelberg, myopic pricing, constant price.
- Metrics: cumulative revenue, average revenue per period, relative gain, transient length, period length.
- Figures: price trajectory, revenue curves, gain heatmap, period length curves.

## 6. Conclusion

- Summary.
- Limitations: discrete prices, known learning rate, independent users, no storage.
- Future work: decaying learning rate, unknown algorithms, heterogeneous users, multi-aggregator competition.
