# Copyright (c) 2025 Intuit Build Challenge

import runpy
import sys


def test_assignment1_main_module_runs_demo(capsys):
    sys.modules.pop("assignment1.__main__", None)
    runpy.run_module("assignment1.__main__", run_name="__main__")
    output = capsys.readouterr().out
    assert "Producer/Consumer transfer complete. Total events: 10" in output
