from deepeval.benchmarks import GSM8K
from models.Nowllm import NowLLM
from utilities.Read_config import Config_read

class GSM8k_Data:

    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]

    def run_gsm(self):
        model = NowLLM(url=self.url, authtoken=self.authtoken)
        benchmark = GSM8K(
            n_problems=10,
            n_shots=3,
            enable_cot=True
        )

        benchmark.evaluate(model=model)
        print(benchmark.overall_score)