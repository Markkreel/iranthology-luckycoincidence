# Use the official Jupyter image as the base image
FROM webis/tira-ir-datasets-starter:0.0.54

# Install any required packages
RUN apk add jq libffi-dev && pip3 install jupyter ir_datasets

# Set the working directory to /app
WORKDIR /app

# Copy the notebook and all necessary files into the container
COPY . /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

# Expose the port that the Jupyter notebook runs on
EXPOSE 8888

# Start Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
