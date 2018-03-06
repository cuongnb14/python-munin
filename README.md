
# Description

This library provides helper classes for writing plugins for the server
monitoring tool Munin. It also comes with some prebuilt plugins for
various services including PostgreSQL, Memcached, and Nginx.

# Install

pip3 install git+https://github.com/cuongnb14/python-munin.git

# Example Usage

```
"""
Cpu Load plugin for Munin.
"""

from munin import MuninPlugin
import os


class LoadPlugin(MuninPlugin):
    title = "Cpu load"
    args = "--base 1000 -l 0"
    vlabel = "load"
    scale = False
    category = "system"
    warning = os.environ.get('load_warn', 3)  
    critical = os.environ.get('load_crit', 4)  
    fields = (
        ('load', dict(
            label="Load",
            type="GAUGE",
            draw="LINE2",
            min="0",
            info="Cpu load averages per one minutes",
            warning=str(warning),
            critical=str(critical)
        )),
    )

    def execute(self):
        return {"load": os.popen("cut -d' ' -f2  /proc/loadavg").read()}


if __name__ == "__main__":
    LoadPlugin().run()

```