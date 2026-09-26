# vector stash nodes (placeholder)
class VectorStashNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("STRING", {"default": ""})}}
    RETURN_TYPES = ("STRING",)
    FUNCTION = "go"
    CATEGORY = "stash"
    def go(self, value):
        return (value,)

NODE_CLASS_MAPPINGS = {"VectorStashNode": VectorStashNode}
NODE_DISPLAY_NAME_MAPPINGS = {"VectorStashNode": "Vector Stash"}
