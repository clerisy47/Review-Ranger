# Review Ranger

This repository contains code for an Automatic Review Response Bot aka the Review Ranger using Rasa and Streamlit. The bot generates reviews based on user-provided text and ratings.

## Demo Video

## Setup

To run the code, you'll need to have the following dependencies installed. You can install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This command will install the necessary dependencies listed in the `requirements.txt` file, including:

- [Streamlit](https://www.streamlit.io/)
- [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/)
- [Rasa](https://rasa.com/)

## Usage

1. Clone the repository or download the `main.py` file.

### By terminal:

2. Run the application by executing the following command in your terminal:
```bash
rasa shell
```

3. Enter the input in the shell and press enter to generate a review based on the provided text.

### By streamlit:
2. Run the application by executing the following command in your terminal:

```bash
streamlit run main.py
```

3. Open the provided URL in your web browser.

4. Enter text and select ratings (out of 5) in the user interface.

5. Click the "Generate Review" button to generate a review based on the provided text and ratings.


## Contributions

Contributions are welcome! Feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributors

1. Utsav Acharya
2. Ashish Pandey
