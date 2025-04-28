# ai_playwright_demo

This project generates Playwright test code based on natural language input by utilizing a GPT model and the RAG method (Retrieval-Augmented Generation).

## Prerequisites (Quickstart)

Before running the project, make sure you have:

### Google Gemini API Key (optional)
- Get your key from [Google AI Studio](https://makersuite.google.com/)
- Save it in a `secrets.toml` file:
```
(On Windows: `C:\Users\<YourUsername>\.streamlit\secrets.toml`)

- Example contents of `secrets.toml`:
google_api_key = "YOUR_API_KEY_HERE"
```

### Python 3.8+
- Download from [python.org](https://www.python.org/downloads/)
- Check Python version:
```
bash
python --version
```
Then setup python virtual environment

```python -m venv venv

## Getting Started

```
pip install -r requirements.txt
streamlit run app.py
```


## Project Structure

- app.py — Streamlit-based user interface
- generate_test.py — Logic for building the prompt, URL detection, model generation, and HTML analysis
- examples.jsonl — Example pairs (description + code)
- best_practices.txt — Playwright best practices that are automatically included in the prompt
- retriever.py — Retrieval of examples from training data
- models.py — Model initialization (Transformer models, Gemini, etc.)
- requirements.txt — Required Python libraries

## Example Data

examples.jsonl contains prompt-code pairs in the following format:
```
{"prompt": "Verify successful login", "code": "test('login works', async ({ page }) => {\\n  await page.goto('https://example.com/login');\\n  await page.fill('#username', 'user');\\n  await page.fill('#password', 'pass');\\n  await page.click('#login');\\n  await expect(page.locator('text=Tervetuloa')).toBeVisible();\\n});"}
```
## Best Practices Guidelines
The best_practices.txt file contains Playwright best practices:
* Use user-centered selectors like getByRole, getByLabel, getByText
* Automatically wait for elements to appear; avoid hardcoded delays (waitForTimeout)
* Write clear and descriptive test names
* Follow the DRY principle (Don't Repeat Yourself)
* Test the application from a real user's perspective
* Use the Page Object Model structure in larger projects


## Additional Features
- URL detection: The system detects a URL from the user's prompt and fetches elements from that page automatically.
- HTML element analysis: Extracted buttons, input fields, and links are added to the model's prompt.
- Prompt enrichment: Examples, discovered elements, and best practices guidelines are combined into the input for the model to generate the best possible code.
- After navigation to a new page, the HTML can be re-analyzed and updated with the new element information.
