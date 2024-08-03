import folder_paths
import os
#

class LLMLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { 
              "ckpt_name": (folder_paths.get_filename_list("llm"), ),   
              "max_ctx": ("INT", {"default": 2048, "min": 128, "max": 128000, "step": 64}),
              "gpu_layers": ("INT", {"default": 27, "min": 0, "max": 100, "step": 1}),
              "n_threads": ("INT", {"default": 8, "min": 1, "max": 100, "step": 1}),
                            }
                }
                
    
    RETURN_TYPES = ("CUSTOM",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_llm_checkpoint"

    CATEGORY = "VLM Nodes/LLM"
    def load_llm_checkpoint(self, ckpt_name, max_ctx, gpu_layers, n_threads):
        ckpt_path = folder_paths.get_full_path("llm", ckpt_name)
        llm = Llama(model_path = ckpt_path, chat_format="chatml", offload_kqv=True, f16_kv=True, use_mlock=False, embedding=False, n_batch=1024, last_n_tokens_size=1024, verbose=True, seed=42, n_ctx = max_ctx, n_gpu_layers=gpu_layers, n_threads=n_threads,) 
        return (llm, ) 

NODE_CLASS_MAPPINGS = {
    "LLMLoader": LLMLoader,
}    

NODE_DISPLAY_NAME_MAPPINGS = {
    "LLMLoader": "LLMLoader",
}