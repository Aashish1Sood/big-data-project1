# Analysis of UFO Sighting Data

In thisproject we tried to analyze different MIME types of data and join it together to derive conlusions.
We chose following three datasets

Dataset 1 – Meteorite Landings: Mime Type – Application/JSON
Source - https://data.nasa.gov/resource/y77d-th95.json?$limit=50000

Dataset 2 – Census Data: MIME Type – text/CSV
Input data Sources:  We took Census 2000 and 2010 data from  https://factfinder.census.gov/, Open data source at https://github.com/grammakov/USA-cities-and-states?files=1

Dataset 3 – Sci-Fi Movies: Mime Type – text/HTML
Sci-Fi Movies (e.g. Star Wars, Star Trek) released - based on the year of release of sci-fi movies and the year of the UFO sightings, we can predict if whether the UFO sighting was a delusion or not.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
The libraries used/need to be installed are:-
pip3 install json
pip3 install geopy
pip3 install csv
pip3 install pickle
pip3 install pymongo
pip3 install pandas
pip install BeautifulSoup
pip install bs4
pip install urlib2
pip install tika
pip install editdistance
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Apache Tika](https://tika.apache.org/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
