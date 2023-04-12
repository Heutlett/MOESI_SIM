import random
import math

def poisson(lam, size):
    """
    Genera un arreglo de tamaño `size` de números aleatorios a partir de una distribución de Poisson con tasa `lam`.
    """
    contador = 0
    arreglo_poisson = []
    for _ in range(size):
        k = 0
        p = 1.0
        while p >= math.exp(-lam):
            k = k + 1
            u = random.uniform(0,1)
            p = p * u
            contador = contador + 1
            
        arreglo_poisson.append(k - 1)
    return arreglo_poisson


def generate_instruction(processor_id):
    instr_op = ['READ', 'WRITE', 'CALC']
    rand_op_list = poisson(10,3)
    rand_max_op_index = rand_op_list.index(max(rand_op_list))
    operation = instr_op[rand_max_op_index]
    
    address = None
    data = None

    if operation != 'CALC':
        instr_addr = ['000', '001', '010', '011', '100', '101', '110', '111']
        rand_addr_list = poisson(10,8)
        rand_max_addr_index = rand_addr_list.index(max(rand_addr_list))
        address = instr_addr[rand_max_addr_index]
        
    if operation == 'READ':
        return f"P{processor_id}: {operation} {address}"
    
    if operation == 'WRITE':
        data = hex(random.randint(0, 65535))[2:].zfill(4)
        return f"P{processor_id}: {operation} {address} ; {data}"
    
    return f"P{processor_id}: {operation}"

def set_next_instruction(processor_id, next_inst_string_var):
    next_inst_string_var.set(generate_instruction(processor_id))
    

def int_to_binary(n):
    binary_str = ""
    if(n == 0):
        return "000"
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2
    if len(binary_str) < 4:
        binary_str = "0" * (3 - len(binary_str)) + binary_str

    return binary_str