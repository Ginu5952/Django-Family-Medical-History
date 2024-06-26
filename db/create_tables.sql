SET searh_path TO family;

CREATE TYPE family_member_marital_status AS ENUM (
        'Single', 'Married', 'Divorced', 'Widowed', 'Separated', 'Committed', 'Other'
    );

CREATE TABLE IF NOT EXISTS family_health_insurance_card_details(
            health_insurance_card_no VARCHAR(50) PRIMARY KEY,
            expiry_date_of_card DATE,

            CHECK (expiry_date_of_card > CURRENT_DATE)
        );

CREATE TABLE IF NOT EXISTS hospital_details(
            hospital_id SERIAL PRIMARY KEY,
            hospital_name VARCHAR(50) NOT NULL,
            location VARCHAR(50),
            address VARCHAR(50),
            contact_number VARCHAR(15) UNIQUE,
            website VARCHAR(100) UNIQUE,
            registration_fees MONEY,
            UNIQUE(hospital_name,location, address)
        );   

CREATE TABLE IF NOT EXISTS doctor_details ( 
            doctor_id SERIAL PRIMARY KEY,
            hospital_id INT NOT NULL,
            department VARCHAR(50) NOT NULL, 
            doctor_name VARCHAR(20) NOT NULL, 
            gender CHAR(1) CHECK (gender IN ('M', 'F')), 
            availability_days TEXT[],
            consultation_hours JSONB,
            contact_no VARCHAR(15) UNIQUE,
            UNIQUE (doctor_id, hospital_id, department),
            FOREIGN KEY (hospital_id) REFERENCES hospital_details(hospital_id)
            
        );                     
CREATE TABLE IF NOT EXISTS family_member_details(
                member_id SERIAL PRIMARY KEY,
                health_insurance_card_no VARCHAR(50) NOT NULL,
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20),
                age INT,
                relation VARCHAR(15),
                gender VARCHAR(10) CHECK (gender IN ('M', 'F')),
                marital_status family_member_marital_status,
                profession VARCHAR(20),
                contact_no VARCHAR(15) UNIQUE,
                UNIQUE(health_insurance_card_no, first_name, relation),
           
                FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no)
            );

CREATE TABLE IF NOT EXISTS children_check_up_details (
            check_up_id SERIAL PRIMARY KEY,
            health_insurance_card_no  VARCHAR(50),
            parents_name VARCHAR(50) NOT NULL,
            number_of_children INT,
            children_name_and_age JSONB,
            vaccination_details JSONB,
            date_of_vaccination JSONB,
            vaccination_name TEXT[],
            UNIQUE(health_insurance_card_no,parents_name),
            FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no)
        );            
CREATE TABLE IF NOT EXISTS family_yearly_check_up_details(
            yearly_check_up_id SERIAL PRIMARY KEY,
            health_insurance_card_no VARCHAR(50) NOT NULL,
            yearly_check_up_done BOOLEAN,
            date_of_check_up DATE,
            
            CHECK(yearly_check_up_done IN (TRUE, FALSE)),
            CHECK(date_of_check_up <= CURRENT_DATE),
            UNIQUE(health_insurance_card_no, date_of_check_up),
            FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no)
        );
        
CREATE TABLE IF NOT EXISTS family_medical_details(
                visit_id SERIAL PRIMARY KEY,
                health_insurance_card_no VARCHAR(50) NOT NULL,
                doctor_id INT NOT NULL,
                hospital_id INT NOT NULL,
                department VARCHAR(50) NOT NULL,
                date_of_visit TIMESTAMPTZ NOT NULL,
                symptoms TEXT[],
                diagnosis TEXT[],
                medication TEXT[],

                CHECK(date_of_visit <= CURRENT_DATE),
                FOREIGN KEY (health_insurance_card_no) REFERENCES family_health_insurance_card_details (health_insurance_card_no),
                FOREIGN KEY (doctor_id, hospital_id, department) REFERENCES doctor_details (doctor_id, hospital_id, department)
            );
