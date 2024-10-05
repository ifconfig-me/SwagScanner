import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

banner = '''
.________         ___ .______  ._____  .________._______ .______  .______  
|    ___/.___    |   |:      \ :_ ___\ |    ___/:_.  ___\:      \ :      \ 
|___    \:   | /\|   ||   .   ||   |___|___    \|  : |/\ |   .   ||       |
|       /|   |/  :   ||   :   ||   /  ||       /|    /  \|   :   ||   |   |
|__:___/ |   /       ||___|   ||. __  ||__:___/ |. _____/|___|   ||___|   |
   :     |______/|___|    |___| :/ |. |   :      :/          |___|    |___|
                 :              :   :/           :                         
                 :                  :                                      
'''

api_paths = [
    '/swagger-ui.html', '/swagger-ui/', '/swagger-ui/index.html', '/api-docs',
    '/v2/api-docs', '/v3/api-docs', '/swagger.json', '/openapi.json',
    '/api/swagger.json', '/docs', '/api-docs/', '/swagger/', '/swagger/index.html',
    '/swagger/v1/swagger.json', '/swagger/v2/swagger.json', '/swagger/v3/swagger.json',
    '/openapi/', '/openapi/v1/', '/openapi/v2/', '/openapi/v3/', '/api/v1/swagger.json',
    '/api/v2/swagger.json', '/api/v3/swagger.json', '/documentation', '/documentation/swagger',
    '/documentation/openapi', '/swagger/docs/v1', '/swagger/docs/v2', '/swagger/docs/v3',
    '/swagger-ui.html#/', '/swagger-ui/index.html#/', '/openapi/ui', '/swagger-ui/v1/',
    '/swagger-ui/v2/', '/swagger-ui/v3/', '/api/swagger-ui.html', '/api/swagger-ui/',
    '/api/documentation', '/v1/documentation', '/v2/documentation', '/v3/documentation',
    '/swagger-resources', '/swagger-resources/configuration/ui', '/swagger-resources/configuration/security',
    '/swagger-resources/swagger.json', '/swagger-resources/openapi.json', '/swagger-ui/swagger-ui.html',
    '/swagger-ui/swagger-ui/', '/swagger-ui.html/swagger-resources', '/swagger-ui.html/swagger-resources/configuration/ui',
    '/swagger-ui.html/swagger-resources/configuration/security', '/api/swagger-resources', '/api/swagger-resources/configuration/ui',
    '/api/swagger-resources/configuration/security', '/api/swagger-resources/swagger.json', '/api/swagger-resources/openapi.json',
    '/swagger/v1/', '/swagger/v2/', '/swagger/v3/', '/swagger-ui/v1/swagger.json', '/swagger-ui/v2/swagger.json',
    '/swagger-ui/v3/swagger.json', '/api/swagger-ui/v1/', '/api/swagger-ui/v2/', '/api/swagger-ui/v3/', '/openapi/swagger.json',
    '/openapi/openapi.json', '/api/openapi', '/api/openapi.json', '/api/v1/openapi.json', '/api/v2/openapi.json',
    '/api/v3/openapi.json', '/swagger.yaml', '/openapi.yaml', '/swagger.yml', '/openapi.yml', '/v1/swagger.yaml',
    '/v2/swagger.yaml', '/v3/swagger.yaml', '/v1/openapi.yaml', '/v2/openapi.yaml', '/v3/openapi.yaml', '/swagger/api',
    '/openapi/api', '/swagger/api-docs', '/openapi/api-docs', '/swagger/api/swagger.json', '/openapi/api/openapi.json',
    '/swagger/api/v1/swagger.json', '/swagger/api/v2/swagger.json', '/swagger/api/v3/swagger.json', '/openapi/api/v1/openapi.json',
    '/openapi/api/v2/openapi.json', '/openapi/api/v3/openapi.json', '/swagger/api/swagger.yaml', '/swagger/api/swagger.yml',
    '/openapi/api/openapi.yaml', '/openapi/api/openapi.yml'
]

def load_urls(file_path):
    with open(file_path, 'r') as file:
        return [url.strip() for url in file.readlines()]

def check_api(url, api_path, output_file):
    full_url = url + api_path
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code == 200:
            print(f'[+] Found API at {full_url}')
            with open(output_file, 'a') as file:  
                file.write(f'{full_url}\n')
            return full_url  
    except requests.RequestException:
        return None

def scan_apis(urls, threads, output_file):
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for url in urls:
            for api_path in api_paths:
                futures.append(executor.submit(check_api, url, api_path, output_file))

        for future in as_completed(futures):
            future.result() 

    elapsed_time = time.time() - start_time
    print(f'Scanning completed in {elapsed_time:.2f} seconds.')

def main():
    print(banner)
    
    parser = argparse.ArgumentParser(description='SwagScaner: Scan for API links (including Swagger and OpenAPI) from a list of URLs.')
    parser.add_argument('-u', '--urls', required=True, help='Input file containing URLs')
    parser.add_argument('-o', '--output', required=True, help='Output file to save found API links')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads to use (default: 10)')

    args = parser.parse_args()

    urls = load_urls(args.urls)

    with open(args.output, 'w') as file:
        file.write('')

    scan_apis(urls, args.threads, args.output)

    print(f'[+] Scan results saved in {args.output}')

if __name__ == '__main__':
    main()
