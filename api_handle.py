import requests

if __name__ == '__main__':

    while True:
        # Take input from the terminal
        comment = input("Enter your comment:")
        if comment == "":
            break
    # Perform ML calculations (Sentiment Analysis) using the API
        api_url = 'http://localhost:5000/api/sentiment'
        data = {'comment': comment}
        print(data)
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            print("Data saved successfully to MongoDB.")
        else:
            print("Failed to save data.")
