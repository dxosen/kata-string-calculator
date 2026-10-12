from calculadora import somar

def test_texto_vazio_devolve_zero():
    assert somar("") == 0

def test_passou_numero_devolve_numero():
    assert somar("1") == 1

def test_dois_numeros_separados_por_virgula_devolve_soma():
    assert somar("1,2") == 3