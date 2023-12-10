from typing import List

from model.patient import Patient
from pydantic import BaseModel


class PatientViewSchema(BaseModel):
    """ Define como um novo paciente é apresentado
    """
    name:str = "Filipe Sousa"
    pelvic_incidence:float = 68.83
    pelvic_tilt:float = 22.22
    lumbar_lordosis_angle:float = 50.09
    sacral_slope:float = 46.61
    pelvic_radius:float = 105.99
    grade_of_spondylolisthesis:float = -3.53

class PatientViewWithIdSchema(PatientViewSchema):
    """ Define um novo paciente com id
    """
    id: int = 1
    result:str = 'AB'
    
class PatientSearchSchema(PatientViewSchema):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no id do paciente.
    """
    id: int = 1

class ListPatientsSchema(BaseModel):
    """ Define como uma listagem de pacientes será retornada.
    """
    patients:List[PatientViewWithIdSchema]
    

def show_patients(patients: List[Patient]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PatientViewWithIdSchema.
    """
    result = []
    for patient in patients:
        result.append({
            "id": patient.id,
            "name": patient.name,
            "pelvic_incidence": patient.pelvic_incidence,
            "pelvic_tilt": patient.pelvic_tilt,
            "lumbar_lordosis_angle": patient.lumbar_lordosis_angle,
            "sacral_slope": patient.sacral_slope,
            "pelvic_radius": patient.pelvic_radius,
            "grade_of_spondylolisthesis": patient.grade_of_spondylolisthesis,
            "result": patient.result,
            "created_at": patient.created_at
        })

    return {"patients": result}

def show_patient(patient: Patient):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PatientViewWithIdSchema.
    """
    return {
            "id": patient.id,
            "name": patient.name,
            "pelvic_incidence": patient.pelvic_incidence,
            "pelvic_tilt": patient.pelvic_tilt,
            "lumbar_lordosis_angle": patient.lumbar_lordosis_angle,
            "sacral_slope": patient.sacral_slope,
            "pelvic_radius": patient.pelvic_radius,
            "grade_of_spondylolisthesis": patient.grade_of_spondylolisthesis,
            "result": patient.result
        }
        

class PatientDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    title: str
