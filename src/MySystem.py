import simpy
import random as rd
import pandas as pd
import numpy as np


class MySystem:
    def __init__(self, env, ram, cpu, n_instrucciones):
        self.env = env
        self.ram = simpy.Container(env, init=ram, capacity=ram)
        self.cpu = simpy.Resource(env, capacity=cpu)
        self.n_instrucciones = n_instrucciones

class Proceso:
    def __init__(self, env, system, process_number, n_process, time_per_process):
        """
        Inicializa una instancia de la clase Proceso.

        Args:
            env (simpy.Environment): Entorno de simulación.
            system (System): Sistema del proceso.
            process_number (int): Número del proceso.
            n_process (list): Lista de números de procesos.
            time_per_process (list): Lista de tiempos por proceso.
        """
        self.env = env
        self.sistema = system
        self.ram_to_use = rd.randint(1,10)
        self.instructionCounter = rd.randint(1,10)
        self.start_time = 0
        self.end_time = 0
        self.process_number = process_number
        self.n_process = n_process
        self.time_per_process = time_per_process
        self.action = env.process(self.runProcess())

    def executeInstructions(self, req):
        """
        Ejecuta las instrucciones del proceso.

        Args:
            req (simpy.Resource.Request): Solicitud de recurso.

        Yields:
            simpy.Timeout: Retardo de tiempo.
        """
        while self.instructionCounter > 0:
            yield req
            yield self.env.timeout(1)
            self.instructionCounter -= min(self.instructionCounter, self.sistema.n_instrucciones)

    def runProcess(self):
        """
        Ejecuta el proceso.

        Yields:
            simpy.Timeout: Retardo de tiempo.
        """
        self.start_time = self.env.now
        with self.sistema.cpu.request() as req:
            yield req
            yield self.env.process(self.executeInstructions(req))

            if rd.randint(1,2) == 1:
                yield self.env.timeout(1)
            else: 
                yield self.env.process(self.executeInstructions(req))

            self.sistema.ram.put(self.ram_to_use)
        self.end_time = self.env.now
        self.n_process.append(self.process_number + 1)
        self.time_per_process.append(self.get_process_time())

    def get_process_time(self):
        """
        Obtiene el tiempo de ejecución del proceso.

        Returns:
            float: Tiempo de ejecución del proceso.
        """
        return self.end_time - self.start_time


def generateProcesses(env, n, system, n_process, time_per_process):
    for i in range(n):
        Proceso(env, system, i, n_process, time_per_process)
        yield env.timeout(1)

def main(n_procesos, ram, cpu, n_instrucciones):
    env = simpy.Environment()
    system = MySystem(env, ram, cpu, n_instrucciones)
    n_process = []
    time_per_process = []
    env.process(generateProcesses(env, n_procesos, system, n_process, time_per_process))
    env.run()

    return n_process, time_per_process

rd.seed(34)


def createCSV(RAM, cpu, n_instrucciones, fileTitle):
    cantidad_procesos = [25, 50, 100, 150, 200]
    df = pd.DataFrame()
    for n in cantidad_procesos:
        n_process, time_per_process = main(n, RAM, cpu, n_instrucciones)
        
        padded_time_per_process = time_per_process + [np.nan] * (max(cantidad_procesos) - len(time_per_process))
        
        df[f't con {n} procesos'] = padded_time_per_process


    df.to_csv(f'{fileTitle}.csv', index=False)


createCSV(100, 1, 1, 'procesos 1')   
createCSV(100, 1, 3, 'procesos 3')
createCSV(100, 1, 5, 'procesos 5')
createCSV(100, 1, 6, 'procesos 6')
createCSV(100, 1, 10, 'procesos 10')

createCSV(200, 1, 3, 'procesos con 200 RAM')
createCSV(100, 2, 3, 'procesos doble cpu')