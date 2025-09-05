"""
for sniffer auto testing
"""

from sniffer.api import *  # import the really small API
import os, termstyle

# you can customize the pass/fail colors like this
pass_fg_color = termstyle.green
pass_bg_color = termstyle.bg_default
fail_fg_color = termstyle.red
fail_bg_color = termstyle.bg_default

# All lists in this variable will be under surveillance for changes.
watch_paths = ['.', 'tests/']


@file_validator
def py_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')


@runnable
def execute_nose(*args):
    import nose
    print(termstyle.bg_red("\n" + "=" * 70))
    test_result = nose.run(argv=list(args))
    print(termstyle.bg_red("\n" + "=" * 70))
    return test_result


@runnable
def execute_ruff(*args):
    import subprocess
    ruff_result = subprocess.run(['ruff', 'check', '.'], capture_output=True, text=True)

    if ruff_result.returncode != 0:
        print(termstyle.bg_blue("\n" + "=" * 70))
        print(termstyle.bg_yellow("Ruff check: "))
        print(termstyle.green(ruff_result.stdout))
        print(termstyle.bg_blue("\n" + "=" * 70))
        print("\n")

    return ruff_result.returncode == 0
