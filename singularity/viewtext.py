#

class ViewText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "view_text"
    OUTPUT_NODE = True

    CATEGORY = "LLM Nodes (gokayfem)"

    def view_text(self, text):
        # Parse the combined JSON string
        return {"ui": {"text": text}, "result": (text,)}

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {"ViewText": ViewText}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {"ViewText": "ViewText"}
