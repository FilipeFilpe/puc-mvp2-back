from datetime import datetime

from flask import redirect
from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI, Tag
from model import ModelML, Patient, Session
from schemas import (ErrorSchema, ListPatientsSchema, PatientViewSchema,
                     show_patient, show_patients)
from sqlalchemy import desc

info = Info(title="Diagnóstico da Coluna API", version="1.0.0")
app = OpenAPI(__name__, info=info, static_url_path='/static')
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
patient_tag = Tag(name="Pacientes", description="Adição e visualização de Pacientes com seus diagnósticos")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/patients', tags=[patient_tag], responses={"200": PatientViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_patient(form: PatientViewSchema):
    """Adiciona um novo Paciente com seu diagnóstico à base de dados

    Retorna uma representação dos pacientes.
    """

    try:
        model = ModelML('./models_ML/modelo_classificador.pkl')
        predict = model.predict([
            form.pelvic_incidence,
            form.pelvic_tilt,
            form.lumbar_lordosis_angle,
            form.sacral_slope,
            form.pelvic_radius,
            form.grade_of_spondylolisthesis
        ])

        _patient = Patient(
            name = form.name,
            pelvic_incidence = form.pelvic_incidence,
            pelvic_tilt = form.pelvic_tilt,
            lumbar_lordosis_angle = form.lumbar_lordosis_angle,
            sacral_slope = form.sacral_slope,
            pelvic_radius = form.pelvic_radius,
            grade_of_spondylolisthesis = form.grade_of_spondylolisthesis,
            result = predict[0]
        )

        # criando conexão com a base
        session = Session()
        # adicionando property
        session.add(_patient)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return show_patient(_patient), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo pacinte :/"
        return {"mesage": error_msg}, 500

@app.get('/patients', tags=[patient_tag], responses={"200": ListPatientsSchema, "404": ErrorSchema})
def get_patient():
    """Faz a busca por todos os Pacientes cadastrados

    Retorna uma representação da listagem de pacientes.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    patients = session.query(Patient).order_by(desc(Patient.created_at)).all()

    if not patients:
        # se não há pacientes cadastrados
        return {"patients": []}, 200
    else:
        # retorna a representação de pacientes
        return show_patients(patients), 200
