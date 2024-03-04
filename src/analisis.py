import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class Analisis: 
    def __init__(self):
        self.intervalos = [1, 3, 5, 6, 10]
        self.procesos = [25, 50, 100, 150, 200]
        self.dataframes = []
        self.ram200 = []
        self.dobleCPU = []
        for intervalo in self.intervalos:
            df = pd.read_csv(f'procesos {intervalo}.csv')
            self.dataframes.append(df)
            df_RAM200 = pd.read_csv('procesos con 200 RAM.csv')
            
        self.ram200.append(df_RAM200)
        df_dobleCPU = pd.read_csv('procesos doble CPU.csv')
        self.dobleCPU.append(df_dobleCPU)

    def get_mean_std(self, dfs):
        mean_values = []
        std_values = []    
        
        for dataframe in dfs:
            mean_values.append([
                dataframe["t con 25 procesos"].mean(),
                dataframe["t con 50 procesos"].mean(),
                dataframe["t con 100 procesos"].mean(),
                dataframe["t con 150 procesos"].mean(),
                dataframe["t con 200 procesos"].mean()
            ])
            
            std_values.append([
                dataframe["t con 25 procesos"].std(),
                dataframe["t con 50 procesos"].std(),
                dataframe["t con 100 procesos"].std(),
                dataframe["t con 150 procesos"].std(),
                dataframe["t con 200 procesos"].std()
            ])
            
        return mean_values, std_values

    def grafico_barras(self, data, title, xlabel, ylabel):
        if len(data) == 1:
            fig, ax = plt.subplots(figsize=(10, 6))
            bars = ax.bar(self.intervalos, data[0])
            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_xticks(self.intervalos)
            ax.legend()
        else:
            x = np.arange(len(self.intervalos))
            width = 0.15

            fig, ax = plt.subplots(figsize=(10, 6))
            bars = []
            labels = ['25 procesos', '50 procesos', '100 procesos', '150 procesos', '200 procesos']

            for i, label in enumerate(labels):
                bars.append(ax.bar(x + (i - 2) * width, [row[i] for row in data], width, label=label))

            ax.set_title(title)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.set_xticks(x)
            ax.set_xticklabels(self.intervalos)
            ax.legend()

        fig.tight_layout()
        plt.show()


    def stats_intervalos(self):
        mean_intervalos, std_intervalos = self.get_mean_std(self.dataframes)
        self.grafico_barras(mean_intervalos, 'Tiempo promedio de ejecución de los procesos', 'Intervalos', 'Tiempo de ejecución promedio (s)')
        self.grafico_barras(std_intervalos, 'Desviación estándar de ejecución de los procesos', 'Intervalos', 'Desviación estándar (s)')
        data_mean_intervalos = {"Procesos": self.procesos,
                        "1 intervalos": mean_intervalos[0],
                        "2 intervalos": mean_intervalos[1],
                        "3 intervalos": mean_intervalos[2],
                        "4 intervalos": mean_intervalos[3],
                        "5": mean_intervalos[4]
                        }
        
        data_std_intervalos = {"Proceos": self.procesos,
                    "25 procesos": std_intervalos[0],
                    "50 procesos": std_intervalos[1],
                    "100 procesos": std_intervalos[2],
                    "150 procesos": std_intervalos[3],
                    "200 procesos": std_intervalos[4]
                    }
        
        df_mean_intervalos = pd.DataFrame(data_mean_intervalos)
        df_std_intervalos = pd.DataFrame(data_std_intervalos)
        
        df_mean_intervalos.to_excel('Data\Promedios intervalos.xlsx', index=False)
        df_std_intervalos.to_excel('Data\Std intervalos.xlsx', index=False)
        
        print("Promedio de tiempo de ejecución de los procesos")
        print(df_mean_intervalos)
        print("Desviación estándar de tiempo de ejecución de los procesos")
        print(df_std_intervalos)
        
    def stats_RAM200(self):
        mean_ram200, std_ram200 = self.get_mean_std(self.ram200)
        self.grafico_barras(mean_ram200, 'Tiempo promedio de ejecución de los procesos con 200 RAM', 'Intervalos', 'Tiempo de ejecución promedio (s)')
        self.grafico_barras(std_ram200, 'Desviación estándar de ejecución de los procesos con 200 RAM', 'Intervalos', 'Desviación estándar (s)')
        data_RAM = {"Estadistica": ["Promedio", "Desviación estándar"],
                            "25 procesos": [mean_ram200[0][0], std_ram200[0][0]],
                            "50 procesos": [mean_ram200[0][1], std_ram200[0][1]],
                            "100 procesos": [mean_ram200[0][2], std_ram200[0][2]],
                            "150 procesos": [mean_ram200[0][3], std_ram200[0][3]],
                            "200 procesos": [mean_ram200[0][4], std_ram200[0][4]]
                            }
        
        df_data_RAM = pd.DataFrame(data_RAM)
        print("\nPromedio de tiempo de ejecución de los procesos con 200 RAM")
        print(df_data_RAM)
        df_data_RAM.to_excel('Data\RAM200.xlsx', index=False)
 
    def  stats_dobleCPU(self):
        mean_dobleCPU, std_dobleCPU = self.get_mean_std(self.dobleCPU)
        self.grafico_barras(mean_dobleCPU, 'Tiempo promedio de ejecución de los procesos con doble CPU', 'Intervalos', 'Tiempo de ejecución promedio (s)')
        self.grafico_barras(std_dobleCPU, 'Desviación estándar de ejecución de los procesos con doble CPU', 'Intervalos', 'Desviación estándar (s)')
        
        data_dobleCPU = {"Estadistica": ["Promedio", "Desviación estándar"],
                                "25 procesos": [mean_dobleCPU[0][0], std_dobleCPU[0][0]],
                                "50 procesos": [mean_dobleCPU[0][1], std_dobleCPU[0][1]],
                                "100 procesos": [mean_dobleCPU[0][2], std_dobleCPU[0][2]],
                                "150 procesos": [mean_dobleCPU[0][3], std_dobleCPU[0][3]],
                                "200 procesos": [mean_dobleCPU[0][4], std_dobleCPU[0][4]]
                                }
        
        df_data_dobleCPU = pd.DataFrame(data_dobleCPU)
        df_data_dobleCPU.to_excel('Data\DobleCPU.xlsx', index=False)
        print("\nPromedio de tiempo de ejecución de los procesos con doble CPU")
        print(df_data_dobleCPU)
        




