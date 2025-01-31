# Depth Estimation Using ZoeDepth - An End-to-End Python Project

This is an end-to-end Python project utilizing Depth Estimation using ZoeDepth. The project includes a CLI tool and a FastAPI-based web service for depth estimation from images.

## Features

- **CLI Tool**: Easily estimate depth from images using the command line.
- **FastAPI Web Service**: Upload images and get depth estimations via a REST API.
- **Docker Support**: Run the entire application in a Docker container for easy deployment.

## Usage/Example

### CLI Example
```python
usage: cli.py [-h] input_image output_image

Depth Estimation using ZoeDepth

positional arguments:
  input_image   Path to input image file
  output_image  Path to output image file

options:
  -h, --help    show this help message and exit
```

### API

You can check the API documentation from [http://127.0.0.1:8041/docs](http://127.0.0.1:8041/docs)

### Example API Request

To use the API, send a POST request to `/predict` with an image file:

```bash
curl -X POST "http://127.0.0.1:8041/predict" -F "file=@path_to_your_image.jpg"
```

## Run it on your computer

### Clone the Project

```bash
git clone https://github.com/vbahadircan/Depth-Estimation-Using-ZoeDepth-EndtoEnd-Python-Project.git
```

### Install dependencies using pip

```bash
pip install -r requirements.txt
```

### Run the CLI Tool

```bash
python cli.py path_to_input_image.jpg path_to_output_image.png
```

### Run the API

```bash
uvicorn api:app --host 0.0.0.0 --port 8041
```

### Run with Docker

Build the Docker image:

```bash
docker build -t depth-estimation .
```

Run the Docker container:

```bash
docker run -p 8041:8041 depth-estimation
```

## License

[MIT](https://choosealicense.com/licenses/mit/)