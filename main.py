from fastapi import FastAPI, HTTPException
from typing import Dict
from datetime import datetime
from utils import load_data_from_json, filter_results_by_time, calculate_average
from config import config

app = FastAPI(title="SuperBenchmark API")


@app.get("/results/average", response_model=Dict[str, float])
async def get_average_results():
    if not config.DEBUG:
        raise HTTPException(status_code=403, detail="Feature not ready for live yet")
    data = load_data_from_json()
    return calculate_average(data)


@app.get("/results/average/{start_time}/{end_time}", response_model=Dict[str, float])
async def get_average_results_in_time_window(start_time: str, end_time: str):
    if not config.DEBUG:
        raise HTTPException(status_code=403, detail="Feature not ready for live yet")
    data = load_data_from_json()
    try:
        start_dt = datetime.fromisoformat(start_time)
        end_dt = datetime.fromisoformat(end_time)
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Invalid datetime format. Use ISO format."
        )
    filtered_data = filter_results_by_time(data, start_dt, end_dt)
    return calculate_average(filtered_data)
