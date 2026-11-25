#!/usr/bin/env python3
"""Write the one-line review for the make.fun bounty
'One Star for Monday'.

The review: Monday as a restaurant that serves Friday's order cold
on Monday and still charges for the weekend. A real diner's complaint
- server, dish, bill - and the joke only works about Monday.
Gate: 1-180 characters, at most 25 words; this entry is 19 words
and 114 characters, short enough to retype without trimming.
"""

import os

ENTRY = "Ordered Friday, served Monday, cold. The waiter blamed the kitchen and still charged me for the weekend. One star."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
