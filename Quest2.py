import subprocess
import os
import pandas as pd

time_servi = 0.88
servidores = 10
time_obs = 30
requisicoes = [1, 3, 5, 7, 9, 11]

results = []
file_name = "results1.xlsx"

def run(requisicoes):
    
    comand = ["java", "-cp", "bin;lib/*", "ServidorWeb", str(requisicoes), str(time_servi), str(servidores), str(time_obs)]
    
    output = subprocess.run(comand, capture_output=True, text=True)    
    resultados = output.stdout.strip()
    
    results.append([requisicoes, time_servi, servidores, time_obs, resultados])
    
    df = pd.DataFrame(results, columns=["Requisicoes", "TempoServico", "Servidores", "TempoObservacao", "Resultados"])

    if os.path.exists(file_name):
        df_exists = pd.read_excel(file_name)  
        final_df = pd.concat([df_exists, df], ignore_index=True)
    else:
        final_df = df

    final_df.to_excel(file_name, index=False)

    print(f"Resultados salvos!")

for req in requisicoes:
    run(req)
