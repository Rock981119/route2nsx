# set base image (host OS)
FROM python:3.9.2-alpine
COPY requirements.txt .
# install dependencies
RUN pip install -r requirements.txt
# set the working directory in the container
WORKDIR /app
# copy the content of the local src directory to the working directory
# copy only the dependencies installation from the 1st stage image
COPY route2nsx.py .
# command to run on container start
CMD [ "python", "./route2nsx.py" ]
# ENTRYPOINT ["tail", "-f", "/dev/null"]