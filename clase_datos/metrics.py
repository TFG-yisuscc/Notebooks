import datetime
from dataclasses import dataclass, field

from clase_datos.hardware_metrics_container import HardwareMetricsContainer


@dataclass
class Metrics:
    """
    Returns the metrics for a given prompt plus the associated hardware metrics
    """
    testDate: datetime# the date when the test started
    tag: str #useful information like without fan
    source: str #llama .cpp, ollama ...
    promptId: str
    start_timestamp:int  # nanoseconds
    finish_timestamp:int  # nanoseconds
    model:str
    total_duration:int
    prompt_eval_count:int
    prompt_eval_duration:int
    eval_count:int
    eval_duration:int
    load_duration :int
    prompt_answer:str
    associated_hardware_metrics:HardwareMetricsContainer







