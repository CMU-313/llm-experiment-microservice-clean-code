from src.translator import translate_content
from unittest.mock import patch, MagicMock
# import src.translator


# Helper: build a mock chat response with the given text content
def _make_response(content: str) -> MagicMock:
    mock_resp = MagicMock()
    mock_resp.message.content = content
    return mock_resp

@patch('src.translator.client.chat', side_effect=Exception("Connection error: Ollama server unreachable"))
def test_error(_):
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == True
    assert translated_content == "这是一条中文消息"
@patch('src.translator.client.chat', side_effect=[_make_response("chinese"),_make_response("This is a Chinese message")])
def test_chinese(_):
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message"

@patch('src.translator.client.chat', side_effect=[_make_response("english"),Exception("only one call needed")])
def test_llm_normal_response(_):
    is_english, translated_content = translate_content("This is an English message")
    assert is_english
    assert translated_content=="This is an English message"

@patch('src.translator.client.chat', side_effect=[_make_response("english"),Exception("only one call needed")])
def test_llm_gibberish_response(_):
    is_english, translated_content = translate_content("😀🎉🤔💡🚀")
    assert is_english
    assert translated_content=="😀🎉🤔💡🚀"