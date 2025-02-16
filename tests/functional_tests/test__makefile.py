import subprocess
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project():
    print("Setup")
    yield 1
    print("Teardown")


def test__linting_passes(project_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_passes(project_dir: Path):
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)


"""
Setup:
1. generate a project using cookiecutter
2. create a virtual environment and install project dependencies

Tests:
3. run tests
4. run linting

Cleanup/Teardown
5. remove virtual environment
6. remove generated project
"""
