set -e
psql -d "$POSTGRES_DB" -U "$POSTGRES_USER"<< EOSQL
CREATE TABLE users(
  id INTEGER PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  group_id = INTEGER NOT NULL,
  group_name = VARCHAR(100) NOT NULL,
  is_watch = BOOLEAN NOT NULL,
  created_at TIMESTAMP NOT NULL
);
CREATE TABLE concentration_values(
  user_id INTEGER,
  concentration_value SMALLINT NOT NULL,
  is_sitting BOOLEAN NOT NULL,
  created_at TIMESTAMP,
  PRIMARY KEY (user_id, created_at),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
EOSQL