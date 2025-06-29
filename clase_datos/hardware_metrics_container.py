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
    mem_percent:float
    swap_total:int
    swap_used:int
    swap_percent:float
    cpu_usage:float
    cpu_usage_pid:float
    fan_speed:int

    @staticmethod
    def parser(string:str) -> 'HardwareMetrics':
        string = string.strip().split(",")

        #timestamp,prompt_id,temperature,frequency,voltage,throttling,
        # mem_total,mem_used,mem_percent,mem_pid,cpu_usage_pid,swap_total,
        # swap_used,swap_percent,cpu_usage,fan_speed
        timestamp = int(string[0])
        prompt_id = int(string[1])
        temperature = float(string[2])
        frequency = int(string[3])
        voltage = float(string[4])
        throttling = Throttling.parser(string[5])
        mem_total = int(string[6])
        mem_used = int(string[7])
        mem_percent = float(string[8])
        mem_percent_pid = float(string[9])
        cpu_usage_pid = float(string[10])
        swap_total = int(string[11])
        swap_used = int(string[12])
        swap_percent = float(string[13])
        cpu_usage = float(string[14])
        fan_speed = int(string[15])
        res = HardwareMetrics(timestamp,prompt_id,temperature,frequency,voltage,throttling,mem_total,mem_used,
                              mem_percent,mem_percent_pid, cpu_usage_pid,swap_total,swap_used,swap_percent,
                              cpu_usage,fan_speed)
        return res


@dataclass
class HardwareMetricsContainer:
    lista:list[HardwareMetrics]

    @staticmethod
    def parser(associated_prompt_metric_path:str, prompt_id:int) -> 'HardwareMetricsContainer':
        #ambos ficheros tienen la misma diferencia
        hm_filepath=associated_prompt_metric_path.replace("prompt_metrics","hardware_metrics")
        res= list()
        #abrimos el fichero
        with open(hm_filepath,"r") as f:
            for line in f:
                hm = HardwareMetrics.parser(line)
                if hm.prompt_id == prompt_id:
                    res.append(hm)
        res.sort(key=lambda hm: hm.timestamp)
        return HardwareMetricsContainer(res)





