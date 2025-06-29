from datetime import  datetime
from dataclasses import dataclass, field

from clase_datos.hardware_metrics_container import HardwareMetricsContainer


@dataclass
class PromptMetrics:
    """
    Returns the metrics for a given prompt plus the associated hardware metrics
    """
    test_date: datetime# the date when the test started

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
    tag: str  = field(default="")
    @staticmethod
    def parser(pm_filepath:str, line:str, asociateted_hm_dict):
        #datos del filepaht
        #procedencia, testdate y model
        pm_filepath = pm_filepath.strip().split("_")
        if "llama_pretrained" in pm_filepath: #TODO  modificar cuandosea posible del lado del cliente
            source= "llama_pretrained"
            test_date = datetime.strptime(pm_filepath[4], "%Y-%m-%d-%H-%M")
        else:
            source= pm_filepath[0]
            test_date = datetime.strptime(pm_filepath[3], "%Y-%m-%d-%H-%M")

        # datos del propio csv
        #prompt_id,start_timestamp,finish_timestamp,model,
        # total_duration,prompt_eval_count,prompt_eval_duration,eval_count,eval_duration,load_duration
        line_aux = line.split(",")
        prompt_id = line_aux[0]
        start_timestamp = int(line_aux[1])
        finish_timestamp = int(line_aux[2])
        model = line_aux[3]
        total_duration = int(line_aux[4])
        prompt_eval_count = int(line_aux[5])
        prompt_eval_duration = int(line_aux[6])
        eval_count = int(line_aux[7])
        eval_duration = int(line_aux[8])
        load_duration = int(line_aux[9])
        # obtenemos  las métricas hardware asociadas
        #TODO Poner un checker
        associated_hardware_metrics = asociateted_hm_dict[prompt_id]
















