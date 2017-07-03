DROP TABLE IF EXISTS trips;
CREATE TABLE trips (
  duration_ms VARCHAR(250),
  start_time VARCHAR(250),
  start_terminal VARCHAR(250),
  end_time VARCHAR(250),
  end_terminal VARCHAR(250),
  bike_number VARCHAR(20),
  subscription_type VARCHAR(20)
)
