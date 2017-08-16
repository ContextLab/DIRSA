# -*- coding: utf-8 -*-
from . import helpers
from nltools.data import Brain_Data
from nltools.mask import expand_mask, collapse_mask

def map_over_parcels(parcels, func):
    """
    Maps a function over brain parcels

    Parameters
    ----------
    parcels : list
        List of samples by voxels arrays

    func : function
        Function to map over parcels

    Returns

    ----------

    """
    return map(function, parcels)


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
def io_ratio():
    """In group Out group ratio"""
    pass

def dynamic_kmeans():
    """Compute dynamic k-means"""
    pass

def dynamic_kmeans_stats():
    "Get k-means stats"
    pass
