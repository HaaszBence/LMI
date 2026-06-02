#!/bin/bash

# Simple script to manage the dev environment
# Usage: ./run.sh [up|down|logs|shell]

COMMAND=$1

case $COMMAND in
  "up")
    docker-compose up --build -d
    echo "🚀 LetsMakeIt is running at http://localhost"
    ;;
  "down")
    docker-compose down
    ;;
  "logs")
    docker-compose logs -f backend
    ;;
  "shell")
    docker-compose exec backend /bin/bash
    ;;
  *)
    echo "Usage: ./run.sh {up|down|logs|shell}"
    exit 1
    ;;
esac
