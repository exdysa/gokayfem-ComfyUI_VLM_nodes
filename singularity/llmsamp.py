#

class LLMSampler:        
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "system_msg": ("STRING",{"default" : "You are an assistant who perfectly describes images."}),
                "prompt": ("STRING",{"forceInput": True,"default": ""}),
                "model": ("CUSTOM", {"default": ""}),
                "max_tokens": ("INT", {"default": 512, "min": 1, "max": 2048, "step": 1}),
                "temperature": ("FLOAT", {"default": 0.2, "min": 0.01, "max": 1.0, "step": 0.01}),
                "top_p": ("FLOAT", {"default": 0.95, "min": 0.1, "max": 1.0, "step": 0.01}),
                "top_k": ("INT", {"default": 40, "step": 1}), 
                "frequency_penalty": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "presence_penalty": ("FLOAT", {"default": 0.0, "step": 0.01}),
                "repeat_penalty": ("FLOAT", {"default": 1.1, "step": 0.01}),
		        "seed": ("INT", {"default": 42, "step": 1})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_text_advanced"
    CATEGORY = "LLM Nodes (gokayfem)"

    def generate_text_advanced(self, system_msg, prompt, model, max_tokens, temperature, top_p, top_k, frequency_penalty, presence_penalty, repeat_penalty, seed):
        llm = model
        response = llm.create_chat_completion(messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt + " Assistant:"},
        ],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            repeat_penalty=repeat_penalty,
	    seed=seed
            
        )
        return (f"{response['choices'][0]['message']['content']}", )

NODE_CLASS_MAPPINGS = {
    "LLMSampler": LLMSampler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMSampler": "LLMSampler",
}