import os

from locust import HttpUser, TaskSet, task, between

class TesteDePerformance(TaskSet):

    @task
    def testar_soma(self):
        self.client.get("/soma?a=10&b=20")

class UsuarioSimulado(HttpUser):
    tasks = [TesteDePerformance]
    wait_time = between(1, 2)

if __name__ == "__main__":
    os.system("locust -f locustfile.py")