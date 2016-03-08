# API prototype
API Prototype for DrChrono


## Installation

In the directory you wish to use for this project...

1. Create a virtualenv and start it up:
    ```
    virtualenv drchrono
    cd drchrono
    source bin/activate
    ```

2. Download this repository:
    ```    
    git clone git@github.com:kyitguy/API.git
    ```

3. Install required python libraries
    ```
    cd API
    pip install -r requirements.txt
    ```

4. Create a file `config_no_commit.py` in the 'API' directory with these
   contents:
    ```
    DRCHRONO_APP_ID = 'The Client ID value from DrChrono API page'
    DRCHRONO_APP_SECRET = 'The Client Secret value from DrChrono API page'
    ```

5. Run the application:
    ```
    python app.py
    ```

6. Go to [http://localhost:5000/](http://localhost:5000/) to view the application.
