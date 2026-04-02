from typing import Callable
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
def eval_single_response_translation(expected_answer: str, llm_response: str) -> float:
  '''TODO: Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
  embeddings = model.encode([expected_answer, llm_response])
  similarity = util.cos_sim(embeddings[0], embeddings[1])
  score = float(similarity)

  return score

def eval_single_response_classification(expected_answer: str, llm_response: str) -> float:
  '''TODO: Compares an LLM response to the expected answer from the evaluation dataset using one of the text comparison metrics.'''
  expected = expected_answer.strip().lower()
  response = llm_response.strip().lower()

  return 1.0 if expected == response else 0
  
def evaluate(query_fn: Callable[[str], str], eval_fn: Callable[[str, str], float], dataset) -> float:
  '''
  TODO: Computes an aggregate score of the chosen evaluation metric across the given dataset. Calls the query_fn function to generate
  LLM outputs for each of the posts in the evaluation dataset, and calls eval_single_response to calculate the metric.
  '''
  total_score = 0.0

  for item in dataset:
    llm_response = query_fn(item["post"])
    score = eval_fn(item["expected_answer"], llm_response)
    total_score += score

  avg_score = total_score / len(dataset)

  return avg_score