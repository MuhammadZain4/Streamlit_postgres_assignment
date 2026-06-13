-- =============================================================
-- seed_data.sql  — 42 sample opportunity records
-- 6 companies, 5 cities, 5 categories, all work modes & statuses
-- =============================================================

INSERT INTO opportunities
    (company_name, job_title, category, city, country, work_mode,
     required_skills, salary_min, salary_max, currency,
     experience_level, application_deadline, status, source_link)
VALUES

-- ── Systems Limited ────────────────────────────────────────────
('Systems Limited', 'Junior Data Scientist',
 'Data Science', 'Lahore', 'Pakistan', 'Onsite',
 'Python, Pandas, Scikit-learn, SQL',
 60000, 90000, 'PKR', 'Entry-Level',
 CURRENT_DATE + INTERVAL '5 days', 'Open',
 'https://www.systemsltd.com/careers/ds001'),

('Systems Limited', 'Senior ML Engineer',
 'AI', 'Lahore', 'Pakistan', 'Hybrid',
 'TensorFlow, PyTorch, MLOps, Docker, Kubernetes',
 180000, 280000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '20 days', 'Open',
 'https://www.systemsltd.com/careers/ml002'),

('Systems Limited', 'Full Stack Developer',
 'Web Development', 'Lahore', 'Pakistan', 'Onsite',
 'React, Node.js, PostgreSQL, REST APIs',
 80000, 130000, 'PKR', 'Mid-Level',
 CURRENT_DATE - INTERVAL '3 days', 'Expired',
 'https://www.systemsltd.com/careers/web003'),

('Systems Limited', 'Cybersecurity Analyst',
 'Cyber Security', 'Lahore', 'Pakistan', 'Onsite',
 'SIEM, Penetration Testing, OWASP, Firewalls',
 100000, 160000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '15 days', 'Open',
 'https://www.systemsltd.com/careers/cs004'),

('Systems Limited', 'Data Engineer Intern',
 'Data Science', 'Lahore', 'Pakistan', 'Hybrid',
 'Python, SQL, ETL, Apache Airflow',
 30000, 45000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '6 days', 'Open',
 'https://www.systemsltd.com/careers/de005'),

('Systems Limited', 'AI Research Intern',
 'AI', 'Lahore', 'Pakistan', 'Remote',
 'Python, NLP, Transformers, HuggingFace',
 25000, 40000, 'PKR', 'Internship',
 CURRENT_DATE - INTERVAL '10 days', 'Closed',
 'https://www.systemsltd.com/careers/ai006'),

-- ── Netsol Technologies ─────────────────────────────────────────
('Netsol Technologies', 'Software Engineer (.NET)',
 'Software Engineering', 'Lahore', 'Pakistan', 'Onsite',
 'C#, .NET Core, Azure, SQL Server',
 90000, 150000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '12 days', 'Open',
 'https://netsoltech.com/jobs/swe001'),

('Netsol Technologies', 'Data Analyst',
 'Data Science', 'Lahore', 'Pakistan', 'Hybrid',
 'Power BI, Excel, SQL, Python',
 55000, 85000, 'PKR', 'Entry-Level',
 CURRENT_DATE + INTERVAL '4 days', 'Open',
 'https://netsoltech.com/jobs/da002'),

('Netsol Technologies', 'DevOps Engineer',
 'Software Engineering', 'Lahore', 'Pakistan', 'Hybrid',
 'Docker, Kubernetes, Jenkins, Terraform, AWS',
 130000, 200000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '30 days', 'Open',
 'https://netsoltech.com/jobs/devops003'),

('Netsol Technologies', 'React Frontend Developer',
 'Web Development', 'Lahore', 'Pakistan', 'Remote',
 'React, TypeScript, Redux, Tailwind CSS',
 70000, 120000, 'PKR', 'Mid-Level',
 CURRENT_DATE - INTERVAL '5 days', 'Expired',
 'https://netsoltech.com/jobs/fe004'),

('Netsol Technologies', 'ML Ops Specialist',
 'AI', 'Lahore', 'Pakistan', 'Onsite',
 'MLflow, Kubeflow, Python, Docker',
 150000, 220000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '25 days', 'Shortlisted',
 'https://netsoltech.com/jobs/mlops005'),

('Netsol Technologies', 'QA Automation Engineer',
 'Software Engineering', 'Lahore', 'Pakistan', 'Onsite',
 'Selenium, Pytest, Postman, JIRA',
 65000, 100000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '18 days', 'Open',
 'https://netsoltech.com/jobs/qa006'),

-- ── Arbisoft ──────────────────────────────────────────────────
('Arbisoft', 'NLP Engineer',
 'AI', 'Lahore', 'Pakistan', 'Hybrid',
 'spaCy, NLTK, BERT, Python, FastAPI',
 120000, 200000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '10 days', 'Open',
 'https://arbisoft.com/jobs/nlp001'),

