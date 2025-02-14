# OCR Image Processor Script - Supplemental Material

**Important:** This README provides supplemental information for an associated article on local image text recognition using Ollama. Please read the main article first for context and setup instructions.

## Requirements

-   Python 3.x
-   `ollama_ocr` library
-   Ollama installed and a Llama 3.2 Vision model pulled (see main article)

## Usage

Run the script from the command line with the following syntax:

```bash
python ocr_script.py <image_path> [--format_type FORMAT] [--model MODEL]
```


### Arguments

-   `image_path`: Path to the image file (required)
-   `--format_type`: Output format type (optional, default: "text")
    -   Choices: markdown, text, json, structured, key_value
-   `--model`: Model name to use for OCR (optional, default: "llama3.2-vision:11b")  **Note:** This should match the model you have pulled in Ollama (see main article).

### Example

```bash
python script_name.py ./image.jpg --format_type text
```

## Output

The script will print the OCR results in the specified format, followed by the processing duration in seconds.

## Important Notes

-   Make sure you have Ollama installed and a Llama 3.2 Vision model (e.g., `llama3.2-vision:11b`) pulled *before* running this script. See the main article for instructions.
-   The `--model` argument should match the name of the model you pulled in Ollama.
-   The performance of the script depends heavily on your hardware and the size of the model you are using.  See the main article for performance testing information.

## License

This project is licensed under the GNU General Public License v3.0

## Author

Ivan Kavaliou (karavanjo)
