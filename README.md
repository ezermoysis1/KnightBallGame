# The End of the Track - Online (Work In Progress)

Welcome to the online version of "The End of the Track," a strategic game by Gaya Game.

<img src="./images/KnightBall_img_site Small.png" alt="Project Logo" width="200"/>

## About the Game

"The End of the Track" is a strategic board game that offers exciting gameplay for players of 8+ age. This online version is a work in progress.

Game rules:


## Play the Game

You can buy "The End of the Track" online by visiting the Gaya Game website:

[Buy the boardgame here](https://www.gaya-game.com/collections/strategy-game/products/the-end-of-the-track)

Enjoy the game and have fun strategizing your way to victory!



## Setup

### Setting up a virtual environment 

1.  First, clone the repository:

    ```
    git clone https://github.com/ezermoysis1/TheEndoftheTrack.git
    ```

2.  Change your directory to where you cloned the files:

    ```
    cd TheEndoftheTrack
    ```

3.  Create a virtual environment with Python 3.11.1:

    ```
    virtualenv venv --python=python3.11.1 (or just use a previous version without indicating the python version)
    ```

4.  Activate the virtual environment. You will need to activate the venv environment in each terminal in which you want to use TheEndoftheTrack.

    ```
    source venv/bin/activate
    ```
5.  Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Run the app using Streamlit

    streamlit run app.py
