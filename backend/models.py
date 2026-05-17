from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key = True, index = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    plant_name = Column(String, nullable = True)
    state = Column(String)
    capacity = Column(Integer)
    annualGeneration = Column(Float)
    heatInput = Column(Float)
    SO2Rate = Column(Float)
    operatingHours = Column(Float)
    baselineSO2 = Column(Float)
    baselineNOx = Column(Float)
    baselinePM25 = Column(Float)
    baselineVOC = Column(Float)
    baselineCO2 = Column(Float)

    
    bau_totalBenefit = Column(Float)
    bau_totalAnnualCost = Column(Float)
    bau_netBenefit = Column(Float)

    gt_totalBenefit = Column(Float)
    gt_totalAnnualCost = Column(Float)
    gt_netBenefit = Column(Float)

    rt_totalBenefit = Column(Float)
    rt_totalAnnualCost = Column(Float)
    rt_netBenefit = Column(Float)

    ac_totalBenefit = Column(Float)
    ac_totalAnnualCost = Column(Float)
    ac_netBenefit = Column(Float)
