from deepeval.test_case import LLMTestCase
from deepeval import evaluate

import logging
from utilities.prompts import Prompts
from utilities.data_loader import load_search_qa_data
from utilities.Read_config import Config_read
from models.Nowllm import NowLLM
from utilities.cleanup import cleanup_pycache
from utilities.report import search_qa_report
from utilities.metrics import search_qa_metric

def test_search_qa():
    logger = logging.getLogger(__name__)
    logger.info('Loading system prompt and user prompt')
    system_prompt = Prompts.SEARCH_QA_SYSTEM_PROMPT
    user_prompt = Prompts.SEARCH_QA_USER_PROMPT
    logger.info('Started loading search qa dataset')
    data = load_search_qa_data(file_path='data/servicenow_data/search_qa.json',
                               system_prompt=system_prompt,
                               user_prompt=user_prompt)
    logger.info('Completed loading chat summarization data')
    url = Config_read.read_conf()["Nowllm"]["url"]
    authtoken = Config_read.read_conf()["Nowllm"]["authtoken"]
    model = NowLLM(url, authtoken)
    test_cases = []
    logger.info('Started making api calls to nowllm')
    for i in range(len(data)):
        logger.info(f'Making api call for record {i+1}')
        model_response = model.generate(data[i]["prompt"])
        test_case = LLMTestCase(
            input=data[i]["query"],
            actual_output=model_response,
            context=[data[i]["context"]],
            expected_output=data[i]["ground_truth"]
        )
        test_cases.append(test_case)
    logger.info('Completed api calls to nowllm')
    logger.info('Started evaluating test cases')
    results = evaluate(
        test_cases=test_cases,
        metrics=[search_qa_metric]
    )
    logger.info('Evaluation completed')        
    search_qa_report(results)
    cleanup_pycache()

