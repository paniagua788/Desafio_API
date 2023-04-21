from app import app, validar_fecha
import pytest
from datetime import datetime, timedelta

def test_obtener_UF():
    with app.test_client() as client:
        response = client.get('/uf?fecha=2022-01-01')
        assert response.status_code == 200

def test_validar_fecha():
    # fecha válida
    fecha = datetime(2013, 1, 1)
    validar_fecha(fecha)

    #fecha inferior a 2013
    with pytest.raises(ValueError) as excinfo:
        fecha = datetime.strptime('2012-12-31', '%Y-%m-%d')
        validar_fecha(fecha)
    assert "valores desde 2013 en adelante" in str(excinfo.value)

    #fecha superior a 2023
    with pytest.raises(ValueError) as excinfo:
        fecha = datetime.strptime('2024-01-01' , '%Y-%m-%d')
        validar_fecha(fecha)
    assert "valores de años posteriores al actual" in str(excinfo.value)