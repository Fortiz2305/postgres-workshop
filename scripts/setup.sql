\c workshop;
DROP TABLE IF EXISTS trips;
CREATE TABLE trips (
  duration_ms VARCHAR(250),
  start_time VARCHAR(250),
  start_terminal VARCHAR(250),
  end_time VARCHAR(250),
  end_terminal VARCHAR(250),
  bike_number VARCHAR(20),
  subscription_type VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS events (
  id character varying(40) NOT NULL,
  ts timestamp NOT NULL,
  category character varying(40) NOT NULL,
  type character varying(40) NOT NULL,
  user_id character varying(40),
  data json NOT NULL,

  CONSTRAINT events_pkey PRIMARY KEY (id));
