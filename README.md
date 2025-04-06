# Streaming Real-Time Weather Data Using Kafka

This project demonstrates how to stream real-time weather data from OpenWeatherMap using Apache Kafka and store it in MongoDB.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project sets up a data pipeline that fetches real-time weather data from the OpenWeatherMap API, produces the data to an Apache Kafka topic, and consumes it to store in a MongoDB database.

## Features

- Fetches real-time weather data from OpenWeatherMap.
- Streams data using Apache Kafka.
- Stores streamed data into MongoDB.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- Apache Kafka
- MongoDB

Additionally, you'll need an API key from [OpenWeatherMap](https://openweathermap.org/api).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aminkay95/Streaming-Real-Time-Weather-Data-Using-Kafka.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Streaming-Real-Time-Weather-Data-Using-Kafka
   ```

3. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start Apache Kafka:**

   Ensure that your Kafka server is running. Refer to the [Kafka Quickstart](https://kafka.apache.org/quickstart) for guidance.

2. **Start MongoDB:**

   Ensure that your MongoDB server is running.

3. **Set up environment variables:**

   Create a `.env` file in the project directory and add your OpenWeatherMap API key and MongoDB connection string:

   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

4. **Run the producer to fetch and produce weather data:**

   ```bash
   python producer.py
   ```

5. **Run the consumer to consume data from Kafka and store it in MongoDB:**

   ```bash
   python consumer.py
   ```

## Project Structure

```
Streaming-Real-Time-Weather-Data-Using-Kafka/
├── producer.py   # Fetches data from OpenWeatherMap and produces to Kafka
├── consumer.py   # Consumes data from Kafka and stores it in MongoDB
├── main.py       # File that contains functions
├── .gitignore    # Git ignore file
└── README.md     # This README file
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
