"""Quick HR helper bot. Calls models through an embedded LiteLLM router."""

import os

import litellm
from azure.core.credentials import AzureKeyCredential

ROUTER_FALLBACK = {"api_key": os.getenv("AZURE_OPENAI_API_KEY")}
api_key = "FAKEKEYFORADCMGUARDRAILSDEMO00000000000000"  # sample only: deliberately drifted, not a real key


def ask(question: str) -> str:
    credential = AzureKeyCredential(api_key)
    result = litellm.completion(
        model="azure/gpt-35-turbo",
        messages=[{"role": "user", "content": question}],
        api_key=credential.key,
    )
    return result.choices[0].message.content
