# NV_AIQ_UI
This is UI for AIQToolkit from Nvidia

### How to run

1. Clone the NV_AIQ_UI repository to your local machine.
    ```bash
    git clone git@github.com:cuiyixin555/NV_AIQ_UI.git
    cd NV_AIQ_UI
    ```

2. Initialize, fetch, and update submodules in the Git repository.
    ```bash
    git submodule update --init --recursive
    ```

3. Fetch the data sets by downloading the LFS files.
    ```bash
    git lfs install
    git lfs fetch
    git lfs pull
    ```

4. Create a Python environment.
    ```bash
    uv venv --seed .venv
    source .venv/bin/activate
    ```
    Make sure the environment is built with Python version `3.11` or `3.12`.
    ```bash
    uv venv --seed .venv --python 3.11
    ```

5. Install the NV_AIQ_UI toolkit library.
    ```bash
    uv sync --all-groups --all-extras
    ```
    ```bash
    uv sync
    ```
    ```bash
    uv pip install -e '.[langchain]'
    ```
    ```bash
    uv pip install -e '.[profiling]'
    ```

6. Verify the installation using the NV_AIQ_UI toolkit CLI

   ```bash
   aiq --version
   ```

   This should output the AIQ toolkit version which is currently installed.

7. For running UI, please install PyQt5

   ```bash
   pip install PyQt5
   ```

### UI: QQ chat with Nvidia AgentIQ

1. Execute UI script.
    ```bash
    python open_index.py
    ```
    ![Image text](https://github.com/cuiyixin555/NV_AIQ_UI/blob/master/index.png)

2. Input the question you want
   ```bash
   you can input like the picture and click the button Chat with AgentIQ
   ```
   ![Image text](https://github.com/cuiyixin555/NV_AIQ_UI/blob/master/chat.png)


