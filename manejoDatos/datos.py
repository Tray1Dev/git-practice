def analizar_intento(linea_log):
    # Busca dónde empieza "IP "
    indice_ip = linea_log.find("IP ")
    
    # Busca la coma después de la IP
    indice_coma = linea_log.find(",", indice_ip + 4)
    
    # Extrae la IP (desde después de "IP " hasta la coma)
    ip = linea_log[indice_ip,indice_coma]
    
    # Busca dónde empieza "ESTADO "
    indice_estado = linea_log.find("ESTADO ")
    
    # Extrae el estado (desde después de "ESTADO " hasta el final)
    estado = linea_log[indice_estado + 7 :]
    
    if ip.startswith("192.168." or "10.0.0."):
       return True
    elif estado == "fallido":
        return True
    else:
        return False
    
    # Retorna True si:
    # - IP empieza con "192.168." O "10.0.0."
    # - Y estado es "FALLIDO"
    # (usa .startswith() para la IP y comparación directa para el estado)
    #return # COMPLETA TÚ