from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams


search_qa_metric = GEval(
    threshold=0.7,
    name='Search QA Metric',
    evaluation_steps=[
        'Determime if the "input" query can be answered using the "context".',
        'If the context contains sufficient information, check if the actual answer correctly answers the question.',
        'Check if "actual output" matches the "expected output".'
    ],
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT, LLMTestCaseParams.CONTEXT]
)