import pytest
from pypro.base import models


@pytest.mark.parametrize('email, password',
                        [
                        (None, 'abc'),
                        ('', 'abc')]
                        )
def test_user_creation_no_email(email, password):
    fake_user = models.UserManager()
    with pytest.raises(ValueError):
        assert fake_user.create_user(email=email, password=password)


@pytest.mark.parametrize('email, norm_email',
                         [
                          ('test_user@amaro.com', 'test_user@amaro.com'),
                          ('test_user@AMARO.COM', 'test_user@amaro.com'),
                          (' TEST_USER@AMARO.COM ', 'TEST_USER@amaro.com'),
                          ('test_user@AMaRO.COM  ', 'test_user@amaro.com')]
                         )
def test_email_normalize(email, norm_email):
    fake_user = models.UserManager()
    assert fake_user.normalize_email(email=email) == norm_email
