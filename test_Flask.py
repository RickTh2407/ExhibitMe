import pytest
from Flask import *

test001 = [
("Admin", "Admin", redirect('hiddenAdmin.html'))
("ftrgvyhbjn","5r6tg7yh", flash('Incorrecte login gegevens, probeer het opnieuw'))
("admin@gmail.com","Admin", redirect('Guest.html'))
]

@pytest.mark.parametrize("loginEmail, loginPassword, result", test001)
def test_Login(loginEmail, loginPassword, result):
    assert Login(loginEmail, loginPassword) == result