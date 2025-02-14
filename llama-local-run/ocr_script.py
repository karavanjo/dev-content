import argparse
import time
from ollama_ocr import OCRProcessor

def main():
    parser = argparse.ArgumentParser(description="Process an image using OCR.")
    parser.add_argument("image_path", help="Path to the image file")
    parser.add_argument("--format_type", choices=["markdown", "text", "json", "structured", "key_value"], 
                        default="text", help="Output format type")
    parser.add_argument("--model", default="llama3.2-vision:11b", help="Model name to use for OCR")
    args = parser.parse_args()

    ocr = OCRProcessor(model_name=args.model)

    start_time = time.perf_counter()

    result = ocr.process_image(
        image_path=args.image_path,
        format_type=args.format_type
    )
    print(result)

    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\nDuration: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
