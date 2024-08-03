class KeywordExtraction:        
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING",{"forceInput": True,"default": ""}),
                "model": ("CUSTOM", {"default": ""}),
                "temperature": ("FLOAT", {"default": 0.15, "min": 0.01, "max": 1.0, "step": 0.01}),                          
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "keyword_extract"
    CATEGORY = "LLM Nodes (gokayfem)"
    
    def keyword_extract(self, prompt, model, temperature):
        gbnf_grammar, documentation = generate_gbnf_grammar_and_documentation([Analysis])
        grammar = LlamaGrammar.from_string(gbnf_grammar, verbose=False)


        wrapped_model = LlamaCppAgent(model, debug_output=True,
                                    system_prompt="You are an advanced AI, tasked to create JSON database entries for analysis.\n\n\n" + documentation)

        response = wrapped_model.get_chat_response(prompt, temperature=temperature, grammar=grammar)
        return (response, )
    
NODE_CLASS_MAPPINGS = {
    "KeywordExtraction": KeywordExtraction,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KeywordExtraction": "Get Keywords",
}