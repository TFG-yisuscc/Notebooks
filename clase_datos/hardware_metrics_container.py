from dataclasses import dataclass, field
from throttling import Throttling

@dataclass
class HardwareMetrics:
    timestamp:int
    prompt_id: int
    temperature:float
    frequency:int
    voltage:float
    throttling: Throttling
    mem_total:int
    mem_used:int
    mam_percent:float
    swap_total:int
    swap_used:int
    swap_percent:float
    cpu_usage:float
    cpu_usage_pid:float

@dataclass
class HardwareMetricsContainer:
    lista:list[HardwareMetrics]
    #TODO a method that given a line and a  method

