# pylint: disable=C0114  # noqa: D100
class DatasetsDoNotMatch(Exception):
    """The two datasets have the wrong length or do not match in x."""


class PointsDoNotMatchInX(Exception):
    """Two points do not have the same x coordinate."""
