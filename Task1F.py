from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

# Build list of stations
stations = build_station_list()

print(inconsistent_typical_range_stations(stations))
