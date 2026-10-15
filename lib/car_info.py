from datetime import date
from typing import List, Dict, Optional


class Reading:
    """Represents a single reading for a tyre at a specific point in time."""
    def __init__(self, pressure: float, tread_depth: float, reading_date: Optional[date] = None):
        self.pressure = pressure            # e.g., 32.0 PSI
        self.tread_depth = tread_depth      # e.g., 6.5 mm
        # Default to today's date if no date is provided
        self.reading_date = reading_date if reading_date else date.today()


class Tyre:
    """Represents a single tyre position on a car."""
    def __init__(self, position: str):
        self.position = position            # e.g., "Front Left"
        self.readings: List[Reading] = []   # List of historical Reading objects

    def add_reading(self, pressure: float, tread_depth: float, reading_date: Optional[date] = None) -> None:
        """Creates a Reading object and adds it to history."""
        new_reading = Reading(pressure, tread_depth, reading_date)
        self.readings.append(new_reading)

    def get_latest_reading(self) -> Optional[Reading]:
        """Returns the most recent reading, or None if no readings exist."""
        if not self.readings:
            return None
        # Return the last added reading
        return self.readings[-1]


class Car:
    """Manages all tyres on the car."""
    def __init__(self):
        # Initialize standard 4 tyre positions
        self.tyres: Dict[str, Tyre] = {
            "Front Left": Tyre("Front Left"),
            "Front Right": Tyre("Front Right"),
            "Rear Left": Tyre("Rear Left"),
            "Rear Right": Tyre("Rear Right")
        }

    def record_tyre_reading(self, position: str, pressure: float, tread_depth: float, reading_date: Optional[date] = None) -> None:
        """Finds the tyre at the position and adds a reading."""
        if position not in self.tyres:
            raise ValueError(f"Invalid tyre position: {position}")
        
        self.tyres[position].add_reading(pressure, tread_depth, reading_date)

    def get_summary(self) -> List[Dict]:
        """
        Returns a list showing each tyre's position, 
        latest pressure, tread depth, and reading date.
        """
        summary = []
        for position, tyre in self.tyres.items():
            latest = tyre.get_latest_reading()
            if latest:
                summary.append({
                    "position": position,
                    "pressure": latest.pressure,
                    "tread_depth": latest.tread_depth,
                    "date": latest.reading_date
                })
            else:
                summary.append({
                    "position": position,
                    "pressure": None,
                    "tread_depth": None,
                    "date": None
                })
        return summary