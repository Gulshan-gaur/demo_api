FROM python:3.10-slim 

WORKDIR /app
 
RUN pip install --upgrade pip
# Install gunicorn
RUN pip install gunicorn

# Copy requirements.txt and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the apps folder
COPY app/ app/
# Copy the wsgi.py file (assuming it is in the root directory)
COPY run.py .

# Expose the port
EXPOSE 5000

# Start the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
