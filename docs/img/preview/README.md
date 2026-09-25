# Preview GIF

Terminal preview shown in the README and docs index. Rendered with
[vhs](https://github.com/charmbracelet/vhs) 0.12.1 (0.12.0 is broken and
writes no output).

`lcpy-preview.gif` shows the practice loop in five beats:

1. `lcpy list` previews the catalog, then `lcpy gen -n 1` generates the
   environment: README, typed stub, parametrized tests, helpers,
   playground notebook
2. `pytest` fails first: 15 cases, zero code
3. the stub gets filled in
4. `pytest` goes green
5. `TreeNode` prints as an ASCII tree in a plain REPL, no Jupyter

## Still PNG

`lcpy-preview.png` is a separate single-beat render (`list.tape` in this
directory, same theme as the GIF): `lcpy list --tag blind-75 --difficulty
Easy` in a 1560x900 terminal, cropped to the table. It is not part of the
tape that renders the GIF, so re-render it separately after changes.

## Rendering

The tape needs a venv with `pytest` and `leetcode-py-sdk` activated before
it starts. From the directory containing this README:

```bash
./setup.sh
```

`setup.sh` builds a fresh demo dir (venv included) and renders the GIF. To
re-render into an existing demo dir, just `vhs lcpy.tape` there: the tape's
hidden warm-up block regenerates `two_sum/` with `--force`, so no manual
reset is needed.

## Tape notes (vhs 0.12.1)

- The tape opens with a hidden warm-up block: `lcpy gen`, `pytest`, and a
  `TreeNode` import all run invisibly with generous `Sleep` durations.
  `Hide` pauses frame capture, so none of that time lands in the GIF.
  This matters because a cold `lcpy` start takes 10-14s; a visible cold
  command outruns any reasonable `Sleep` and the next commands get typed
  while the shell is still busy, cascading text into itself. vhs also
  slows command output roughly 3x versus a direct run, so visible dwell
  times are budgeted from in-render runtimes, not direct ones.
- The venv must exist before rendering. Building it inside the tape would
  reintroduce the cold-start race (uv can stall on the network for tens of
  seconds).
- zsh has no interactive comments, so captions use `echo 'text'`.
- Beat 1 pipes `lcpy list` through `head` for a quick catalog flash. A pipe
  strips colors, so the hidden warm-up exports `FORCE_COLOR=1`; the visible
  command stays clean.
- The tape parser does not support `\"` escapes; use single quotes inside
  double-quoted `Type` strings.
