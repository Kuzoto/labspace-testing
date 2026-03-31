FROM dockersamples/labspace-workspace-python

RUN python3 -m pip install --break-system-packages pytest pytest-cov ollama flake8 && sudo apt update && sudo apt-get install -y zstd && curl -fsSL https://ollama.com/install.sh | sh && python3 -m pip install --break-system-packages ollama