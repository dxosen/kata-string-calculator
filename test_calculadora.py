from calculadora import somar

def test_texto_vazio_devolve_zero():
    assert somar("") == 0

def test_passou_numero_devolve_numero():
    assert somar("1") == 1

def test_dois_numeros_separados_por_virgula_devolve_soma():
    assert somar("1,2") == 3

def test_aceita_qualquer_quantidade_de_numeros_separados_por_virgula():
    assert somar("1,2,3,4,5") == 15

def test_mudanca_de_linha_entre_numeros_devolve_soma():
    assert somar("1\n2,3") == 6