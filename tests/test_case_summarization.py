from deepeval.test_case import LLMTestCase
from deepeval import evaluate
import pandas as pd 

from utilities.Read_config import Config_read
from utilities.data_loader import load_data
from utilities.prompts import Prompts
from utilities.metrics import faithfulness_metric, relavance_metric, coherance_metric
from utilities.cleanup import cleanup_pycache
from utilities.report import case_summarization_report
from models.Nowllm import NowLLM


def test_case_summarization():

    # loading system prompt and user prompt for case summarization
    system_prompt = Prompts.CASE_SUMMARIZATION_SYSTEM_PROMPT
    user_prompt = Prompts.CASE_SUMMARIZATION_USER_PROMPT

    # loading the case summarization data
    data = load_data(file_path="data/servicenow_data/latest_case_data.json",
                     system_prompt=system_prompt,
                     user_prompt=user_prompt)
    
    # fetching url and token from properties file
    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]
    model = NowLLM(url, authtoken)

    # variables for storing test cases and model responses
    model_responses = []
    test_cases = []

    # calling nowllm and creating test cases for evaluation
    for i in range(len(data)):
        model_response = model.generate(data[i]["prompt"])
        test_case = LLMTestCase(
            input=data[i]["case_detail"],
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
