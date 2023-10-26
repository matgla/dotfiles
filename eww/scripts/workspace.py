#!/bin/python3

import subprocess
import os
import socket

icon_empty=""
icon_occupied=""

def get_occupied():
    resp = subprocess.run("hyprctl workspaces", shell=True, stdout=subprocess.PIPE)
    occupied = [] 
    for line in resp.stdout.decode("utf-8").splitlines():
        if "workspace ID" in line: 
            occupied.append(int(line.split()[2]))
    return occupied


def update_workspaces(active):
    occupied = get_occupied()
    active_workspace=0
    widget = "(box :spacing 10 :space-evenly true "
    for i in range(0, 10):
        if i == active - 1 or (i == 9 and active == 0):
            button_active = "workspace_active"
            active_workspace = i + 1 
        else:
            button_active = "workspace_inactive"
    
        icon = icon_empty 
        if i + 1 in occupied:
            icon = icon_occupied
        button = '(button :class "{button_active}" :onclick "hyprctl dispatch workspace {workspace}" "{icon}")'.format(
            button_active=button_active, icon=icon, workspace = i + 1
        )
        widget += " " + button

    widget += ")"
    subprocess.run(f"echo '{widget}'", shell=True)
    return active_workspace


hyprland_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
hyprland_server = f'/tmp/hypr/{os.environ["HYPRLAND_INSTANCE_SIGNATURE"]}/.socket2.sock'
hyprland_socket.connect(hyprland_server)

resp = subprocess.run("hyprctl activeworkspace", shell=True, stdout=subprocess.PIPE)
workspace = int(resp.stdout.decode("utf-8").split()[2])
active_workspace = update_workspaces(workspace)
while True:
    event = hyprland_socket.recv(4096).decode("utf-8")
    for item in event.split("\n"):
        if "workspace>>" == item[0:11]:
            active_workspace = update_workspaces(int(item[-1]))
        if "destroyworkspace" in item: 
            update_workspaces(active_workspace)     

