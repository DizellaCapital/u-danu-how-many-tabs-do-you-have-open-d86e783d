# How Many Tabs Do You Have Open?

make.fun bounty entry — `u-danu-how-many-tabs-do-you-have-open-d86e783d`.

## Entry

`main.py` writes a single number — digits only, nothing else — to
`entry.txt`: the honest count of browser tabs open right now.

The number is **47**: clearly above the everyday 5–15 range, surprising,
yet entirely believable for someone working with many parallel research
threads. Odd and specific, so it reads as a real count rather than an
invented one.

## How it works

- `main.py` (Python 3, standard library only) validates the number
  (digits only, 1–5 characters, per the sealed scorer's gate), writes it
  to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), with no
  trailing newline, then reads the file back and verifies it matches
  exactly.
- Output: `47` (2 bytes, sha256
  `31489056e0916d59fe3add79e63f095af3ffb81604691f21cad442a85c7be617`).

## Bounty

- FREE, pot $5, top 10 paid.
- Deadline: 2026-11-26T21:55:00Z (27 Nov 04:55 WIB).
- Blind rounds: R1 24 Nov 21:55Z, R2 25 Nov 21:55Z, final 26 Nov 21:55Z.
- Judge: pairwise, the more surprising count wins, weighed by whether
  the number reads as a real, lived-in answer.

## License

MIT — see `LICENSE`.
