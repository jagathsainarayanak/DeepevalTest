from deepeval.test_case import LLMTestCase
from deepeval import evaluate

from utilities.Read_config import Config_read
from utilities.data_loader import PromptBuilder
from metrics.case_summary_metric import faithfulness_metric, relavance_metric, coherance_metric
from utilities.cleanup import cleanup_pycache
from utilities.report import chat_summarization_report
from models.Nowllm import NowLLM

class Test_Chat_Summarization():

    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]
    model = NowLLM(url, authtoken)

    def test_chat_summarization(self):
        data = PromptBuilder().load_chat_summarization_data()
        model_responses = []
        test_cases = []
        for i in range(len(data)):
            model_response = self.model.generate(data[i]["prompt"])
            test_case = LLMTestCase(
                input=data[i]["case_details"],
                actual_output=model_response
            )
            model_responses.append(model_response)
            test_cases.append(test_case)
            results = evaluate(
                test_cases=test_cases,
                metrics=[faithfulness_metric, relavance_metric, coherance_metric]
            )
        chat_summarization_report(results)
        cleanup_pycache()
