from deepeval.benchmarks import HellaSwag
from deepeval.benchmarks.tasks import HellaSwagTask
from models.Nowllm import NowLLM
from utilities.Read_config import Config_read


class Hellaswag_data:

    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]

    def run_Hellaswag(self):
        model = NowLLM(url=self.url, authtoken=self.authtoken)
        benchmark = HellaSwag(
            tasks=[HellaSwagTask.TRIMMING_BRANCHES_OR_HEDGES, HellaSwagTask.BATON_TWIRLING],
            n_shots=5
        )
        benchmark.evaluate(model=model)
        print(benchmark.overall_score)