# EXAMPLES TAKEN FROM ArjanCodes Video

# ADAPTER PATTERN
'''
The Adapter pattern solves the problem of incompatible interfaces —
situations where you have data or an object in one format, but another part of your program expects a different format.
Rather than modifying either side, you introduce an Adapter class that sits in between and acts as a translation layer.
The Adapter wraps the incompatible object and exposes an interface that the rest of your program can work with, 
handling all the conversion logic internally. This keeps both sides clean and decoupled — 
neither the source nor the consumer needs to know anything about the other. 
A good analogy is a power plug adapter when travelling abroad — the socket and your device haven't changed,
 but the adapter in between makes them compatible
'''

# Don't worry too much about the formats and attributes
# This example is more about how the design pattern does what it does

# The key issue we solve here is that we are reading an XML file
# Beutiful Soup upon parsing XML provides as on object that has methods from which we can extract data
# JSON data on the other hand exists in key:value pairs (We need to provide JSON data to our Experiment class)
# So when we read XML data, but need the data in JSON format in order to work with other parts of our program, we need an translational layer
# that will help us convert it or ADAPT it to JSON
# This is where the Adapter comes in, and provides a layer that helps adapt the incompatible data to data compatible with your program


from bs4 import BeautifulSoup

# BeautifulSoup is a Python library for parsing and extracting data from HTML and XML files — it's the go-to tool for web scraping

from experiment import Experiment # imports Experiment from an experiment file
from xml_adapter import XMLAdapter


def main() -> None:
    with open("config.xml", encoding="utf8") as file: # Opens an XML file
        config_xml = file.read()
    bs_xml = BeautifulSoup(config_xml, "xml")
    adapter = XMLAdapter(bs_xml)
    experiment = Experiment(adapter)
    experiment.run()


if __name__ == "__main__":
    main()