# Social Media Post Improvement
This application takes social media post content as input and rectifies post content based on AI critique feedback.

## Application Workflow
- User Input: The user inputs their post content (e.g., a tweet or Facebook post).
- Critique Feedback: The application provides critique feedback on the post text, suggesting improvements.
- Iterative Improvement: The user can refine the post based on the feedback, and the process repeats up to 3 times.
- Final Output: The application displays the final post content along with the critique feedback and rectifications at each step.

## Set Up the Environment
### Install the required libraries:
Create virtual environment
```bash
python3 -m venv env
source env/bin/activate
```
```bash
pip install -r requirements.txt
```

- streamlit: For the frontend.
- langgraph: For building the critique and improvement workflow.
- openai: For leveraging GPT models for critique and text generation.

### Set up your OpenAI API key:
```dotenv
OPENAI_API_KEY="your-openai-api-key"
```

## Design the LangGraph Workflow
LangGraph will be used to create a graph-based workflow for critique and improvement. Here's how to design it:

### Define Nodes:
- Critique Node: Analyzes the post and provides feedback.
- Improvement Node: Refines the post based on the feedback.
- Decision Node: Decides whether to continue iterating or stop after 3 steps.
- End Node: Stop execution

### Define Edges:

Connect the nodes to create a loop for iterative improvement.


## Run the Application
### Locally
```bash
streamlit run app.py
```

### Docker container
```bash
docker-compose up -d
```

### Access the Application:
Open your browser and navigate to http://localhost:8501

## Test and Refine
- Test the application with different post content to ensure the critique and improvement workflow works as expected.
- Refine the prompts and LangGraph nodes for better feedback and results.
