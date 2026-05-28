from typing import Protocol


# This is what our program expects to work with
class DataSource(Protocol):
    def get_name(self) -> str: ...
    def get_value(self) -> float: ...


# An external class we don't control — incompatible interface
class ExternalSensor:
    def read(self) -> dict:
        return {"sensor_name": "Temperature", "sensor_value": 22.5}


# The Adapter — wraps ExternalSensor and exposes the interface our program expects
class SensorAdapter:
    def __init__(self, sensor: ExternalSensor):
        self.sensor = sensor

    def get_name(self) -> str:
        return self.sensor.read()["sensor_name"]

    def get_value(self) -> float:
        return self.sensor.read()["sensor_value"]


# Our program — only knows about DataSource, nothing about ExternalSensor
class Dashboard:
    def display(self, source: DataSource) -> None:
        print(f"{source.get_name()}: {source.get_value()}")


# Main
sensor = ExternalSensor()
adapter = SensorAdapter(sensor)
dashboard = Dashboard()

dashboard.display(adapter)  # Temperature: 22.5

'''
EXPLANATION: 

ExternalSensor is the incompatible class - you don't control it and can't modify it
Dashboard only knows about the DataSource interface — it has no idea ExternalSensor exists
SensorAdapter is the translation layer — it wraps ExternalSensor and makes it look like a DataSource
Neither side changes — the adapter does all the work in between

'''