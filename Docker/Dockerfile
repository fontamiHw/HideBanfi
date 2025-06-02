 # Use the official lightweight Python image
FROM python:3.12-slim


# Set the working directory
WORKDIR /app

# # Download latest listing of available packages:
RUN apt-get -y update
# # Upgrade already installed packages:
RUN apt-get -y upgrade
# Install a new package:
RUN apt-get -y install vim net-tools iputils-ping 
RUN apt-get -y install cron supervisor procps

# Define environment variable
ENV APP_ROOT_PATH="/app"
ENV APP_ROOT_HOST="${APP_ROOT_PATH}/host"
ENV TMP_RESOURCE_PATH="${APP_ROOT_PATH}/resources"
ENV APP_SOR_FILES="${APP_ROOT_HOST}/SOR"
ENV APP_JPG_FILES="${APP_ROOT_HOST}/JPG"
ENV APP_LOG_FILES="${APP_ROOT_HOST}/logs"

# will be created from the run script 
ENV RESOURCE_PATH="${APP_ROOT_HOST}/resources"

# Create a new directory under /app
RUN mkdir -p ${APP_ROOT_HOST}
RUN mkdir -p ${TMP_RESOURCE_PATH}

# Install any needed packages specified in requirements.txt
# If you don't have any additional packages, you can skip this step
RUN pip install --no-cache-dir  --force-reinstall -v matplotlib>=3.10.3 pyaml>=25.5.0
RUN pip install --no-cache-dir --force-reinstall -v webex-bot[proxy]==0.5.2 webexteamssdk==1.6.1 

# Copy project files
# Copy the current directory contents into the container at /app
COPY app ${APP_ROOT_PATH}
# Copy the start application
COPY run.sh /app/run.sh

# Start supervisor from the script
CMD ["/app/run.sh"]