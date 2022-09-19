from typer.testing import CliRunner
import pytest

@pytest.fixture
def runner():
    runner = CliRunner()
    yield runner