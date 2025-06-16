CREATE TABLE clicks (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT now(),
    ip TEXT NOT NULL,
    user_agent TEXT NOT NULL,
    referrer TEXT,
    source TEXT,
    campaign TEXT
);
