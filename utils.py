import json
from typing import List
from datetime import datetime
from models import BenchmarkResult
from config import config


def load_data_from_json() -> List[BenchmarkResult]:
    if config.DEBUG:
        with open("test_database.json", "r") as f:
            data = json.load(f)["benchmarking_results"]
            return [BenchmarkResult(**item) for item in data]
    else:
        raise NotImplementedError("Live database connection not implemented")


def filter_results_by_time(
    results: List[BenchmarkResult], start_time: datetime, end_time: datetime
) -> List[BenchmarkResult]:
    return [result for result in results if start_time <= result.timestamp <= end_time]


def calculate_average(results: List[BenchmarkResult]):
    total_count = len(results)
    if total_count == 0:
        return {}
    avg_token_count = sum(r.token_count for r in results) / total_count
    avg_time_to_first_token = sum(r.time_to_first_token for r in results) / total_count
    avg_time_per_output_token = (
        sum(r.time_per_output_token for r in results) / total_count
    )
    avg_total_generation_time = (
        sum(r.total_generation_time for r in results) / total_count
    )
    return {
        "average_token_count": avg_token_count,
        "average_time_to_first_token": avg_time_to_first_token,
        "average_time_per_output_token": avg_time_per_output_token,
        "average_total_generation_time": avg_total_generation_time,
    }
