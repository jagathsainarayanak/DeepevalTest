from deepeval.test_case import LLMTestCase
from deepeval import evaluate
from utilities.Read_config import Config_read
from utilities.data_loader import PromptBuilder
from metrics.case_summary_metric import faithfulness_metric, relavance_metric, coherance_metric
from utilities.cleanup import cleanup_pycache
from utilities.report import case_summarization_report
from models.Nowllm import NowLLM

class test_case_summarization:

    case_data = PromptBuilder()
    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]
    model = NowLLM(url, authtoken)

    def test_case_summarization(self):
        model_responses = []
        test_cases = []
        # loading the case summarization data
        data = self.case_data.load_case_summarization_data()
        for i in range(len(data)):
            model_response = self.model.generate(data[i]["prompt"])
            test_case = LLMTestCase(
                input=data[i]["case_details"],
                actual_output=model_response
            )
            model_responses.append(model_response)
            test_cases.append(test_case)

        # evaluating the created test cases
        results = evaluate(
            test_cases=test_cases,
            metrics=[faithfulness_metric, relavance_metric, coherance_metric]
        )

        # generating excel report for showing scores and pass or fail status
        case_summarization_report(results)

        # deleting all the pycache folders that are generated
        cleanup_pycache()
