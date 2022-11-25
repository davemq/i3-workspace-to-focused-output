#!/usr/bin/env python3

import asyncio
from i3ipc.aio import Connection

global i3

async def move_to_focused(num):
    global i3

    i3 = await Connection().connect()

    workspaces = await i3.get_workspaces()

    focused = None
    for workspace in workspaces:
        if workspace.focused:
            focused = workspace.output
    if focused is None:
        return
        
    await i3.command(f'workspace {num}; move workspace to output {focused}')

