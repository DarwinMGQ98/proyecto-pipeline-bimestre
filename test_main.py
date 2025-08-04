from main import saludar

def test_saludar():
    assert saludar("Vinicio") == "Hola, Vinicio!"
    assert saludar("Mundo") == "Hola, Mundo!"

if __name__ == "__main__":
    test_saludar()
    print("Todos los tests pasaron")
