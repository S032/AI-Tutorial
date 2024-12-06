CREATE TABLE languages (
  id SERIAL PRIMARY KEY,
  name VARCHAR(32)
);

CREATE TABLE manuales (
  id SERIAL PRIMARY KEY,
  name VARCHAR (255),
  language_id INTEGER REFERENCES languages(id)
);

CREATE TABLE topics (
  id SERIAL PRIMARY KEY,
  name VARCHAR (255),
  manuale_id INTEGER REFERENCES manuales(id)
);

CREATE TABLE tutorials (
  id SERIAL PRIMARY KEY,
  name VARCHAR (255),
  content TEXT,
  topic_id INTEGER REFERENCES topics(id)
);
