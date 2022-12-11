from screeninfo import get_monitors

for m in get_monitors():
    monitor_width = m.width // 2
    monitor_height = m.height // 2

