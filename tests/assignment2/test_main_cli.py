# Copyright (c) 2025 Intuit Build Challenge

import runpy
import sys

from assignment2.main import main


def test_cli_main_prints_report(capsys):
    main()
    output = capsys.readouterr().out
    assert "Total revenue by region" in output


def test_assignment2_main_module_guard_executes(capsys):
    sys.modules.pop("assignment2.main", None)
    runpy.run_module("assignment2.main", run_name="__main__")
    output = capsys.readouterr().out
    assert "Total revenue by region" in output
