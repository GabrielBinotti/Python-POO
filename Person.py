class Pessoa:
    def __init__(self, nome: str, idade: int, peso_kg: float):
        self._nome = nome
        self._idade = idade
        self._peso_kg = peso_kg

    @property
    def nome(self) -> str:
        """Getter para o nome."""
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        """Setter para o nome."""
        self._nome = novo_nome

    @property
    def idade(self) -> int:
        """Getter para a idade."""
        return self._idade

    @idade.setter
    def idade(self, nova_idade: int) -> None:
        """Setter para a idade."""
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("A idade não pode ser negativa.")

    @property
    def peso_kg(self) -> float:
        """Getter para o peso em quilogramas."""
        return self._peso_kg

    @peso_kg.setter
    def peso_kg(self, novo_peso: float) -> None:
        """Setter para o peso em quilogramas."""
        if novo_peso > 0:
            self._peso_kg = novo_peso
        else:
            raise ValueError("O peso deve ser maior que zero.")

    def __str__(self) -> str:
        """Retorna uma representação em string da Pessoa."""
        return f"Pessoa(nome={self.nome}, idade={self.idade}, peso_kg={self.peso_kg})"
