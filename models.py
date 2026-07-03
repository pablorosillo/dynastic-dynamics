import numpy as np
from tqdm.auto import tqdm

def draw_truncated_power_law(alpha, cutoff):
    """
    Draws a random sample from a truncated power-law distribution.
    P(K) ~ K^(-alpha) for 1 <= K <= cutoff
    """
    r = np.random.rand()
    if alpha == 1.0:
        return np.exp(r * np.log(cutoff))
    else:
        term = 1.0 - r * (1.0 - cutoff**(1.0 - alpha))
        return term**(1.0 / (1.0 - alpha))

def simulate_all_models(t_max, rho, alpha, cutoff, n_sims=100):
    """
    Simulates the abundance variance trajectories for the RIP, RGR, and Random models.
    
    Parameters:
    -----------
    t_max : int
        Total number of successions (time steps).
    rho : float or np.ndarray
        Innovation rate. Can be a fixed scalar or a time-varying array of length t_max.
    alpha : float
        Power-law exponent for prestige increments.
    cutoff : float
        Upper bound kappa for prestige increments.
    n_sims : int, optional
        Number of Monte Carlo simulations to perform (default 100).
    """
    rho_array = np.full(t_max, rho) if np.isscalar(rho) else np.asarray(rho)
    
    Var_sims_rip = np.zeros((n_sims, t_max))
    Var_sims_rgr = np.zeros((n_sims, t_max))
    Var_sims_rand = np.zeros((n_sims, t_max))

    for s in tqdm(range(n_sims), desc="Simulating Models"):
        # RIP Trackers
        counts_rip = []
        prestiges_rip = []
        
        # RGR & Random Trackers
        counts_rgr = []
        counts_rand = []

        for t in range(t_max):
            current_rho = rho_array[t]

            # 1. RIP MODEL
            if np.random.rand() < current_rho or len(counts_rip) == 0:
                counts_rip.append(1)
                prestiges_rip.append(draw_truncated_power_law(alpha, cutoff))
            else:
                p_arr = np.array(prestiges_rip, dtype=float)
                probs = p_arr / p_arr.sum()
                idx = np.random.choice(len(counts_rip), p=probs)
                counts_rip[idx] += 1
                prestiges_rip[idx] += draw_truncated_power_law(alpha, cutoff)
            Var_sims_rip[s, t] = np.var(counts_rip)

            # 2. RGR MODEL
            if np.random.rand() < current_rho or len(counts_rgr) == 0:
                counts_rgr.append(1)
            else:
                c_arr = np.array(counts_rgr, dtype=float)
                probs = c_arr / c_arr.sum()
                idx = np.random.choice(len(counts_rgr), p=probs)
                counts_rgr[idx] += 1
            Var_sims_rgr[s, t] = np.var(counts_rgr)

            # 3. RANDOM MODEL
            if np.random.rand() < current_rho or len(counts_rand) == 0:
                counts_rand.append(1)
            else:
                idx = np.random.choice(len(counts_rand))
                counts_rand[idx] += 1
            Var_sims_rand[s, t] = np.var(counts_rand)

    return {
        'Var_mean_rip': np.mean(Var_sims_rip, axis=0),
        'Var_mean_rgr': np.mean(Var_sims_rgr, axis=0),
        'Var_mean_rand': np.mean(Var_sims_rand, axis=0),
        'Var_std_rip': np.std(Var_sims_rip, axis=0),
        'Var_std_rgr': np.std(Var_sims_rgr, axis=0),
        'Var_std_rand': np.std(Var_sims_rand, axis=0),
    }
