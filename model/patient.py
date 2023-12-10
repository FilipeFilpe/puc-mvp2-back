from datetime import datetime
from typing import Union

from model import Base
from sqlalchemy import Column, DateTime, Float, Integer, String


class Patient(Base):
    __tablename__ = 'patients'

    id = Column("pk_patient", Integer, primary_key=True)
    name = Column(String(250))
    pelvic_incidence = Column(Float)
    pelvic_tilt = Column(Float)
    lumbar_lordosis_angle = Column(Float)
    sacral_slope = Column(Float)
    pelvic_radius = Column(Float)
    grade_of_spondylolisthesis = Column(Float)
    result = Column(String(2))
    
    created_at = Column(DateTime, default=datetime.now())

    def __init__(
        self,        

        name:str,
        pelvic_incidence:float,
        pelvic_tilt:float,
        lumbar_lordosis_angle:float,
        sacral_slope:float,
        pelvic_radius:float,
        grade_of_spondylolisthesis:float,
        result:str,
    
        created_at:Union[DateTime, None] = None
    ):
        """
        Create a Patient

        Arguments:
            name: name of the patient
            pelvic_incidence: pelvic incidence
            pelvic_tilt: pelvic tilt
            lumbar_lordosis_angle: lumbar lordosis angle
            sacral_slope: sacral slope
            pelvic_radius: pelvic radius
            grade_of_spondylolisthesis: grade of spondylolisthesis
            result: result of the diagnoses
        """
        self.name = name
        self.pelvic_incidence = pelvic_incidence
        self.pelvic_tilt = pelvic_tilt
        self.lumbar_lordosis_angle = lumbar_lordosis_angle
        self.sacral_slope = sacral_slope
        self.pelvic_radius = pelvic_radius
        self.grade_of_spondylolisthesis = grade_of_spondylolisthesis
        self.result = result

        # se não for informada, será o data exata da inserção no banco
        if created_at:
            self.created_at = created_at
