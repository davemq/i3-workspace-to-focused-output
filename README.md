# i3-workspace-to-focused-output
Move an i3 workspace to the focused output.

Most of the documentation I found about i3ipc uses `asyncio`, so I implemented
this code using `asyncio`. It turns out that you can use i3ipc without
`asyncio`, but at this point the code is written. I'm not very familiar with
the ins and outs of asyncio so my code may need improvement and I welcome
pointers and tips about it.

To use this code, import it then run

``` python
	asyncio.run(move_to_focused(number))
```

where `number` is the workspace number.
