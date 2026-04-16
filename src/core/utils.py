"""
Lab 11 — Helper Utilities
"""
from openai import OpenAI

# Mock classes for compatibility
class types:
    class Part:
        @staticmethod
        def from_text(text): return type('Part', (), {'text': text})
    class Content:
        def __init__(self, role, parts): 
            self.role = role
            self.parts = parts

async def chat_with_agent(agent, runner, user_message: str, session_id=None):
    """Send message to OpenAI model using the same interface."""
    client = OpenAI()
    messages = [{"role": "system", "content": agent.instruction}]
    
    # 1. Input Guardrail Logic (Manual Interception)
    class UserContent: 
        def __init__(self, text): self.parts = [types.Part.from_text(text)]
    
    for plugin in getattr(runner, 'plugins', []):
        if hasattr(plugin, 'on_user_message_callback'):
            res = await plugin.on_user_message_callback(invocation_context=None, user_message=UserContent(user_message))
            if res: return res.parts[0].text, type('Session', (), {'id': 'session_123'})

    messages.append({"role": "user", "content": user_message})
    
    # 2. Main Model Call
    try:
        response = client.chat.completions.create(
            model=agent.model if agent.model and 'gpt' in agent.model else 'gpt-4o-mini',
            messages=messages
        )
        final_response = response.choices[0].message.content
    except Exception as e:
        final_response = f"Error calling OpenAI: {e}"

    # 3. Output Guardrail Logic (Manual Interception)
    for plugin in getattr(runner, 'plugins', []):
        if hasattr(plugin, 'after_model_callback'):
            class MockResponse: 
                def __init__(self, text): self.content = type('Content', (), {'parts': [types.Part.from_text(text)]})
            
            res = await plugin.after_model_callback(callback_context=None, llm_response=MockResponse(final_response))
            final_response = res.content.parts[0].text

    return final_response, type('Session', (), {'id': 'session_123'})
