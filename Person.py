class Person:
    def __init__(self, name: str, age: int):
        self._name  = name
        self._age   = age

    @property
    def name(self) -> str:
        """Getter para o nome."""
        return self._name

    @name.setter
    def name(self, novo_nome: str) -> None:
        """Setter para o nome."""
        self._name = novo_nome

    @property
    def age(self) -> int:
        """Getter para a idade."""
        return self._age

    @age.setter
    def age(self, nova_idade: int) -> None:
        """Setter para a idade."""
        if nova_idade >= 0:
            self._age = nova_idade
        else:
            raise ValueError("A idade não pode ser negativa.")

    def __str__(self) -> str:
        """Retorna uma representação em string da Pessoa."""
        return f"Pessoa(nome={self._name}, idade={self._age})"


person = Person('Gabriel', 31)
