# diagnosticos.py


def enfermedad1(Presion_sistolica, Presion_diastolica, Pulso, Temperatura):
    categoria = 'SIN CATEGORIA'

    if Presion_sistolica is None:
        Presion_sistolica = 100
    if Presion_diastolica is None:
        Presion_diastolica = 70
    if Pulso is None:
        Pulso = 80
    if Temperatura is None:
        Temperatura = 37

    Presion_sistolica = float(Presion_sistolica)
    Presion_diastolica = float(Presion_diastolica)
    Pulso = float(Pulso)
    Temperatura = float(Temperatura)

    if ((Presion_sistolica < 120 and Presion_diastolica < 80 and Pulso < 100) and (Temperatura < 37.3 or Temperatura <= 36.5)):
        categoria = 'NO ENFERMO'
    if (Presion_sistolica < 120 and Presion_diastolica < 80 and Pulso < 100 and Temperatura >= 37.3):
        categoria = 'ENFERMEDAD LEVE'
    elif (Presion_sistolica < 120 and Presion_diastolica < 80 and Pulso >= 100):
        categoria = 'ENFERMEDAD AGUDA'
    elif ((Presion_sistolica >= 120 and Presion_sistolica < 130)  or 
          (Presion_diastolica >= 80 and Presion_diastolica < 83)):
        categoria = 'ENFERMEDAD CRÓNICA'
    elif (Presion_sistolica >= 130 or Presion_diastolica >= 83):
        categoria = 'ENFERMEDAD TERMINAL'
    return categoria

