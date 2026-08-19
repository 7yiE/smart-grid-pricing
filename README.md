# Smart Grid Dynamic Pricing against Learning Users

Research project: how should an electricity aggregator set dynamic prices when users update their demand strategies with the Hedge (multiplicative weights) learning algorithm?

## Status

- [ ] Read related papers
- [ ] Model formulation
- [ ] Baseline: static Stackelberg pricing
- [ ] Simulation: Hedge users
- [ ] Dynamic programming solver
- [ ] Periodicity analysis
- [ ] Conference draft (CCDC 2027)

## Repository layout

- `academic-paper/` - paper outline and LaTeX draft
- `academic-paper/main-zh.tex` - Chinese draft of the paper
- `code/` - Python simulation and experiments
- `docs/` - notes and reading materials

## Reproduce

```bash
pip install -r requirements.txt
python code/simulation.py
```

## Related papers

- Xinxiang Guo, Yifen Mu. The Optimal Strategy against Hedge Algorithm in Repeated Games. arXiv:2312.09472.
- Yifen Mu et al. An Optimal Pricing Formula for Smart Grid based on Stackelberg Game. arXiv:2407.09948.
- Yuan Deng et al. Strategizing against No-regret Learners. NeurIPS 2019.

## Planned paper

**Working title:** Periodic Optimal Dynamic Pricing against Online-Learning Users in Smart Grid Demand Response

Main claim: when users are Hedge learners, the optimal price sequence eventually becomes periodic, and periodic pricing outperforms static Stackelberg pricing.
