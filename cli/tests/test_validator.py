import pytest
from cli.users import validator


@pytest.mark.parametrize("email", 
    (
    "name.surname@gmail.com",
    "anonymous123@yahoo.co.uk",
    pytest.param("anonymous123@...uk", marks=pytest.mark.xfail),
    pytest.param("...@domain.us", marks=pytest.mark.xfail),
    )
)
def test_email_validation(email: str):
    assert validator.is_valid_email(email)
