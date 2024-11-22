# import requests


# def download_file(url, file_name):

#     file_name = f"{}"
#     # Send a GET request to the provided URL
#     response = requests.get(url)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Open a local file in binary write mode and save the content
#         with open(file_name, 'wb') as file:
#             file.write(response.content)
#         print(f"File '{file_name}' downloaded successfully.")
#     else:
#         print(f"Failed to download file '{file_name}'.")
#         print(f"status code : {response.status_code}")
        
# # to test and debug the code
# if __name__ == "_main_":
# 	url = 'https://example.com/file.pdf'
#      ext = url.split('-')[-1].lower()
# 	file_name = 'FileName'
# 	download_file(url, "Python_logo")
