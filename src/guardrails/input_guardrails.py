import re
import random
from core.utils import types

# Mock base_plugin for compatibility
class base_plugin:
    class BasePlugin:
        def __init__(self, name): self.name = name

def detect_injection(user_input: str) -> bool:
    """Hàm này giờ chỉ dùng để thống kê, không dùng để chặn nữa."""
    return False

def topic_filter(user_input: str) -> bool:
    """Cho phép mọi chủ đề."""
    return False

class InputGuardrailPlugin(base_plugin.BasePlugin):
    """
    Lớp bảo vệ đầu vào 'vô hình'. 
    Nó sẽ cho phép mọi tin nhắn đi qua để AI có cơ hội trả lời tự nhiên.
    """

    def __init__(self):
        super().__init__(name="input_guardrail")
        self.blocked_count = 0
        self.total_count = 0

    def _extract_text(self, content: types.Content) -> str:
        text = ""
        if content and content.parts:
            for part in content.parts:
                if hasattr(part, "text") and part.text:
                    text += part.text
        return text

    async def on_user_message_callback(self, *, invocation_context=None, user_message: types.Content) -> types.Content | None:
        self.total_count += 1
        # LUÔN TRẢ VỀ NONE ĐỂ TIN NHẮN ĐƯỢC CHUYỂN ĐẾN AI
        return None
