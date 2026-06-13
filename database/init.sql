-- =============================================================
-- init.sql  — Runs once when the PostgreSQL container is created
-- Creates the database schema for the Internship & Job Tracker
-- =============================================================

-- Drop table if a previous run left a partial state (safe on fresh volume)
DROP TABLE IF EXISTS opportunities;

CREATE TABLE opportunities (
    opportunity_id      SERIAL PRIMARY KEY,
    company_name        VARCHAR(100)    NOT NULL,
    job_title           VARCHAR(150)    NOT NULL,
    category            VARCHAR(50)     NOT NULL,
    city                VARCHAR(80),
    country             VARCHAR(80),
    work_mode           VARCHAR(30)     CHECK (work_mode IN ('Remote', 'Onsite', 'Hybrid')),
    required_skills     TEXT            NOT NULL,
    salary_min          NUMERIC(10,2),
    salary_max          NUMERIC(10,2),
    currency            VARCHAR(10)     DEFAULT 'PKR',
    experience_level    VARCHAR(50),
    application_deadline DATE,
    status              VARCHAR(30)     DEFAULT 'Open'
                                        CHECK (status IN ('Open', 'Closed', 'Expired', 'Shortlisted')),
    source_link         TEXT,
    created_at          TIMESTAMP       DEFAULT CURRENT_TIMESTAMP
);

-- Index on frequently filtered columns
CREATE INDEX idx_status       ON opportunities (status);
CREATE INDEX idx_category     ON opportunities (category);
CREATE INDEX idx_city         ON opportunities (city);
CREATE INDEX idx_deadline     ON opportunities (application_deadline);
CREATE INDEX idx_work_mode    ON opportunities (work_mode);

-- Verify table was created
DO $$
BEGIN
    RAISE NOTICE 'opportunities table created successfully.';
END $$;
