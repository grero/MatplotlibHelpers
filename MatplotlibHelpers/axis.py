import numpy as np
import matplotlib.pylab as plt

def twinx(ax=None):
    """
    Similar to matplotlib.Axes.twinx, but attempts to re-use
    an already existing axis in the same position as `ax`, if
    it exists.
    """
    if ax is None:
        ax = plt.gca()
    fig = ax.figure
    if len(fig.axes) > 1:
        pos0 = ax.get_position()
        for _ax in fig.axes:
            if _ax == ax:
                continue
            pos1 = _ax.get_position()
            if np.allclose(pos0.get_points(), pos1.get_points()):
                return _ax

    # default is to just run ax.twinx
    return ax.twinx()

