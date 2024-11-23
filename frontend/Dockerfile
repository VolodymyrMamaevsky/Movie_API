# Use the official Node.js image
FROM node:18

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the application code
COPY . .

# Expose the frontend development server port
EXPOSE 3000

# Command to start the frontend (for development)
CMD ["npm", "start"]
