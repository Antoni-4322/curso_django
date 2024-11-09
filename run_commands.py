#!/usr/bin/env python3
import psutil
import sys




def get_memory_in_percentage():
    # Coleta o uso de memória em percentual
    used_mem = psutil.virtual_memory().percent
    return float(used_mem)

def get_cpu_in_percentage():
    used_cpu = psutil.cpu_percent(interval=1)
    return float(used_cpu)

def get_disk_in_percentage():
    # Obter todas as partições do disco
    particoes = psutil.disk_partitions()
    
    maior_consumo = 0
    maior_particao = ""

    for particao in particoes:
        try:
            # Obter informações de uso do disco
            uso = psutil.disk_usage(particao.mountpoint)
            percentual = uso.percent

            # Verificar se é a partição com maior consumo
            if percentual > maior_consumo:
                maior_consumo = percentual
                maior_particao = particao.mountpoint
        except PermissionError:
            # Ignorar partições que não podem ser acessadas
            continue

    return maior_consumo


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erro: Nenhuma função especificada.")
        sys.exit(1)
    
    function = sys.argv[1]

    if function == "get_used_memory_in_percentage":
        print(get_memory_in_percentage())
    elif function == "get_used_cpu_in_percentage":
        print(get_cpu_in_percentage())
    elif function == "get_used_disk_in_percentage":
        print(get_disk_in_percentage())
    else:
        print("Erro: Função desconhecida.")