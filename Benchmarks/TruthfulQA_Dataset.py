from deepeval.benchmarks import TruthfulQA
from deepeval.benchmarks.tasks import TruthfulQATask
from deepeval.benchmarks.modes import TruthfulQAMode
from models.Nowllm import NowLLM
from utilities.Read_config import Config_read

class TruthfulQA_data:

    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]

    def run_TruthfulQA(self):
        model = NowLLM(url=self.url, authtoken=self.authtoken)
        benchmark = TruthfulQA(
            tasks=[TruthfulQATask.ADVERTISING, TruthfulQATask.FICTION],
            mode=TruthfulQAMode.MC2)
        benchmark.evaluate(model=model)
        print(benchmark.overall_score)


