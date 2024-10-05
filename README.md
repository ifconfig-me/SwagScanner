# SwagScaner

**SwagScaner** is a multithreaded tool designed to efficiently scan a list of URLs for various API endpoints, including Swagger and OpenAPI specifications. This tool helps developers, security researchers, and penetration testers discover exposed API documentation on websites.

## Features

- Scans for a wide range of common API paths, including Swagger and OpenAPI
- Uses multithreading to speed up the scanning process
- Outputs discovered API endpoints to a specified file
- Handles connection timeouts and exceptions gracefully
- Simple to use with flexible options for file input and thread management

## Installation

To install and use **SwagScaner**, ensure that Python 3.x is installed on your system. You will also need the following Python libraries:

```bash
pip install requests argparse
```

## Usage

```bash
python swagscaner.py -u <urls_file> -o <output_file> [-t <threads>]
```

### Arguments:
- `-u`, `--urls`: Input file containing the list of URLs to scan.
- `-o`, `--output`: Output file where the discovered API links will be saved.
- `-t`, `--threads`: (Optional) Number of threads to use for concurrent scanning. Default is 10.

### Example:

```bash
python swagscaner.py -u urls.txt -o api_links.txt -t 20
```

This will scan the URLs in `urls.txt` for known API paths using 20 threads and save any found APIs to `api_links.txt`.

## Sample Output

The tool will output any found API URLs like this:

```
[+] Found API at https://example.com/swagger.json
[+] Found API at https://api.example.com/v2/api-docs
```

All found links are also saved to the output file you specify.

## API Paths Scanned

SwagScaner looks for the following commonly used API paths (Swagger, OpenAPI, and others):

- `/swagger-ui.html`
- `/swagger-ui/`
- `/swagger-ui/index.html`
- `/api-docs`
- `/v2/api-docs`
- `/v3/api-docs`
- `/swagger.json`
- `/openapi.json`
- `/api/swagger.json`
- `/docs`
- `/swagger/`
- `/openapi/`
- `/swagger.yaml`
- `/openapi.yaml`
- `/swagger.yml`
- `/openapi.yml`
- `/documentation`
- And many more... (See the full list in the script)

## Contributing

Feel free to submit issues or pull requests on [GitHub](https://github.com/ifconfig-me). Contributions are welcome!

