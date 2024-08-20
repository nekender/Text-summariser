# Text Summarizer Web Application

This application allows you to summarize an article by inputting the text directly into a web form.

## Requirements

Before running the application, make sure to install the following libraries:

- `Flask`
- `nltk`
- `sumy`

You can install these libraries using pip. Run the following command:

```bash
pip install flask nltk sumy

## Usage

Follow the steps below to run the text summarizer web application:

1. **Run the Server:**
   - Open your terminal.
   - Navigate to the directory containing `app.py`.
   - Execute the following command to start the server:
     ```bash
     python app.py
     ```

2. **Access the Web Interface:**
   - Open your web browser and go to `http://127.0.0.1:5000`.
   - You will see a web form where you can input your article text.

3. **Input the Article Text:**
   - Type or paste the article text into the text area provided on the web page.
   - Click on the `Get Summary` button to submit the text.

4. **View the Summary:**
   - After processing, the summary of the article will be displayed below the form on the same page.

## Conclusion

This web application provides a user-friendly way to summarize text using a web interface. Follow the instructions above to input your text and receive a summary directly in your browser.
