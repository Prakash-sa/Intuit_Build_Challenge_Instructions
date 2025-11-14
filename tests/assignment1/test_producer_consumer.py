# Copyright (c) 2025 Intuit Build Challenge

import runpy
import sys

from assignment1.producer_consumer import demo_run


def test_demo_run_outputs_expected_lines(capsys):
    demo_run()
    out = capsys.readouterr().out
    assert "Producer: produced event-1" in out
    assert "Consumer: consumed event-1" in out
    assert "Producer/Consumer transfer complete. Total events: 10" in out


def test_module_guard_executes_demo(capsys):
    sys.modules.pop("assignment1.producer_consumer", None)
    runpy.run_module("assignment1.producer_consumer", run_name="__main__")
    output = capsys.readouterr().out
    assert "Producer/Consumer transfer complete. Total events: 10" in output
