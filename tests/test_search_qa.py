from deepeval.test_case import LLMTestCase
from deepeval import evaluate

import logging

from utilities.data_loader import PromptBuilder
from utilities.Read_config import Config_read
from models.Nowllm import NowLLM
from utilities.cleanup import cleanup_pycache
from utilities.report import search_qa_report
from metrics.search_qa_metrics import search_qa_metric

class Test_Search_QA:
    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]
    model = NowLLM(url, authtoken)
    
    def test_search_qa(self):
        data = PromptBuilder().load_search_qa_data()
        test_cases = []

        for i in range(len(data)):            
            model_response = self.model.generate(data[i]["prompt"])
            test_case = LLMTestCase(
                input=data[i]["query"],
                actual_output=model_response,
                context=[data[i]["context"]],
                expected_output=data[i]["ground_truth"]
            )
            test_cases.append(test_case)

        results = evaluate(
            test_cases=test_cases,
            metrics=[search_qa_metric]
        )
    
        #search_qa_report(results)
        cleanup_pycache()

