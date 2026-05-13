from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.scenarios import router as scenarioRouter
import csv
import pandas as pd

app = FastAPI()
plantsDF = pd.read_csv("data/plants.csv")
plants = plantsDF.to_dict('facilityID')



origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8080",
    "https://mecaqc.vercel.app"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scenarioRouter)