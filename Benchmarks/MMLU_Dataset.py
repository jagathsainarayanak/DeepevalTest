from models.Nowllm import NowLLM
from deepeval.benchmarks import MMLU
from deepeval.benchmarks.tasks import MMLUTask
from utilities.Read_config import Config_read

class MMLU_Data:

    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]

    def run_mmlu(self):
        model = NowLLM(url=self.url, authtoken=self.authtoken)
        benchmark = MMLU(
                tasks=[MMLUTask.HIGH_SCHOOL_COMPUTER_SCIENCE, MMLUTask.ASTRONOMY],
                n_shots=3
            )
        benchmark.evaluate(model=model)
        print(benchmark.overall_score)