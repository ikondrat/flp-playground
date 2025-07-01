"""French deck implementation for Fluent Python examples."""

from __future__ import annotations

import collections
from typing import ClassVar

Card = collections.namedtuple(
    "Card",
    ["rank", "suit"],
)


class FrenchDeck:
    """A deck of French playing cards."""

    ranks: ClassVar[list[str]] = [str(n) for n in range(2, 11)] + list("JQKA")

    suits: ClassVar[list[str]] = ["spades", "diamonds", "clubs", "hearts"]