('Arbisoft', 'Backend Python Developer',
 'Web Development', 'Lahore', 'Pakistan', 'Remote',
 'Django, DRF, PostgreSQL, Redis, Docker',
 90000, 145000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '22 days', 'Open',
 'https://arbisoft.com/jobs/be002'),

('Arbisoft', 'Data Science Intern',
 'Data Science', 'Lahore', 'Pakistan', 'Remote',
 'Python, Pandas, Matplotlib, Scikit-learn',
 20000, 35000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '3 days', 'Open',
 'https://arbisoft.com/jobs/dsi003'),

('Arbisoft', 'Cloud Security Engineer',
 'Cyber Security', 'Lahore', 'Pakistan', 'Hybrid',
 'AWS Security, IAM, CloudTrail, SIEM',
 160000, 240000, 'PKR', 'Senior',
 CURRENT_DATE - INTERVAL '2 days', 'Closed',
 'https://arbisoft.com/jobs/cloudsec004'),

('Arbisoft', 'React Native Developer',
 'Web Development', 'Lahore', 'Pakistan', 'Remote',
 'React Native, JavaScript, Expo, REST APIs',
 80000, 130000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '40 days', 'Open',
 'https://arbisoft.com/jobs/mob005'),

('Arbisoft', 'Computer Vision Engineer',
 'AI', 'Lahore', 'Pakistan', 'Onsite',
 'OpenCV, PyTorch, YOLO, Python',
 140000, 210000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '14 days', 'Shortlisted',
 'https://arbisoft.com/jobs/cv006'),

-- ── Techlogix ─────────────────────────────────────────────────
('Techlogix', 'Business Intelligence Developer',
 'Data Science', 'Karachi', 'Pakistan', 'Onsite',
 'Power BI, SQL Server, DAX, SSAS',
 75000, 120000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '9 days', 'Open',
 'https://techlogix.com/careers/bi001'),

('Techlogix', 'Java Backend Engineer',
 'Software Engineering', 'Karachi', 'Pakistan', 'Hybrid',
 'Java, Spring Boot, Microservices, Kafka',
 100000, 170000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '35 days', 'Open',
 'https://techlogix.com/careers/java002'),

('Techlogix', 'Penetration Tester',
 'Cyber Security', 'Karachi', 'Pakistan', 'Onsite',
 'Kali Linux, Metasploit, Burp Suite, Python',
 110000, 175000, 'PKR', 'Mid-Level',
 CURRENT_DATE - INTERVAL '8 days', 'Expired',
 'https://techlogix.com/careers/pen003'),

('Techlogix', 'Data Engineering Intern',
 'Data Science', 'Karachi', 'Pakistan', 'Hybrid',
 'Python, Spark, Hadoop, SQL',
 25000, 40000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '7 days', 'Open',
 'https://techlogix.com/careers/dei004'),

('Techlogix', 'Generative AI Engineer',
 'AI', 'Karachi', 'Pakistan', 'Remote',
 'LangChain, OpenAI API, RAG, Python, Vector DBs',
 160000, 260000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '45 days', 'Open',
 'https://techlogix.com/careers/genai005'),

('Techlogix', 'WordPress Developer',
 'Web Development', 'Karachi', 'Pakistan', 'Remote',
 'WordPress, PHP, MySQL, Elementor, CSS',
 40000, 70000, 'PKR', 'Entry-Level',
 CURRENT_DATE + INTERVAL '2 days', 'Open',
 'https://techlogix.com/careers/wp006'),

-- ── Contour Software ──────────────────────────────────────────
('Contour Software', 'Senior Data Scientist',
 'Data Science', 'Islamabad', 'Pakistan', 'Hybrid',
 'Python, R, Spark, Machine Learning, Statistics',
 200000, 320000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '28 days', 'Open',
 'https://contour-software.com/jobs/sds001'),

('Contour Software', 'iOS Developer',
 'Software Engineering', 'Islamabad', 'Pakistan', 'Onsite',
 'Swift, SwiftUI, Xcode, Core Data, REST',
 90000, 150000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '16 days', 'Open',
 'https://contour-software.com/jobs/ios002'),

('Contour Software', 'SOC Analyst',
 'Cyber Security', 'Islamabad', 'Pakistan', 'Onsite',
 'SIEM, Splunk, Threat Intelligence, IDS/IPS',
 85000, 140000, 'PKR', 'Entry-Level',
 CURRENT_DATE - INTERVAL '1 days', 'Closed',
 'https://contour-software.com/jobs/soc003'),

('Contour Software', 'AI Product Manager',
 'AI', 'Islamabad', 'Pakistan', 'Hybrid',
 'Product Management, ML Lifecycle, Agile, JIRA',
 180000, 280000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '50 days', 'Open',
 'https://contour-software.com/jobs/aipm004'),

('Contour Software', 'Vue.js Developer',
 'Web Development', 'Islamabad', 'Pakistan', 'Remote',
 'Vue 3, Pinia, REST APIs, TypeScript, Docker',
 75000, 120000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '20 days', 'Shortlisted',
 'https://contour-software.com/jobs/vue005'),

