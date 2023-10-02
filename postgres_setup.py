import os
import subprocess
import psycopg2
import platform

# Function to check if PostgreSQL is installed
def check_postgres_installed():
    try:
        if platform.system() == "Windows":
            try:
                subprocess.run(["pg_config"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            except Exception as e:
                return False
        return True
    except subprocess.CalledProcessError as e:
        error_message = str(e.stderr, 'utf-8')  # Get the error message as a string
        if "The system cannot find the file specified" in error_message:
            print("Failed to run command: The system cannot find the file specified")
        else:
            print(f"Failed to run command: {e.cmd}")
        return False

# Function to create a PostgreSQL user if it doesn't exist
def create_postgres_user_if_not_exists(dbnamee,username, password):
    try:
        # Connect to the PostgreSQL server as the superuser (postgres) to check if the user exists
        conn = psycopg2.connect(
            dbnamee=dbnamee,  # Connect to the default "postgres" database
            user=username,    # Default superuser username
            password= password,        # Default superuser password (blank for initial setup)
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute(f"SELECT 1 FROM pg_user WHERE usename = '{username}';")
        user_exists = cursor.fetchone()

        if not user_exists:
            # Create a new PostgreSQL user with the specified username and password
            cursor.execute(f"CREATE USER {username} WITH PASSWORD '{password}';")

            # Grant the CREATEDB privilege to the new user
            cursor.execute(f"ALTER USER {username} CREATEDB;")

            # Commit the changes
            conn.commit()

            print(f"User '{username}' created with the specified password and CREATEDB privilege.")
        else:
            print(f"User '{username}' already exists. Skipping user creation.")

        # Close the cursor and connection
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating PostgreSQL user: {str(e)}")

# Function to install PostgreSQL on Windows
def install_postgres_on_windows(username, password, dbnamee):
    try:
        # Check if PostgreSQL is already installed
        if not check_postgres_installed():
            installer_path = "postgresql-14.9-1-windows-x64.exe"

            # Check if the installer file already exists in the same folder
            if not os.path.exists(installer_path):
                print("PostgreSQL is not installed. Downloading and installing...")

                # Download the PostgreSQL installer from the official website
                download_url = "https://get.enterprisedb.com/postgresql/postgresql-14.9-1-windows-x64.exe"

                subprocess.run(["curl", "-o", installer_path, download_url], check=True)

                # Run the installer silently
                subprocess.run([installer_path, "--mode", "unattended"], check=True)
                print("PostgreSQL installed successfully.")

            else:
                print("PostgreSQL installer already exists in the folder.")

        # Clean up the installer file (even if it already existed)
        #os.remove(installer_path)

        # Add PostgreSQL bin directory to the system's PATH
        postgres_bin_dir = os.path.join(os.environ['PROGRAMFILES'], 'PostgreSQL', '14', 'bin')
        os.environ['PATH'] = f"{os.environ['PATH']};{postgres_bin_dir}"

        # Create the PostgreSQL user (if not exists)
		
        print("jkjkjk")

        # Connect to the PostgreSQL server as the new user
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default "postgres" database
            user=username,
            password=password,
            host="localhost",
            port="5432"
        )
        conn.set_session(autocommit=True)  # Set autocommit to True
        
        cursor = conn.cursor()
        
        # Check if the database exists and create it if it doesn't exist
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{dbnamee}';")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f"CREATE DATABASE {dbnamee};")

            create_postgres_user_if_not_exists(dbnamee,username, password)
       
        print("jkj8888kjk")
        conn = psycopg2.connect(
            dbname=dbnamee,  # Connect to the default "postgres" database
            user=username,
            password=password,
            host="localhost",
            port="5432"
        )
        conn.set_session(autocommit=True)  # Set autocommit to True
        
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS objectdet (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                description TEXT
            );
        """)

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        print(f"Database '{dbnamee}' and table 'objectdet' created if they didn't exist.")
    except Exception as e:
        print(f"Error installing and setting up PostgreSQL: {str(e)}")
        exit(1)

if __name__ == "__main__":
    username = "postgres"
    password = "postgres"  # Specify the desired password here
    dbnamee = "skfvision"  # Specify the desired database name here
  
    if platform.system() == "Windows":
        print("jkjkjk")
        install_postgres_on_windows(username, password, dbnamee)
        print("jkjkjk")

    print("PostgreSQL is installed and configured.")
