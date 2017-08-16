# -*- coding: utf-8 -*-
from . import helpers
from nltools.data import Brain_Data
from nltools.mask import expand_mask, collapse_mask

def get_complexity(data, complexity_func=None):
    """
    Returns a neural 'complexity' timeseries

    Parameters
    ----------

    Returns
    ----------

    """
    pass

# Jeremy's functions

def io_ratio(observations, group_labels):
    """Compute in-group out-group ratio"""
    group_labels = np.array(group_labels)
    unique_groups = np.unique(group_labels)
    in_group = 0.0
    out_group = 0.0

    for g in unique_groups:
        if np.sum(group_labels == g) == 0:
            continue

        in_obs = np.array(observations[group_labels == g, :], ndmin=2)
        out_obs = np.array(observations[group_labels != g, :], ndmin=2)

        in_group += np.mean(pdist(in_obs))
        out_group += np.mean(cdist(in_obs, out_obs))

    return in_group / out_group

def dynamic_kmeans(observations, minK, maxK, n, statfun=io_ratio):
    '''
    observations: T by V numpy array of observations
    minK, maxK: minimum and maximum values of K to use
    n: number of timepoints
    statfun: takes in an observations matrix and cluster labels; returns a clustering stat
    '''

    stats = np.zeros([observations.shape[0] - n + 1, maxK - minK])
    for t in np.arange(stats.shape[0]):
        next_obs = observations[t:(t+n), :]
        stats[t, :] = np.array(list(map(lambda k: statfun(next_obs.T, hyp.tools.cluster(next_obs.T, n_clusters=k)),
                                   np.arange(minK, maxK))))
    return stats
