# Using wxbot from wechatbot-webhook to get local weather information via python to push to wechat
Project dependency https://github.com/danni-cool/wechatbot-webhook
# 1. Import the module:

`requests`: for sending HTTP requests. <br>
`json`: for processing JSON data. <br>
# 2. Define the `Webhook URL`:

`webhook_url`: This is the `UR`L of your `Webhook` service for receiving `POST` requests. In this example, it points to port `3001` on the IP address `192.168.1.133` on your local network. <br>

# 3. Define the function `get_weather_data(city_code)` to get weather data:

This function takes one argument `city_code`, which is the weather code for the city. <br>
Use `requests.get` to send a `GET` request to the `API URL`, which contains the city code. <br>
Check the status code of the `HTTP` response and return an error message if the request fails. <br>
Parses the `JSON` response data to extract the city name, current temperature, weather conditions, air quality, `PM2.5` and `PM10` values, and forecast notifications. <br>

``python
return f "Weather Push City: {city_name}, Current Temperature: {wendu} °C, Weather: {weather_description}, Air Quality: {quality}, PM2.5: {pm25}, PM10: {pm10}, Forecast: {forecast} Information from China Weather Net Query "
``.
The characters inside `return f` can be customized to achieve the effect of customizing the message text<br>
If there is an error parsing `JSON`, catch `json.JSONDecodeError` and return the error message. <br>
Returns a string containing all extracted information. <br>
# 4. Define the function that sends the POST request `send_post_request(content)`:

Sets the request header, specifying the content type as `pplication/json`. <br>
Create a dictionary `payload` containing the recipient's identity, message type and content. <br>
Use `requests.post` to send a `POST` request to the `Webhook URL`, passing `payload` as `JSON` data. <br>
Print the response status code from the Webhook service.
# 5. main function:

Set the city code `city_code` to `01010100`, which is the city code for Beijing. <br>
Call the `get_weather_data` function to get the weather information. <br>
Use a list to store the names of the recipients, and then use a `for` loop to traverse the list, realizing that the function occurs to multiple recipients<br>.
Call the `send_post_request` function to send the weather information to `Webhook`. <br>
# 6. Code to look up your city
> Where 01010100 is the city code, get the city code to enter: 
> http://www.weather.com.cn<br>
> Enter the city you want to need to get the weather on the search box, click query, you can get the corresponding city number on the address bar, and then replace it:
> http://m.weather.com.cn/data/01010100.html
