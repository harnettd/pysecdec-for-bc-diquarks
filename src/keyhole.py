"""Define a keyhole domain."""
import numpy as np

from typing import Union


def keyhole(
        centre: Union[int, float], 
        radius: Union[int, float], 
        max_re_qq: Union[int, float],
        num_pts_arc: int, 
        num_pts_line: int,
        delta: float = 1e-6) -> np.array:
    """
    Return a keyhole domain.

    :param centre: The centre of the arc portion of the keyhole
    :type: Union[int, float]

    :param radius: The radius of the arc portion of the keyhole
    :type: Union[int, float]

    :param max_re_qq: The max value of Re(qq)
    :type: Union[int, float]

    :param num_pts_arc: The number of points on the arc
    :type: int

    :param num_pts_line: The number of points on the line
    :type int:

    :param delta: The value of Im(qq)
    :type delta: float

    :return: A keyhole domain
    :rtype: Array
    """
    assert isinstance(centre, float) or isinstance(centre, int)
    assert radius > 0 
    assert max_re_qq > centre + radius
    assert isinstance(num_pts_line, int)
    assert isinstance(num_pts_arc, int)
    assert delta > 0 
    assert delta < radius

    # Determine the coordinates at which the line portion of the 
    # keyhole intersects with the arc portion of the keyhole.
    min_re_qq = centre + np.sqrt(radius ** 2 + delta ** 2)
    max_theta = np.arctan(delta / min_re_qq)

    thetas = np.linspace(np.pi, max_theta, num_pts_arc,
                         dtype=np.complex64)
    
    # There are problems with roundoff error when theta == np.pi.
    # It's better to handle this value as a special case.
    arc = centre + radius * np.exp(thetas[1:] * 1j)
    arc = np.insert(arc, 0, centre - radius)

    qq_line = np.linspace(min_re_qq, max_re_qq, num_pts_line, 
                          dtype=np.complex64) + delta * 1j

    # We drop the final element of arc to avoid double counting it.
    return np.concatenate((arc[:-1], qq_line))


if __name__ == '__main__':
    print(__doc__)
 