from __future__ import annotations

import typing

from .coord_cartesian import coord_cartesian

if typing.TYPE_CHECKING:
    from typing import Optional

    import plotnine as p9


class coord_fixed(coord_cartesian):
    """
    Cartesian coordinates with fixed relationship between x and y scales

    Parameters
    ----------
    ratio : float
        Desired aspect_ratio (:math:`y/x`) of the panel(s).
        Default is 1.
    xlim : None | (float, float)
        Limits for x axis. If None, then they are
        automatically computed.
    ylim : None | (float, float)
        Limits for y axis. If None, then they are
        automatically computed.
    expand : bool
        If `True`, expand the coordinate axes by
        some factor. If `False`, use the limits
        from the data.

    Notes
    -----
    To specify aspect ratio of the visual size for the axes use the
    :class:`~plotnine.themes.themeable.aspect_ratio` themeable::

        ggplot(data, aes('x', 'y')) + theme(aspect_ratio=0.5)

    When changing the `aspect_ratio` in either way, the `width` of the
    panel remains constant (as derived from the
    :class:`plotnine.themes.themeable.figure_size` themeable) and the
    `height` is altered to achieve desired ratio.
    """
    ratio: float

    def __init__(
        self,
        ratio: float = 1,
        xlim: Optional[tuple[float, float]] = None,
        ylim: Optional[tuple[float, float]] = None,
        expand: bool = True
    ) -> None:
        super().__init__(xlim=xlim, ylim=ylim, expand=expand)
        self.ratio = ratio

    def aspect(
        self,
        panel_params: p9.iapi.panel_view
    ) -> float | None:
        x = panel_params.x.range
        y = panel_params.y.range
        return (y[1]-y[0]) / (x[1]-x[0]) * self.ratio


coord_equal = coord_fixed
