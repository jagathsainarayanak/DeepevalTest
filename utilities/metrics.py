from deepeval.metrics import GEval, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCaseParams

faithfulness_metric = GEval(
    threshold=0.7,
    name="Faithfulness",
    criteria="Determine whether the actual output is factually correct based on the input.",
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
)

relavance_metric = AnswerRelevancyMetric(
    threshold=0.7,
    model="gpt-4",
    include_reason=True
)

coherance_metric = GEval(
    threshold=0.7,
    name="Coherance",
    criteria="Does the actual output organize the information into a well-structured summary?",
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT]
)

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