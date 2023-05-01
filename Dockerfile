# Use the official Jupyter image as the base image
FROM webis/tira-ir-datasets-starter:0.0.54

# Set the working directory to /app
WORKDIR /app

# Copy the notebook and all necessary files into the container
COPY . .


# Install any required packages
RUN pip3 install ir_datasets

# Expose the port that the Jupyter notebook runs on
EXPOSE 8888

# Start Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
