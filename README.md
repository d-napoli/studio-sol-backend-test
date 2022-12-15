# Studio Sol Backend Test

## How to run the application
To simplify the coding process, this project was made using `docker`.

```shell
# generates the iso image for the project
docker-compose build

# run the iso image for the project
docker-compose up
```

After running those commands, you can use the Rest API by going to this address: `0.0.0.0:8000/verify/`
The endpoint is configured to receive `application/json` requests in the following format:

```json
{
	"password": "TesteSenhaForte!123&",
	"rules": [
		{"rule": "minSize","value": 8},
		{"rule": "minSpecialChars","value": 2},
		{"rule": "noRepeted","value": 1},
		{"rule": "minDigit","value": 4}
	]
}
```

You can check more info about the API documentation on the `api-documentation.yaml` file.