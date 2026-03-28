def greet_names(names: list[str]) -> list[str]:
    """
    Retorna uma lista de saudações para cada nome.

    Args:
        names (list[str]): lista de nomes

    Returns:
        list[str]: lista com mensagens "Hello, <name>!"
    """
    greetings = []
    for i in names:
        greetings.append(f"Hello, {i}!")
    return greetings
