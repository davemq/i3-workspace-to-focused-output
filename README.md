# i3-workspace-to-focused-output
Move an i3 workspace to the focused output.

The i3ipc library used by this code uses `asyncio`. I'm not very familiar with
the ins and outs of asyncio so my code may need improvement and I welcome
pointers and tips about it.

To use this code, import it then run

``` python
	asyncio.run(move_to_focused(number))
```

where `number` is the workspace number.
