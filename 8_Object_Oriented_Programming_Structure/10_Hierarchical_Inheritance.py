# PARENT CLASS: The Base AI Model
class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def power_on(self):
        print(f"System: {self.model_name} is now online and ready.")

# CHILD 1: Specialized for Text (Inherits from AIModel)
class TextGenerator(AIModel):
    def generate_story(self, prompt):
        print(f"Text-AI: Writing a story about '{prompt}'...")

# CHILD 2: Specialized for Images (Inherits from AIModel)
class ImageGenerator(AIModel):
    def generate_art(self, style):
        print(f"Image-AI: Generating a high-res masterpiece in {style} style.")

# CHILD 3: Specialized for Audio (Inherits from AIModel)
class AudioGenerator(AIModel):
    def generate_music(self, genre):
        print(f"Audio-AI: Composing a 2026 {genre} track.")

# --- Execution ---

# Multiple children using the same parent features
gpt = TextGenerator("GPT-5")
midjourney = ImageGenerator("MJ-v7")

gpt.power_on()       # Method from Parent
gpt.generate_story("The future of Python") # Method from Child 1

midjourney.power_on() # Method from Parent
midjourney.generate_art("Cyberpunk") # Method from Child 2