('Contour Software', 'MLOps & Data Pipelines Engineer',
 'Data Science', 'Islamabad', 'Pakistan', 'Hybrid',
 'Airflow, dbt, Snowflake, Python, CI/CD',
 140000, 220000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '33 days', 'Open',
 'https://contour-software.com/jobs/mlops006'),

-- ── i2c Inc. ──────────────────────────────────────────────────
('i2c Inc.', 'Data Analyst Intern',
 'Data Science', 'Rawalpindi', 'Pakistan', 'Onsite',
 'SQL, Excel, Power BI, Python basics',
 22000, 35000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '6 days', 'Open',
 'https://www.i2cinc.com/careers/dai001'),

('i2c Inc.', 'Node.js Backend Developer',
 'Web Development', 'Rawalpindi', 'Pakistan', 'Hybrid',
 'Node.js, Express, MongoDB, REST, JWT',
 80000, 135000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '19 days', 'Open',
 'https://www.i2cinc.com/careers/node002'),

('i2c Inc.', 'Deep Learning Researcher',
 'AI', 'Rawalpindi', 'Pakistan', 'Onsite',
 'PyTorch, CNNs, RNNs, Research Papers, Python',
 160000, 250000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '42 days', 'Open',
 'https://www.i2cinc.com/careers/dl003'),

('i2c Inc.', 'Network Security Engineer',
 'Cyber Security', 'Rawalpindi', 'Pakistan', 'Onsite',
 'Cisco, Firewalls, VPN, Network Monitoring, CCNA',
 95000, 155000, 'PKR', 'Mid-Level',
 CURRENT_DATE - INTERVAL '4 days', 'Expired',
 'https://www.i2cinc.com/careers/netsec004'),

('i2c Inc.', 'Android Developer',
 'Software Engineering', 'Rawalpindi', 'Pakistan', 'Hybrid',
 'Kotlin, Jetpack Compose, Retrofit, Room DB',
 85000, 140000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '24 days', 'Open',
 'https://www.i2cinc.com/careers/android005'),

('i2c Inc.', 'BI & Analytics Engineer',
 'Data Science', 'Rawalpindi', 'Pakistan', 'Remote',
 'Tableau, SQL, Python, Data Modeling, ETL',
 90000, 150000, 'PKR', 'Mid-Level',
 CURRENT_DATE + INTERVAL '11 days', 'Open',
 'https://www.i2cinc.com/careers/bi006'),

-- ── Remote / International roles ──────────────────────────────
('Upwork Client - FinTech', 'Freelance Data Scientist',
 'Data Science', 'Remote', 'Global', 'Remote',
 'Python, ML, Financial Modeling, API Integration',
 500, 1500, 'USD', 'Mid-Level',
 CURRENT_DATE + INTERVAL '60 days', 'Open',
 'https://www.upwork.com/jobs/fintech-ds-001'),

('Toptal Partner', 'Senior AI Engineer (Remote)',
 'AI', 'Remote', 'Global', 'Remote',
 'LLMs, Fine-tuning, Python, Cloud (AWS/GCP)',
 4000, 8000, 'USD', 'Senior',
 CURRENT_DATE + INTERVAL '90 days', 'Open',
 'https://www.toptal.com/jobs/ai-senior-001'),

('Techlogix', 'Cybersecurity Intern',
 'Cyber Security', 'Karachi', 'Pakistan', 'Onsite',
 'Linux, Networking, Ethical Hacking Basics, Python',
 18000, 28000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '5 days', 'Open',
 'https://techlogix.com/careers/cyberint001'),

('Arbisoft', 'Software Engineering Intern',
 'Software Engineering', 'Lahore', 'Pakistan', 'Hybrid',
 'Python or JavaScript, Git, Problem Solving',
 20000, 32000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '8 days', 'Open',
 'https://arbisoft.com/jobs/swei001'),

('Systems Limited', 'Senior Software Architect',
 'Software Engineering', 'Lahore', 'Pakistan', 'Hybrid',
 'System Design, Microservices, Java/.NET, Cloud',
 300000, 480000, 'PKR', 'Senior',
 CURRENT_DATE + INTERVAL '55 days', 'Open',
 'https://www.systemsltd.com/careers/arch001'),

('Contour Software', 'Data Science Intern',
 'Data Science', 'Islamabad', 'Pakistan', 'Hybrid',
 'Python, Jupyter, Pandas, Data Visualization',
 22000, 38000, 'PKR', 'Internship',
 CURRENT_DATE + INTERVAL '4 days', 'Open',
 'https://contour-software.com/jobs/dsi001');

-- Verify record count
DO $$
DECLARE
    rec_count INT;
BEGIN
    SELECT COUNT(*) INTO rec_count FROM opportunities;
    RAISE NOTICE 'seed_data.sql: % opportunity records inserted.', rec_count;
END $$;
