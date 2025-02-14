from ollama_ocr import OCRProcessor

import time
start_time = time.perf_counter()
print(f"Start time: {start_time:.2f} seconds")

ocr = OCRProcessor(model_name='llama3.2-vision:11b')

result = ocr.process_image(
    image_path="./hero.jpg",
    format_type="text"
)
print(result)

end_time = time.perf_counter()
print(f"End time: {end_time:.2f} seconds")
duration = end_time - start_time
print(f"Duration: {duration:.2f} seconds")
