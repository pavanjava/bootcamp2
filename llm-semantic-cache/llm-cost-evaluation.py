import os

from litellm import completion, cost_per_token
from dotenv import load_dotenv, find_dotenv
import json


class LLMCostMetrics:
    _ = load_dotenv(find_dotenv())

    def display_hidden_params(self):
        response = completion(
            api_key=os.environ['OPENAI_API_KEY'],
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hey, how's it going?"}]
        )

        print(json.dumps(response.json(), indent=4))
        return response

    def compute_cost_per_token(self):
        response = self.display_hidden_params()
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        prompt_tokens_cost_usd_dollar, completion_tokens_cost_usd_dollar = cost_per_token(model="gpt-3.5-turbo",
                                                                                          prompt_tokens=prompt_tokens,
                                                                                          completion_tokens=completion_tokens)
        print(f'prompt_tokens_cost_usd_dollar: {prompt_tokens_cost_usd_dollar}')
        print(f'completion_tokens_cost_usd_dollar: {completion_tokens_cost_usd_dollar}')
        print(f'total_cost: {prompt_tokens_cost_usd_dollar + completion_tokens_cost_usd_dollar}')


if __name__ == '__main__':
    cost_metrics = LLMCostMetrics()
    cost_metrics.display_hidden_params()
    cost_metrics.compute_cost_per_token()
