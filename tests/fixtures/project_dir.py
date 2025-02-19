import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Generator[Path, None, None]:
    test_session_id = generate_test_session_id()
    template_values = {
        "repo_name": f"test_repo-{test_session_id}",
        "package_import_name": f"test_package_{test_session_id}",
    }
    generated_repo_dir: Path = generate_project(
        template_values=template_values, test_session_id=test_session_id
    )
    try:
        initialize_git_repo(repo_dir=generated_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
        yield generated_repo_dir
    finally:
        # shutil.rmtree(path=generated_repo_dir) #noqa:ERA001 # pylint: disable=W2301, W0611
        ...  # pylint: disable=W2301, W0611


def generate_test_session_id() -> str:
    test_session_id = str(uuid4())[:6]
    return test_session_id
