# Discord Weather Bot
![](logo.png)

## Usage
- `!weather`
- `!satellite`
- `!world`
- `!sigwx`

## Running The Bot
### Python
Create a [`.env` file](https://saurabh-kumar.com/python-dotenv/#file-format) in the root folder with the DISCORD_TOKEN variable set to your personal discord token.
Open a terminal in the root folder and run the following commands.

```
pip install -r requirements.txt
python bot.py
```

### Docker
```
docker build -t ghcr.io/aviationtools/weather-bot:main
docker run -e DISCORD_TOKEN=<your_token> ghcr.io/aviationtools/weather-bot:main
```
### Docker Compose
Adjust the token in `docker-compose.yml` to your personal token. Then run the following.
```
docker-compose up --build
```
