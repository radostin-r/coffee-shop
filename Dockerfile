FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . ./

ENV PYTHONPATH "${PYTHONPATH}:/app/app"
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint.sh script
COPY entrypoint.sh .

# Grant executable permissions to the entrypoint.sh script
RUN chmod +x entrypoint.sh

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Set the entrypoint command
ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
