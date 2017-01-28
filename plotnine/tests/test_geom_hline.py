from __future__ import absolute_import, division, print_function

import pandas as pd
import pytest

from plotnine import ggplot, aes, geom_hline, geom_point
from plotnine.utils.exceptions import GgplotError

df = pd.DataFrame({
        'yintercept': [1, 2],
        'x': [-1, 1],
        'y': [0.5, 3],
        'z': range(2)
    })


def test_aesthetics():
    p = (ggplot(df) +
         geom_point(aes('x', 'y')) +
         geom_hline(aes(yintercept='yintercept'), size=2) +
         geom_hline(aes(yintercept='yintercept+.1', alpha='z'),
                    size=2) +
         geom_hline(aes(yintercept='yintercept+.2',
                        linetype='factor(z)'),
                    size=2) +
         geom_hline(aes(yintercept='yintercept+.3',
                        color='factor(z)'),
                    size=2) +
         geom_hline(aes(yintercept='yintercept+.4', size='z')))

    assert p == 'aesthetics'


def test_aes_inheritance():
    with pytest.raises(GgplotError):
        p = (ggplot(df, aes('x', 'y', yintercept='yintercept')) +
             geom_point() +
             geom_hline(size=2))
        print(p)