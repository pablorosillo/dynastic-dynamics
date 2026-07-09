# Dynastic dynamics: Modeling powerful naming choices with stochastic prestige

This repository provides the official implementation of the models introduced in *"Dynastic dynamics: Modeling powerful naming choices with stochastic prestige"* (2026).

## Abstract
The naming choices of powerful rulers encode millennia of cultural, political, and institutional change. Here we examine the onomastic record of several ruling dynasties, including Roman emperors, Egyptian pharaohs, popes, and kings. We show that their naming choices are not captured by random reuse or by frequency-based rich-get-richer mechanisms alone, but are better described by a reinforcement process shaped by rare but high-impact stochastic prestige increments driving the interplay between innovation and name reuse. With our model, we capture the strong inequalities in name use, the persistence of dominant names, and the abrupt rises in popularity observed across historical sequences. Our results suggest that ruling-name traditions preserve institutional memory through reinforcement, while remaining sensitive to rare historical events that can reshape the hierarchy of names across generations.

## Naming models explained

This framework simulates and compares three competing choice dynamics to analyze how names are selected during succession events:

1. **RIP model (Reinforcement and Innovation through Prestige):** Reused names are chosen proportionally to their accumulated historical prestige. Each reign contributes a prestige increment $K$ drawn from a heavy-tailed, truncated power-law distribution ($1 \le K \le \kappa$). This captures how rare, highly influential reigns substantially elevate a name's standing.
2. **RGR model (the rich-get-richer):** A classic preferential attachment baseline where names are selected proportionally to their current frequency/abundance.
3. **Random copying model:** A neutral baseline where names are chosen uniformly at random from the existing active repertoire.

All models are refactored into a single, straightforward function inside the `models.py` file.

## Historical dataset reference

We provide the names used for the analysis in the `data.md` file.

Optimal parameters derived via root-mean-square error (RMSE) minimization across the studied dynasties:

| Dynasty / Tradition | Upper cutoff ($\kappa$) | Exponent ($\alpha$) | Dominant Mechanism |
| :--- | :---: | :---: | :--- |
| **Popes** | 209 | 3.07 | Prestige required |
| **Pharaohs** | 244 | 1.31 | Prestige required |
| **Roman emperors** | 585 | 2.71 | Prestige required |
| **Spanish monarchs** | 105 | 4.98 | Rich-get-richer explains |
| **Danish monarchs** | 374 | 3.90 | Rich-get-richer explains |
| **English monarchs** | 70 | 1.82 | Prestige required |
| **Constantinople patriarchs** | 330 | 4.22 | Rich-get-richer explains |
| **Ottoman sultans** | 1 | — | Random copying explains |
| **Russian tsars** | 1 | — | Random copying explains |
| **Holy Roman emperors** | 1 | — | Random copying explains |

## Code requirements

Ensure you have the following packages installed:
```bash
pip install numpy tqdm
```


## Citation
```
@article{rosillolamata2026,
  title={Dynastic dynamics: Modeling powerful naming choices with stochastic prestige},
  author={Rosillo-Rodes, Pablo and Lamata-Ot{\'i}n, Santiago and Soriano-Pa{\~n}os, David and H{\'e}bert-Dufresne, Laurent and Dodds, Peter Sheridan},
  journal={arXiv preprint},
  year={2026}
}
```
