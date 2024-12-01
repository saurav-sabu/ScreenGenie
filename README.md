# ScreenGenie: ATS Tracking Application

## Project Setup Details

Follow the steps below to set up and run the project locally:

### Clone the Repository
```bash
git clone <repository-url>
cd ScreenGenie
```

### Create a Virtual Environment
Using Conda:
```bash
conda create -p venv python=3.12 -y
conda activate ./venv
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Set your Google API key in the .env file.
```bash
Google_API_KEY=your-google-api-key
```

### Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```

### Notes
- Ensure you have Python 3.12 installed.
- Replace `<repository-url>` with the actual URL of the Git repository.
- Replace `your-google-api-key` with your valid Google API key.

You're now ready to use ScreenGenie! 🎉
