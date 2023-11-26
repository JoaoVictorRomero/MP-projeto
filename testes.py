# test_menu_de_busca.py

import pytest
from menu_de_busca import criar_menu

def test_criar_menu_user_input(monkeypatch):
    # Mock user input for testing purposes
    user_input = "Test input"
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    # Call the function to test and capture the returned value
    result = criar_menu()

    # Check if the function returns the expected user input
    assert result == user_input

# Add more test cases as needed