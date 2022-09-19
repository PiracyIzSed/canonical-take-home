from cli.main import app
def test_version(runner):

    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0

    assert "cli v1.0.0" in result.stdout