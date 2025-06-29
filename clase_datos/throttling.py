from dataclasses import dataclass, field

@dataclass
class Throttling:
    #present events
    undervoltage:bool
    freq_cap:bool
    throttled:bool #current
    soft_temp_limit: bool
    #past events
    undervoltage_occurred: bool
    freq_cap_occurred: bool
    throttled_occurred: bool
    soft_temp_limit_occurred: bool

    @staticmethod
    def parser(cadena:str):
        #TODO a serie of checkers/raisers for the parsing
        #convertimos de cadena a binario
        b= format(int(cadena),'b' ) #es a la inversa
        undervoltage= bool(b[-1])
        freq_cap= bool(b[-2])
        throttled= bool(b[-3])
        soft_temp_limit= bool(b[-4])
        undervoltage_occurred= bool(b[-17])
        freq_cap_occurred= bool(b[-18])
        throttled_occurred= bool(b[-19])
        return Throttling(undervoltage,freq_cap,throttled,soft_temp_limit,undervoltage_occurred,freq_cap_occurred,throttled_occurred, soft_temp_limit_occurred)

